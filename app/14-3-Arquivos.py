## 1 - Metodo1 =  Cadastrar uma cerveja: nome, tipo
## 2 - Metodo2 = Armazenar em um arquivo texto
## 3 - Metodo3 = Ler os dados armazenados no arquivo texto

# Método Cadastrar 
# Solicita através do console os dados para cadastro de uma cerveja
# Armazena os dados lidos do console em um dicionário
# Retorna ao final o dicionário 
def cadastrar():
    # Cria um dicionário vazio
    cerveja = {}
    # Cria uma nova chave para o dicionário (chave 'nome')  e armazena o conteudo vindo do console
    cerveja['nome'] = input('Digite o nome : ')
    # Cria uma nova chave para o dicionário (chave 'tipo') e armazena o conteudo vindo do console
    cerveja['tipo'] = input('Digite o tipo : ')
    # Retorna o dicionário com as duas chaves e dados adionados 
    return cerveja

# Método Salvar
# Abre um arquivo específico em modo de adição de dados ('a')
# Salva uma nova linha no arquivo texto aberto
# Fecha o arquivo texto
# Retorna uma mensagem informando que o dado foi salvo
def salvar(dado):
    # Abre o arquivo em formado de adição de dados (parâmetro 'a')
    # Armazena este arquivo aberto em uma variável com o nome de 'arquivo'
    arquivo = open( r'app\cerveja.txt', 'a' )
    # Adiciona uma nova linha ao arquivo através da função write()
    # Na função write é passado '\n' para pular de linha e assim adionar cada dado em uma linha separada
    arquivo.write(f'{dado}\n')
    # fecha o arquivo aberto pela função open()
    arquivo.close()
    # Retorna uma mensagem para informar que os dados foram salvos
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

