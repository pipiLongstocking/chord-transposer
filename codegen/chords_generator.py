import jinja2
import chordparser
chords_template = "chords_template.txt"
chords_data = "./chords.yaml"
output_file = "./chords2.py"
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
