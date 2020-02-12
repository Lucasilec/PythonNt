nome = 'Maykon'
sobrenome = 'Graneman'

arquivo =  open('pessoa.txt', 'a')
arquivo.write(f'  {nome};{sobrenome}\n')
arquivo.close()

arquivo =  open('pessoa.txt', 'r')
for l in arquivo:
    print( l.strip() )
arquivo.close()

