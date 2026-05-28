from flask import Flask, render_template, request
from enc_code import (
    encode_sentence, decode_sentence,
    reverse_encode, reverse_decode,
    binary_encode, binary_decode,
    atbash_encode, atbash_decode,
    morse_encode, morse_decode,
    rail_fence_encode, rail_fence_decode,
    ascii_encode, ascii_decode
)

app = Flask(__name__)

TECHNIQUES = {
    "codez":   {"encode": encode_sentence,   "decode": decode_sentence},
    "reverse": {"encode": reverse_encode,    "decode": reverse_decode},
    "binary":  {"encode": binary_encode,     "decode": binary_decode},
    "atbash":  {"encode": atbash_encode,     "decode": atbash_decode},
    "morse":   {"encode": morse_encode,      "decode": morse_decode},
    "rail":    {"encode": rail_fence_encode, "decode": rail_fence_decode},
    "ascii":   {"encode": ascii_encode,      "decode": ascii_decode},
}

CUSTOM_ALLOWED = ["codez", "reverse", "atbash", "rail"]


@app.route('/', methods=['GET', 'POST'])
def index():
    enc_result = None
    enc_original = None
    dec_result = None
    dec_original = None
    selected_technique = "codez"

    if request.method == 'POST':
        selected_technique = request.form.get('technique', 'codez')
        action = request.form.get('action')
        technique = TECHNIQUES.get(selected_technique, TECHNIQUES['codez'])
        if action == 'encode':
            enc_original = request.form.get('encode_sentence')
            enc_result = technique['encode'](enc_original)
        elif action == 'decode':
            dec_original = request.form.get('decode_sentence')
            dec_result = technique['decode'](dec_original)

    return render_template('index.html',
        page='home',
        enc_result=enc_result,
        enc_original=enc_original,
        dec_result=dec_result,
        dec_original=dec_original,
        selected_technique=selected_technique
    )


@app.route('/custom', methods=['GET', 'POST'])
def custom():
    enc_result = None
    enc_original = None
    dec_result = None
    dec_original = None
    custom_flow = []

    if request.method == 'POST':
        flow_raw = request.form.get('custom_flow', '')
        custom_flow = [t.strip() for t in flow_raw.split(',') if t.strip() in CUSTOM_ALLOWED]
        action = request.form.get('action')
        if action == 'encode':
            enc_original = request.form.get('encode_sentence')
            enc_result = enc_original
            for t in custom_flow:
                enc_result = TECHNIQUES[t]['encode'](enc_result)
        elif action == 'decode':
            dec_original = request.form.get('decode_sentence')
            dec_result = dec_original
            for t in reversed(custom_flow):
                dec_result = TECHNIQUES[t]['decode'](dec_result)

    return render_template('custom.html',
        page='custom',
        enc_result=enc_result,
        enc_original=enc_original,
        dec_result=dec_result,
        dec_original=dec_original,
        custom_flow=custom_flow
    )


@app.route('/about')
def about():
    return render_template('about.html', page='about')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
