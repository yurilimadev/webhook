import requests
import json
import time
from flask import Flask, render_template, url_for, jsonify, request, redirect
from service.disparo_service import mock_trigger
from repository.endpoint_repository import EndpointRepository


app = Flask(__name__)
repo=EndpointRepository()

@app.route('/')
def home():
    print(mock_trigger())
    return render_template('index.html')

@app.route('/cadastros-endpoint', methods=['POST'])
def cadastrar():
    if request.method == 'POST':

        endpoint = request.form.get('endpoint')
        email = request.form.get('email')
        
        repo.cadastrar(email, endpoint)
        repo.enviar_token(email)
        print(f"{email} cadastrou {endpoint} com sucesso")
        return redirect(url_for('home')) 
    

@app.route('/disparo', methods=['GET', 'POST'])
def disparar():
    print(repo)
    try:
        while True:
            requests.post(
                repo.endpoint_list['endpoint'][0],
                data=mock_trigger()
            )
            time.sleep(5)
    except:
        return "Deu ruim"

app.run(port='3000', debug=True)