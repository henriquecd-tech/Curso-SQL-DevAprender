# Criar uma abela nova com 3 colunas
# alterar o tipo de uma coluna
# renoemar uma coluna
# renomear a tabela criada
# resolução
# https://paste.pics/fdcbce6e2f5d452302db312d9ba3e6aa


'''
1 - criar uma tabela com três colunas
create table teste (
	coluna1 varchar not null,
	coluna2 varchar not null,
	coluna3 varchar not null
);

2 - alterar o tipo de uma coluna
alter table teste
alter column coluna1 int not null

3 - renomear uma coluna
exec sp_rename 'teste.coluna1', 'coluna1 - tipo inteiro'

4 - renomar a tabela criada
exec sp_rename 'teste', 'tabelaAlterada'

-- vai gerar um erro após renomear a tabela teste para tabelaAlterada
select *
from teste

select *
from tabelaAlterada

'''