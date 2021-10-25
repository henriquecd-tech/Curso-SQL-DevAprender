# Crie 2 tabelas e não permita campos vazios em duas colunas
# resolução
# https://paste.pics/72abaf49d82efe34cf29a57758f895d4
'''
create table notnull01 (
	nome varchar not null,
	idade int not null
);


create table notnull02 (
	cidade varchar not null,
	pais varchar not null
);

'''