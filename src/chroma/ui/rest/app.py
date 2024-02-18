from flask import Flask, render_template, jsonify

app = Flask(__name__)

from chroma.main import name


@app.route('/')
def index():
    colour = name(output_format='html', view=lambda x: x)
    return render_template("index.html", colour=colour)


@app.route('/colour')
def colour_endpoint():
    colour = name(output_format='json', view=lambda x: x)
    return jsonify(colour)
