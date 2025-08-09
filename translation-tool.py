from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)

translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get('text')
    src = data.get('source')
    dest = data.get('target')

    if not text or not dest:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        translated = translator.translate(text, src=src, dest=dest)
        return jsonify({'translated_text': translated.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8888)
