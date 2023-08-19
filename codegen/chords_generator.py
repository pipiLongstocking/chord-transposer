import sys
import jinja2
import chordparser
def main(chords_template, chords_data, output_file):
    try:
        chord_metadata = chordparser.generate(chords_data)
        environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader("templates/"),
        )
        template = environment.get_template(chords_template)
        with open(output_file, "w") as file:
            content = template.render(
                chords_len = chord_metadata["chord_len"],
                chord_sharps = chord_metadata["chord_sharps"],
                chord_flats = chord_metadata["chord_flats"],
                basic_chord_pattern = chord_metadata["basic_chord_pattern"],
                suffixes = chord_metadata["suffixes"],
                diagram_path = chord_metadata["diagram_path"],
                audio_path = chord_metadata["audio_path"],
            )
            file.write(content)
            print(f"...wrote {output_file}")
    except Exception as e:
        print("failed generating the chords class.", e)

if __name__ == '__main__':
    chords_template = sys.argv[1]
    chords_data = sys.argv[2]
    output_file = sys.argv[3]
    main(chords_template, chords_data, output_file)
