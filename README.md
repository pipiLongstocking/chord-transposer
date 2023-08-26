Create chord objects by specifying the chord notation.
For eg;

```
    c = chords.Chord("A#min")
```
You can transpose the chord by an integer as :

```
     c.transpose(1)             # makes this Bmin
     c.shift_flats_sharps()     # switches between flats and sharps
     c.print()                  # Prints the chord
```

More features to be added; such as:
1. Support for displaying guitar chord diagrams
2. Parsing chord webpage and playing it, given a bpm.
3. Showing the chord diagrams for the chords and the ability to transpose it.
4. Ability to play fingerstyle.