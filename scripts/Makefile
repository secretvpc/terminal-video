# Makefile for terminal-video pipeline

# Directories
RAW_DIR := assets/raw
PROCESSED_DIR := assets/processed
VISUALS_DIR := assets/visuals
CAPTURES_DIR := assets/captures

# Tools
PYTHON := python3
SIMULATE := scripts/simulate-typing.py
GURU := scripts/simulate-guru-extended.py
OVERLAY := scripts/generate-terminal-overlay.sh
RENDER := scripts/render-cast-wsl.sh

# All .cast recordings
CAST_FILES := $(wildcard $(RAW_DIR)/*.cast)
PROCESSED_CASTS := $(patsubst $(RAW_DIR)/%.cast,$(PROCESSED_DIR)/%.cast,$(CAST_FILES))
SVG_FILES := $(patsubst $(RAW_DIR)/%.cast,$(VISUALS_DIR)/%.svg,$(CAST_FILES))
MP4_FILES := $(patsubst $(RAW_DIR)/%.cast,$(CAPTURES_DIR)/%.mp4,$(CAST_FILES))
MOV_FILES := $(patsubst $(RAW_DIR)/%.cast,$(CAPTURES_DIR)/%.mov,$(CAST_FILES))

.PHONY: all simulate render overlay clean

all: simulate render overlay

simulate: $(PROCESSED_CASTS)

render: $(SVG_FILES) $(MP4_FILES)

overlay: $(MOV_FILES)

$(PROCESSED_DIR)/%.cast: $(RAW_DIR)/%.cast
	@echo "[simulate] Processing $< → $@"
	$(PYTHON) $(SIMULATE) $< > $@.tmp && \
	$(PYTHON) $(GURU) $@.tmp > $@ && \
	rm -f $@.tmp

$(VISUALS_DIR)/%.svg: $(PROCESSED_DIR)/%.cast
	@echo "[render:svg] Generating SVG $@"
	svg-term --in $< --out $@ --window --padding 10 --no-cursor --frame --theme "dracula"

$(CAPTURES_DIR)/%.mp4: $(VISUALS_DIR)/%.svg
	@echo "[render:mp4] Rendering MP4 $@"
	ffmpeg -y -loop 1 -i $< -c:v libx264 -t 10 -pix_fmt yuv420p $@

$(CAPTURES_DIR)/%.mov: $(PROCESSED_DIR)/%.cast
	@echo "[render:mov] Creating MOV $@"
	bash $(OVERLAY) $< $@
	
clean:
	rm -f $(PROCESSED_CASTS) $(SVG_FILES) $(MP4_FILES) $(MOV_FILES)
