from flask import Flask, render_template, redirect, request

from empresa import Empresa

nome= 'Site Flask'
lista_empresas = []

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo=nome)

@app.route('/empresa')
def empresa():
    return render_template('empresa.html', titulo=nome, empresas=lista_empresas)

@app.route('/cadastro-empresa')
def cadastro_empresa():
    return render_template('cadastro-empresa.html', titulo=nome )

@app.route('/salvar-empresa')
def salvar_empresa():
    e = Empresa()    
    e.nome = request.args['nome']
    e.cnpj = request.args['cnpj']
    e.descricao = request.args['descricao']

    lista_empresas.append(e)
    return redirect('/empresa')
#---- Executa o servidor flask e inicia a app
#--- Parâmetro debug=True, 
#   faz servidor reiniciar quando arquivo python for alterado

app.run(debug=True)