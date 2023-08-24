chords.py: chords.yaml
	python3 codegen/chords_generator.py chords_template.txt chords.yaml chords.py

clean:
	rm chords.py