from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count_words_and_characters', methods=['POST'])
def count_words_and_characters():
    text = request.json['text']
    word_count = len(text.split())
    char_count = len(text)

    # Simulating a delay for the loading animation
    time.sleep(3)

    return jsonify({'word_count': word_count, 'char_count': char_count})

if __name__ == "__main__":
    app.run(debug=True)
