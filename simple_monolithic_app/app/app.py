from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process_text():
    input_text = request.form['input_text']

    output_text = input_text

    if 'to_upper' in request.form:
        output_text = output_text.upper()

    if 'to_lower' in request.form:
        output_text = output_text.lower()

    if 'revert' in request.form:
        output_text = output_text[::-1]

    return render_template("index.html", input_text=input_text, output_text=output_text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
