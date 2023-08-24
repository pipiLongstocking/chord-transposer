chords.py: chords.yaml
	python codegen/chords_generator.py chords_template.txt chords.yaml chords.py

clean:
	rm chords.py