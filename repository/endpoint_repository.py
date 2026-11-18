import yagmail
from pathlib import Path
import os
from dotenv import load_dotenv


env_path = Path(__file__).resolve().parent.parent / ".env"
print("Procurando .env em:", env_path)
print("Arquivo existe?", env_path.exists())

load_dotenv(dotenv_path=env_path)

usuario = os.getenv("SMTP_USER")
senha = os.getenv("SMTP_PASSWORD")

yag = yagmail.SMTP(usuario, senha)

class EndpointRepository:

    endpoint_list = {
        "email":[],
        "endpoint":[]
    }

    token = 'uhdfaAADF123'
    def cadastrar(self,email,endpoint):
        self.endpoint_list['email'].append(email)
        self.endpoint_list['endpoint'].append(endpoint)
    def enviar_token(self, email):
        try:
            html_msg = f"""
            <div style="font-family: Arial, sans-serif; color: #333; max-width: 600px;">
                <h2 style="color: #2e7d32;">Olá!</h2>
                <p>Seu email foi cadastrado com <strong>SUCESSO</strong>:</p>
                <ul>
                    <li><strong>Email:</strong> {email} </li>
                    <li><strong>Valor:</strong> {self.token}</li>
                </ul>
                <p style="font-size: 12px; color: #777;">
                    Este é um e-mail automático do nosso sistema de notificações.
                </p>
            </div>
            """
            yag.send(
                to=email,
                subject="Envio de Token - Simulador",
                contents=html_msg
            )

            print('Email Enviado')
        except Exception as e:
            print(f"Ocorreu um erro no envio do Token: {e}")

if __name__ == '__main__':
    repo = EndpointRepository()

    #cadastrando
    email = 'dimitriribeiro01@gmail.com'
    endpoint = 'https://webhook.site/d56e6c03-8c91-4a46-891e-04c0f936f32f'
    
    repo.cadastrar(
        email,
        endpoint
    )

    print(repo.endpoint_list)

    repo.enviar_token(email)
