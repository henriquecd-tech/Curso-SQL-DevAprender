# Crie 2 tabelas e depois exclua
# resolução
# https://paste.pics/c63833f7e0287915815bcb0f5dc71201
'''
1º criação da primeira tabela
create table teste1 (
	nome varchar not null,
	idade int not null
);

2º criação da segunda tabela
create table teste2 (
	cidade varchar not null,
	pais varchar not null
);

3º retornar tabela 1
select *
from teste1

4º retornar tabela 2
select *
from teste2

5º exclui as duas tabelas criadas (teste1 e teste2)
drop table teste1
drop table teste2

6º retornar erro tabela 1
select *
from teste1

7º retornar erro tabela 2
select *
from teste2
'''