from flask import Flask, render_template, request
import openai

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def home():
    if request.method == 'POST':
        # ler arquivo com chave da api criptografada, descriptografar e rodar.
        openai.api_key = 'myapikey'

        # Receber o texto digitado pelo usuário
        usertext = request.form['textimg']

        response = openai.Image.create(
            # ler resultado do text box da pagina
            # testar caso não for possível gerar imagem com textos em português
            # utilizar alguma lib para traduzir os textos automaticamente
            prompt= usertext,
            # numero de imagens a serem geradas
            n=1,
            # tamanho das imagens, permitir posteriormente interação com o valor
            size='1024x1024'
        )
        # verificar possibilidade de exibir a imagem na página e fazer o download automaticamente
        image_url = response['data'][0]['url']
        return render_template("index.html", linkimage= image_url, seed= usertext)
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)