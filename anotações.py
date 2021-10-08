# instalação do SQL + SSMS
# criação de bancos via interface SSMS e comandos -> create database nome_do_banco; e executar (f5)
# derrubar / excluir dbs -> drop database nome_do_banco; ou botão direito -> excluir
# comando mais básico e um dos mais usados no SQL -> SELECT


'''SELECT E FROM'''
# SELECT -> comando universal do SQL (a ideia básica é selecionar uma coluna ou mais na tabela)
# SEELCT nome_da_coluna1, nome_da_coluna2 FROM nome_da_tabela; -> extrai as informações que estão dentro dessas colunas
# SELECT * FROM nome_da_tabela; -> O * indica que todas as colunas serão selecionadas
# por convenção, todos os comandos em SQL são em letra maiuscula


'''DISTINCT'''
# é usado para omitir dados duplicados de uma tabela e retorna somente dados únicos.
# sintaxe -> SELECT DISTINCT nome_da_coluna1, nome_da_coluna2 FROM nome_da_tabela
# exemplo prático -> SELECT DISTINCT FirstName FROM Person.Person;


'''WHERE'''
# para extrair dados especificos de uma tabela podemos utilizar o comando where
# sintaxe -> SELECT coluna1,coluna2,coluna3 FROM tabela WHERE condição
# comentários em SQL são feitos usando -- ou /* e fechando com */
# exemplo prático -> SELECT * FROM person.Person WHERE LastName = 'miller'
# exemplo prático com operadores lógicos - SELECT * FROM person.Person WHERE LastName = 'miller' and FirstName = 'anna'
# exemplo prático -> SELECT * FROM Production.Product WHERE Color = 'blue' or Color = 'black';
# exemplo prático -> SELECT * FROM Production.Product WHERE ListPrice > 1500;
# exemplo prático -> SELECT * FROM Production.Product WHERE ListPrice > 1500 and ListPrice < 5000;
# exemplo prático -> SELECT * FROM Production.Product WHERE Color <> 'red';

'''
OPERADOR    DESCRIÇÃO
=           IGUAL
>           MAIOR QUE
<           MENOR QUE
>=          MAIOR QUE OU IGUAL
<=          MENOR QUE OU IGUAL
<>          DIFERENTE DE
AND         OPERADOR LÓGICO E
OR          OPERADOR LÓGICO OU  
'''

'''COUNT'''
# O comando count serve para retornar / devolver o número de linhas que seencaixam em uma determinada condição
# # sintaxe -> select count (* ou nome da conluna. Tbm é possivel usar o distinct no inicio) from tabela
# selec count (distinct *) from tabela
# exemplo prático -> select count(*) from Person.Person; (retorna a informação de que existem 19972) linhas nessa busca
# exemplo prático -> select count (distinct title) from person.Person;


'''Top'''
# o comando top basicamente limita a quantidade de dados que é retornada em um select
# é comum termos milhões de linhas em Dbs de grandes aplicações, o top nos ajuda a limitar a qutd de dados retornados
# sintaxe selec top qtd_retornada from tabela -> select 10 * from tabela
# select top 15 * from Production.Product;

'''ORDER BY'''
# Ordey by permite que você ordene os resultados em alguma coluna de forma crescer ou decrescente
# sintaxe -> select coluna1, coluna2, from tabela order by coluna1 asc/desc (ordenação crescente ou decrescente)
# exemplo prático -> select * from Person.Person order by FirstName asc;
# exemplo prático -> select * from Person.Person order by FirstName desc;
# exemplo prático -> select * from Person.Person order by FirstName asc, LastName desc;
# exemplo prático -> select FirstName, LastName from Person.Person order by FirstName asc, LastName desc;
# como boa prática, é importante inserir no select os parametros que serão usados no order by para ordenção.

'''BETWEEN'''
# o between é usado para encontrar um valor entre um valor minimo e um valor máximo
# sintaxe -> valor BETWEEN minimo AND máximo
# valor >= minimo AND valor <= máximo
# exemplo prático select * from Production.Product where ListPrice between 1000 and 1500;
# exemplo prático usando o not -> select * from Production.Product where ListPrice  not between 1000 and 1500;
'''retorna todos os valores que não esntre 1000 e 1500'''
# também é possivel usar o between com datas
# exemplo prático
# select *
# from HumanResources.Employee
# where HireDate between '2009/01/01' and '2010/01/01';

# exemplo prático
# select *
# from HumanResources.Employee
# where HireDate between '2009/01/01' and '2010/01/01'
# order by HireDate;

'''IN'''
# o operador in é usado junto com o where para verificar se um item corresponde a qualquer item na lista de valores
# sintaxe -> valor IN (valor1, valor2)
# color IN ('blue', 'black')
# basicamente o IN faz uma busca no DB e sempre que ele retornar um valor que corresponde aos atributos passados, ele
# retorna essas informações.
# essa sintaxe tbm é utilziada valor IN (select valor from nomeDaTabela) -> isso e chamado de sub-select ou sub-query
# exemplo prátco ->  select * from Person.Person where BusinessEntityID in (2,7,13);
# essa é uma forma mais rápida e assertiva de buscar informações.
'''
COMAPARATIVO COM IN E SEM IN
select * from Person.Person where BusinessEntityID in (2,7,13); (com in)
x
select * from Person.Person where BusinessEntityID = 2 or BusinessEntityID = 7 or BusinessEntityID = 13; (sem in)
'''

# é possivel usar o not para efeitos de negação(retorno todos os itens que não estão dentro da condição passada)

'''LIKE'''
# exemplo de aplicação prática; Você precisa achar um nome em que as três primeiras letras são ovi mas não sabe o resto"
# é possivel montar uma query com o like para performar essa operação no db
# select * from person,person firstname like 'ovi%'
# o sinal de % é uma máscara e quer dizer que não importa o que venha depois, tudo que tenha ovi deve retornar.
# exemplo prático -> select * from Person.Person where FirstName like 'ovi%';
# exemplo prático com a máscara no inicio, retorna todos os nomes que terminal com o parametro passado
# -> select * from Person.Person where FirstName like '%to';
# exemplo prático com máscaras no inicio e no final para retornar todos os elementos que tem o parametro no meio
# -> select * from Person.Person where FirstName like '%essa%';
# exemplo prático para sinalizar apenas um caractere
# -> select * from Person.Person where FirstName like '%ro_'
# o like não é case sensitive no SQL
