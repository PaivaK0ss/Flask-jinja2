from flask import Flask, render_template
import dados

app = Flask(__name__)

jogos = dados.carregar_do_arquivo()

@app.route('/jogos')
def listar_jogos():
    return render_template('jogos.html', jogos=jogos)

@app.route('/api/jogos', methods=['GET', 'POST'])
@app.route('/api/jogos/<codigo>', methods=['GET', 'DELETE', 'POST'])
def jogos_api(codigo=None):
    return {"mensagem": "rota funcionando"}

if __name__ == "__main__":
    app.run(debug=True)