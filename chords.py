import re


# ChordError inherits the exception class
class ChordError(Exception):
    pass


class Chord:
    """
    Chord denotes a musical chord.
    """
    chords_len = 12
    chord_sharps = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    chord_flats = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
    basic_chord_pattern = r'^(?i)[ABCDEFG]#?'
    suffixes = ["", "maj", "min", "7", "maj7", "min7", "dim", "aug", "sus4", "sus2", "maj6", "6", "min6", "dom7",
                "dom9"]

    def __init__(self, notation: str):
        match = re.search(self.basic_chord_pattern, notation)
        if not match:
            raise ChordError("the notation is an invalid chord")
        parent_chord = match.group(0)
        remaining_notation = notation[len(parent_chord):]
        if remaining_notation not in self.suffixes:
            raise ChordError("the notation is an invalid chord")
        self.parent_chord = parent_chord
        self.suffix = remaining_notation
        try:
            index = self.chord_sharps.index(self.parent_chord)
            self.index = index
            self.sharps = True
        except ValueError:
            index = self.chord_flats.index(self.parent_chord)
            self.index = index
            self.sharps = False
        # TODO
        self.path_to_sound = ""
        self.path_to_chord_folder = ""

    def transpose(self, scale):
        """
        transpose transposes the scale by and integer, positive or negative
        :param scale:
        :return:chord
        """
        self.index = (self.index + scale) % self.chords_len
        if self.sharps:
            self.parent_chord = self.chord_sharps[self.index]
        else:
            self.parent_chord = self.chord_flats[self.index]
        # TODO
        self.path_to_sound = ""
        self.path_to_chord_folder = ""

    def print(self):
        """
        print prints the chord onto the console
        :return:
        """
        print(f'{self.parent_chord}{self.suffix}')

    def shift_flats_sharps(self):
        """
        flips between the sharp/flat based notation when called.
        :return:
        """
        if self.sharps:
            self.sharps = False
            self.parent_chord = self.chord_flats[self.index]
        else:
            self.sharps = True
            self.parent_chord = self.chord_sharps[self.index]
