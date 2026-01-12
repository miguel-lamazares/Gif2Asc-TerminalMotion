# Makefile for Gif2Asc-TerminalMotion
# Integrates full_process.sh, quick_start.sh, and execute_last.sh
# PNGPersonalizer.py is optional (set PERSONALIZE=1 to enable)

# Project root (adjust if needed)
PROJECT_ROOT = .

# Virtual environment
VENV_DIR = $(PROJECT_ROOT)/.venv
PYTHON = $(VENV_DIR)/bin/python

# Paths for full process (Engine)
FRAME_EXTRACTOR_FULL = $(PROJECT_ROOT)/Gif/Gif_to_asc/Gif-to-png/FrameExtractor.py
ASC_CONVERTER_FULL = $(PROJECT_ROOT)/Gif/Gif_to_asc/png-to-asc/AscConverter.py
PNG_PERSONALIZER_FULL = $(PROJECT_ROOT)/Gif/Gif_to_asc/png-to-asc/PNGPersonalizer.py
RENDER_C_FULL = $(PROJECT_ROOT)/Engine/Render/Render.c
RENDER_OUT_FULL = $(PROJECT_ROOT)/Engine/Render/Render
PLAYER_JAVA_FULL = $(PROJECT_ROOT)/Engine/Player/Player.java
PLAYER_CLASS_FULL = Gif2Asc.Engine.Player.Player

# Paths for quick process (Gif) - note typo in FrameExtractor
FRAME_EXTRACTOR_QUICK = $(PROJECT_ROOT)/Gif/Gif_to_asc/Gif-to-png/FrameExatractor.py
ASC_CONVERTER_NO_ARGS_QUICK = $(PROJECT_ROOT)/Gif/Gif_to_asc/png-to-asc/AscConverterNoArgs.py
RENDER_C_QUICK = $(PROJECT_ROOT)/Gif/Render/Render.c
RENDER_OUT_QUICK = $(PROJECT_ROOT)/Gif/Render/Render
PLAYER_JAVA_QUICK = $(PROJECT_ROOT)/Gif/Player/Player.java
PLAYER_CLASS_QUICK = Gif.Player.Player

# Personalization flag (0=skip, 1=enable)
PERSONALIZE ?= 0

.PHONY: all full quick last personalized venv_check clean

# Default target
all: full

# Full process with Engine (optionally with personalization)
full: run_full

# Quick process with Gif (no personalization, no interactive questions)
quick: run_quick

# Only compile and run (assumes frames already extracted and converted)
last: compile_c_full compile_java_full
	cd $(PROJECT_ROOT) && java $(PLAYER_CLASS_FULL)

# Full process with personalization forced on
personalized: PERSONALIZE = 1
personalized: full

# Check virtual environment exists
venv_check:
	@test -d $(VENV_DIR) || (echo "Virtualenv not found. Run ./setup_env.sh first." && exit 1)

# --- Full process chain ---
run_full: compile_java_full venv_check
	@echo "Running animation (full)..."
	cd $(PROJECT_ROOT) && java $(PLAYER_CLASS_FULL)

compile_java_full: compile_c_full
	@echo "Compiling Java player (full)..."
	javac $(PLAYER_JAVA_FULL)

compile_c_full: convert_full
	@echo "Compiling C render (full)..."
	gcc $(RENDER_C_FULL) -O3 -o $(RENDER_OUT_FULL)

convert_full: personalize_full venv_check
	@echo "Converting to ASCII (full)..."
	$(PYTHON) $(ASC_CONVERTER_FULL)

personalize_full: extract_full venv_check
ifeq ($(PERSONALIZE),1)
	@echo "Personalizing PNGs..."
	$(PYTHON) $(PNG_PERSONALIZER_FULL)
else
	@echo "Skipping PNG personalization."
endif

extract_full: venv_check
	@echo "Extracting frames (full)..."
	$(PYTHON) $(FRAME_EXTRACTOR_FULL)

# --- Quick process chain ---
run_quick: compile_java_quick venv_check
	@echo "Running animation (quick)..."
	cd $(PROJECT_ROOT) && java $(PLAYER_CLASS_QUICK)

compile_java_quick: compile_c_quick
	@echo "Compiling Java player (quick)..."
	javac $(PLAYER_JAVA_QUICK)

compile_c_quick: convert_quick venv_check
	@echo "Compiling C render (quick)..."
	gcc $(RENDER_C_QUICK) -O3 -o $(RENDER_OUT_QUICK)

convert_quick: extract_quick venv_check
	@echo "Converting to ASCII (quick, no args)..."
	$(PYTHON) $(ASC_CONVERTER_NO_ARGS_QUICK)

extract_quick: venv_check
	@echo "Extracting frames (quick)..."
	$(PYTHON) $(FRAME_EXTRACTOR_QUICK)

# Clean generated files (optional)
clean:
	@echo "Cleaning compiled binaries..."
	rm -f $(RENDER_OUT_FULL) $(RENDER_OUT_QUICK)
	@echo "Cleaning Java classes..."
	rm -f $(PROJECT_ROOT)/Engine/Player/*.class $(PROJECT_ROOT)/Gif/Player/*.class
	@echo "Cleaning extracted frames and ASCII files..."
	# Add commands to remove PNG and ASC files if desired