.PHONY: all typing guru svg mp4 overlay clean

# Input/output files
RAW_CAST=assets/raw/demo.cast
TYPED_CAST=assets/processed/demo-typed.cast
GURU_CAST=assets/processed/demo-guru.cast
SVG=assets/visuals/demo.svg
MP4=assets/captures/demo.mp4
MOV=assets/captures/demo-overlay.mov

all: typing guru svg mp4 overlay

typing:
	./scripts/simulate-typing.py $(RAW_CAST) $(TYPED_CAST)

guru:
	./scripts/simulate-guru-extended.py $(TYPED_CAST) $(GURU_CAST)

svg:
	svg-term --in $(GURU_CAST) --out $(SVG) --window --theme dracula --font "JetBrains Mono"

mp4:
	ffmpeg -loop 1 -i $(SVG) -t 10 -pix_fmt yuv420p $(MP4)

overlay:
	scripts/generate-terminal-overlay.sh $(GURU_CAST) dracula "JetBrains Mono" 10 30

clean:
	rm -f $(TYPED_CAST) $(GURU_CAST) $(SVG) $(MP4) $(MOV)
