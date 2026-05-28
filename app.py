from flask import Flask, render_template, request
from enc_code import encode_sentence, decode_sentence

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    enc_result = None
    enc_original = None
    if request.method == 'POST' and 'encode_sentence' in request.form:
        enc_original = request.form.get('encode_sentence')
        enc_result = encode_sentence(enc_original)
    return render_template('index.html', enc_result=enc_result, enc_original=enc_original)

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    dec_result = None
    dec_original = None
    if request.method == 'POST' and 'decode_sentence' in request.form:
        dec_original = request.form.get('decode_sentence')
        dec_result = decode_sentence(dec_original)
    return render_template('index.html', dec_result=dec_result, dec_original=dec_original)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)