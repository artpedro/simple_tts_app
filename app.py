from flask import Flask, render_template, request, send_from_directory
import os
from datetime import datetime
from api.tts_controller import generate_audio

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'audio')

# Configure available options
SPEAKERS = ['Claribel Dervla', 'Daisy Studious', 'Gracie Wise', 'Tammie Ema', 'Alison Dietlinde', 'Ana Florence', 'Annmarie Nele', 'Asya Anara', 'Brenda Stern', 'Gitta Nikolina', 'Henriette Usha', 'Sofia Hellen', 'Tammy Grit', 'Tanja Adelina', 'Vjollca Johnnie', 'Andrew Chipper', 'Badr Odhiambo', 'Dionisio Schuyler', 'Royston Min', 'Viktor Eka', 'Abrahan Mack', 'Adde Michal', 'Baldur Sanjin', 'Craig Gutsy', 'Damien Black', 'Gilberto Mathias', 'Ilkin Urbano', 'Kazuhiko Atallah', 'Ludvig Milivoj', 'Suad Qasim', 'Torcull Diarmuid', 'Viktor Menelaos', 'Zacharie Aimilios', 'Nova Hogarth', 'Maja Ruoho', 'Uta Obando', 'Lidiya Szekeres', 'Chandra MacFarland', 'Szofi Granger', 'Camilla Holmström', 'Lilya Stainthorpe', 'Zofija Kendrick', 'Narelle Moon', 'Barbora MacLean', 'Alexandra Hisakawa', 'Alma María', 'Rosemary Okafor', 'Ige Behringer', 'Filip Traverse', 'Damjan Chapman', 'Wulf Carlevaro', 'Aaron Dreschner', 'Kumar Dahl', 'Eugenio Mataracı', 'Ferran Simen', 'Xavier Hayasaka', 'Luis Moray', 'Marcos Rudaski']
LANGUAGES = ['en', 'es', 'fr', 'de', 'it', 'pt', 'pl', 'tr', 'ru', 'nl', 'cs', 'ar', 'zh-cn', 'hu', 'ko', 'ja', 'hi']
AUDIO_FORMAT = "wav"

@app.route('/')
def index():
    return render_template('index.html', speakers=SPEAKERS, languages=LANGUAGES)

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    speaker = request.form['speaker']
    language = request.form['language']
    
    # Simple filename using timestamp
    filename = f"output_{datetime.now().strftime('%Y%m%d%H%M%S')}.{AUDIO_FORMAT}"
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    try:
        generate_audio(text, speaker, language, output_path)
        return {'status': 'success', 'audio_url': f'/static/audio/{filename}'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}, 500

@app.route('/static/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)