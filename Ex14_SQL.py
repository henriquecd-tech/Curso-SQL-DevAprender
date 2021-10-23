# Crie uma tabela nova
# insira uma linha de dados nela
# insira 3 linhas de dados ao mesmo tempo
# crie uma segudan tabela
# insira 1 linha nessa tabela nova
# copie os dados da segunda tabela para a primeira
# https://paste.pics/4dafc0e9e2c0dc72a33e7e7d35ee100f
# resolução
'''
create table alunos (
	nome varchar(40) not null,
	curso varchar (40) not null
);

insert into alunos (nome, curso)
values ('henrique', 'comércio exterior')

insert into alunos(nome, curso)
values
('heitor', 'economia e negocios'),
('thayna', 'marketing digital'),
('artur', 'analise e desenvolvimento de software');

select *
from alunos


create table graduandos (
	nome varchar(40) not null,
);

insert into graduandos(nome)
values ('joão')


insert into graduandos (nome)
select nome
from alunos

select *
from graduandos

'''

