# Crie 2 tabelas novas e uma restrição para cada uma delas.
# resolução
'''
1º criação da primeira tabela com restrição númerica

create table restriteste1 (
	nome varchar(30) not null,
	idade int check (idade >= 18)
);

2º inserção de dados na tabela e retorno de erro
insert into restriteste1 (nome, idade)
values
	('', 15)

3º criação da segunda tabela com restrição númerica
create table restriteste2 (
	cidade varchar not null,
	cod_do_pais int check (cod_do_pais < 3)
);

4º inserção de dados na tabela conforme restrição
insert into restriteste2 ( cidade, cod_do_pais)
values ('', 2)

'''