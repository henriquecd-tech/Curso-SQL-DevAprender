# Desafio
# crie tabelas que se relacionam entre si

'''
1º tabela criada
CREATE TABLE Cliente (
	nomeDoCliente varchar(20) not null,
	idadeDoCliente int not null,
	idDoCliente int primary key
);

select *
from Cliente
'''

'''
2º tabela criada
CREATE TABLE Vendas (
	protocoloDaVenda int not null,
	valorDaVenda int not null,
	idDoCliente int foreign key REFERENCES Cliente (idDoCliente)
);

select *
from Vendas
'''


