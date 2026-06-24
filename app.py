from flask import Flask, render_template, request, redirect, jsonify, url_for
import dados

app = Flask(__name__)

jogos = dados.carregar_do_arquivo()

@app.route('/')
def redirecionar_pagina():
    return redirect('/jogos')

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

@app.route('/jogos/alterar/<codigo>', methods=['GET', 'POST'])
def alterar_jogo(codigo=None):
    for i, jogo in enumerate(jogos):
        if jogo['codigo'] == codigo:
            if request.method == 'GET':
                return render_template('edit.html', jogo=jogo)
            jogo_atualizado = {
                'codigo': request.form.get('codigo'),
                'nome': request.form.get('nome'),
                'criador': request.form.get('criador'),
                'genero': request.form.get('genero'),
                'tamanho': request.form.get('tamanho'),
                'ano_lancamento': request.form.get('ano_lancamento'),
                'plataforma': request.form.get('plataforma')
            }
            jogos[i] = jogo_atualizado
            dados.salvar_no_arquivo(jogos)
            return redirect('/jogos')
    return redirect('/jogos')

@app.route('/jogos/excluir/<codigo>', methods=['GET'])
def excluir_jogo(codigo):
    for i, jogo in enumerate(jogos):
        if jogo['codigo'] == codigo:
            del jogos[i]
            break
    dados.salvar_no_arquivo(jogos)
    return redirect('/jogos')

if __name__ == "__main__":
    app.run(debug=True)