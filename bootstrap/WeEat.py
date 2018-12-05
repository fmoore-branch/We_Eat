from flask import Flask, render_template
app = Flask(__name__, static_url_path='')

@app.route('/')
def bootstrap():
    return render_template('index.html', title="Gabe's Page")

