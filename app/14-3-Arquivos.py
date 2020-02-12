## 1 - Metodo1 =  Cadastrar uma cerveja: nome, tipo
## 2 - Metodo2 = Armazenar em um arquivo texto
## 3 - Metodo3 = Ler os dados armazenados no arquivo texto


def cadastrar():
    cerveja = {}
    cerveja['nome'] = input('Digite o nome : ')
    cerveja['tipo'] = input('Digite o tipo : ')
    return cerveja

def salvar(dado):
    arquivo = open( r'app\cerveja.txt', 'a' )
    arquivo.write(f'{dado}\n')
    arquivo.close()
    return 'Dado salvo no arquivo'


# Metodo ler :
# Abrirá um arquivo texto específico 
# Tratará os dados 
# Armazenará os dados tratados em uma lista
# Retornará a lista com os dados
def ler():
    # Criando uma lista vazia para armazenar os dados vindos do arquivo texto
    lista = []
    # Open - Abrir um arquivo, Primeiro parametro= nome do arquivo, segundo parametro = tipo de abertura
    # 'r' = abre no formato de leitura, gerando uma lista onde cada item representa uma linha do arquivo
    arquivo = open(r'app\cerveja.txt', 'r')
    for linha in arquivo:
        # Strip retira '\n', '\t' e espaços em branco de uma string
        # '\n' = pula linha
        # '\t' = cria espaço de tabulação (5 espaços em branco)
        linha_tratada = linha.strip()
        # Split - Separa uma string de acordo com uma condição e armazena em um vetor
        vetor = linha_tratada.split(';')
        # Usando f-strings para formatar o dado que seja mais visual para o usuário
        dado_formatado = f"Nome :  {vetor[0]} --- Tipo : {vetor[1]} "
        # Adiciona o dado formatado à lista        
        lista.append(dado_formatado)
    # Após a execução do for retorna a lista 
    return lista
# Função formatar_dado:
# Recebe um dicionario
# Usa f-strings para formatar o dado
# Retorna o dado formatado 
def formatar_dado(dado):
    # Usando F-String para a formatação do dicionario recebido por parâmetro(dado)
    dado_formatado = f"{dado['nome']};{dado['tipo']}"
    # Retorna o dado formatado
    return dado_formatado

c = cadastrar()
c = formatar_dado(c)
mensagem = salvar(c)
print(mensagem)
cervejas = ler()

for cv in cervejas:    
    print( cv )

