from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def ola():
    nome = request.args.get("nome", "Coppi")
    return f'Olá, {escape(nome)}!'

@app.route('/home')
def home():
    nome = request.args.get("nome", "Visitante")
    return render_template('home.html', nome=nome)

@app.route('/entrar')
def entrar():
    return render_template('entrar_form.html')

if __name__ == "__main__":
    app.run(debug=True)