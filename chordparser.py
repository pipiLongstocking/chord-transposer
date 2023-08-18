#The yaml parser file should do the following
#
# Read "suffixes" and make a list such as suffixes = ["", "maj", "min", "7", "maj7", "min7", "dim", "aug", "sus4", "sus2", "maj6", "6", "min6", "dom7",
#                 "dom9"]

# Read "diagram_path" and store it
# Read "audio_path" and store it
# Read "basic_chord_pattern" and store it

# Read "chords"
# Break it into "chord_sharps" and "chord_flats" and fill the list"

import yaml

def generate(path: str):
    with open(path, 'r') as file:
        data = yaml.safe_load(file)
        try:
            suffixes = data["suffixes"]
            diagram_path = data["diagram_path"]
            audio_path = data["audio_path"]
            basic_chord_pattern = data["basic_chord_pattern"]
            basic_chords = data["basic_chords"]
            chord_sharps = []
            chord_flats = []
            for chord in basic_chords:
                c = chord["name"]
                chord_flats.append(c)
                chord_sharps.append(c)
                if chord["sharp"] is True:
                    chord_sharps.append(f"{c}#")
                if chord["flat"] is True:
                    chord_flats.append(f"{c}b")
            res = {
                "suffixes": suffixes,
                "diagram_path": diagram_path,
                "audio_path": audio_path,
                "basic_chord_pattern": basic_chord_pattern,
                "chord_sharps": chord_sharps,
                "chord_flats": chord_flats,
                "chord_len": len(chord_sharps)
            }
            return res
        except KeyError:
            print("The key isn't present in the dictionary")
        return None