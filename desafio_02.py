import csv # Importação do csv.

listaOrdenada = []; # Lista onde guardará os registros.

arquivo = csv.reader(open('funcionarios.csv'), delimiter=';'); # Método para ler o arquivo csv.
next(arquivo); # Pula a primeira informação da lista(cabeçalho) do arquivo. Assim, facilita na tratativa da lista caso necessário.
for linha in arquivo: # Método para percorrer a lista
  listaOrdenada.append(linha); # Apos retornar uma lista para cada conjunto de informação, adicionára em outra lista.

ordenaNome = lambda nome: nome[1]; # Lambda para acessar o índice de 'NOME'.
listaOrdenada.sort(key=ordenaNome); # Passamos a lambda no sort para a ordenação.
print(listaOrdenada);

