# Desafio 1
# quantos produtos temos cadastrados no sistema que custam mais de 1500 dolares?
# resolução -> select COUNT (*) from Production.Product where ListPrice > 1500;
# alternativa -> select COUNT (ListPrice) from Production.Product where ListPrice > 1500;
# https://paste.pics/91cad7a31e63af02fe40b0ced14f48b8

'''
Dicas - Desafio 1
- você terá que usar a tabela production.produtc
- terá que usar Count e where mais algum operador de comparação
'''


# Desafio 2
# quantas pessoas temos com o sobrenome que inicia com a letra p
# resolução -> select count(LastName) from Person.Person where LastName like 'p%';
# https://paste.pics/b667e494443be216dc0bb247dc273382

'''
Dicas - Desafio 2
- terá que usar a tabela person.person
- usar o count, where e like
'''

# Desafio 3
# Em quntas cidades únicas estão cadastrados nossos clientes?
# resolução -> select count(distinct City) from Person.Address
# https://paste.pics/c829e82b208fef1acb5cd61099ca2965

'''
Dicas - Desafio 3
- você terá que usar a tabela person.address
- você terá que usar count e distinct
'''

# Desafio 4
# Quais são as cidades únicas que temos cadastradas em nosso sistema
# resolução -> select distinct City from Person.Address;
# https://paste.pics/741aa6dd53c17cda2f9202584fc3b3c3
'''
Dicas - Desafio 4
- terá que usar a tabela person.address
- será similar a resposta anterior
'''


# Desafio 5
# quantos produtos vermelhos tem o preço entre 500 - 1000 dolares
# resolução -> select * from Production.Product where Color = 'red' and ListPrice between 500 and 1000
# alternativa -> select count (*) from Production.Product where Color = 'red' and ListPrice between 500 and 1000
# https://paste.pics/aab3c52d64d945c517a4876cf863a485

'''
Dicas - Desafio 5
- você terá que usar a tabela production.product
- você terá que usar where, between
'''

# Desafio 6
# Quantos produtos cadastrados tem a palavra 'road' no nome?
# resolução -> select count(*) from Production.Product where name like '%road%';
# https://paste.pics/c58a9bbd0fbd39649d5d0da58952953c

'''
Dicas - Desafio 6
- terá que usar a tabela production.product
- terá que usar count e like
'''


