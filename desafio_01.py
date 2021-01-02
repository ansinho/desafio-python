estagiarios = [ # Declarando a lista de dicionários
  {
    'nome': 'Anderson B David',
    'idade': 23,
    'curso': 'Sistemas de Informação',
    'função': 'Fron-end'
  },
  {
    'nome': 'Abel Max Batista',
    'idade': 24,
    'curso': 'Análise e Desenvolvimento de Sistemas',
    'função': 'DBA'
  },
  {
    'nome': 'Raul Andrade',
    'idade': 21,
    'curso': 'Sistemas de Informação',
    'função': 'Dev Mobile'
  },
  {
    'nome': 'Yan Almeida',
    'idade': 21,
    'curso': 'Engenheria de software',
    'função': 'Back-end',
  },
  {
    'nome': 'Neander Wendel',
    'idade': 23,
    'curso': 'Sistemas para Internet',
    'função': 'Front-end'
  }
];


listNames = []; # Declarando a lista de nomes


for estagiario in estagiarios: # Percorrendo a lista de dicionários
  if 'nome' in estagiario: # Identificando se nos dicionários exite a chave 'nome'.
    listNames.append(estagiario['nome']); # Caso exista, adicionará o valor da chave 'nome' na lista de nomes.

listNames.sort(); # Ordena a lista.
print(listNames);