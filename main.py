from flask import Flask, render_template, url_for, jsonify, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def response():
    if request.method == 'POST':
        endpoint = request.form.get('endpoint')
        email = request.form.get('email')
        return jsonify(
            {
                'endpoint':endpoint,
                'email':email
            }
        )
    return render_template('index.html')
app.run(port='5000', debug=True)