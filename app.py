from flask import Flask, render_template, request, redirect, jsonify
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

@app.route('/jogos/criar', methods=['GET', 'POST'])
def criar_jogos():
    if request.method == 'POST':
        novo_jogo = {
            'codigo': request.form.get('codigo'),
            'nome': request.form.get('nome'),
            'criador': request.form.get('criador'),
            'genero': request.form.get('genero'),
            'tamanho': request.form.get('tamanho'),
            'ano_lancamento': request.form.get('ano_lancamento'),
            'plataforma': request.form.get('plataforma')
        }
        for jogo in jogos:
            if jogo['codigo'] == novo_jogo['codigo']:
                return jsonify("Jogo já está cadastrado"), 200
        jogos.append(novo_jogo)
        dados.salvar_no_arquivo(jogos)
        return redirect(listar_jogos())
    else:
        return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)