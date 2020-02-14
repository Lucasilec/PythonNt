from flask import Flask, render_template 

nome= 'Site Flask'
lista_empresas = ['Proway', 'Hbsis', 'TSystems', 'Senior', 'Philips']

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo=nome)

@app.route('/empresa')
def empresa():
    return render_template('empresa.html', titulo=nome, empresas=lista_empresas)

#---- Executa o servidor flask e inicia a app
#--- Parâmetro debug=True, 
#   faz servidor reiniciar quando arquivo python for alterado

app.run(debug=True)