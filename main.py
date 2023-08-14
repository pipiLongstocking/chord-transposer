import chords

if __name__ == '__main__':
    c = chords.Chord("A#min")
    c.shift_flats_sharps()
    c.transpose(1)
    c.print()
