# Simple TTS Web Application

[![Flask](https://img.shields.io/badge/Flask-3.0.0-blue.svg)](https://flask.palletsprojects.com/)
[![XTTS](https://img.shields.io/badge/Coqui-XTTS_v2-green.svg)](https://github.com/coqui-ai/TTS)

A lightweight web-based Text-to-Speech (TTS) prototype application using Flask and Coqui's XTTS_v2 model.

## Features

- Text input field for TTS conversion
- Speaker selection dropdown
- Language selection dropdown
- Real-time audio generation
- Loading spinner during processing
- Audio player with controls
- Simple web interface
- Error handling and validation

## Prerequisites

- Python 3.7+
- pip package manager
- Coqui TTS setup (XTTS_v2)
- Web browser with audio support
- Rust

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-tts-app.git
   cd simple-tts-app
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Access the application in your browser:
   ```
   http://localhost:5000
   ```

3. Enter text, select speaker and language, then click "Generate Speech".

4. Play the generated audio using the built-in player.

## Project Structure

```
simple-tts-app/
├── api/                 # TTS controller module
├── static/              # Static files (CSS, audio)
├── templates/           # HTML templates
├── app.py               # Main application entry point
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
```

## Notes

- This is a prototype - not recommended for production use.
- Audio files are stored in `static/audio/`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
