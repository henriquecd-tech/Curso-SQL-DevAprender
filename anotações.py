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
# O comando count serve para retornar / devolver o número de linhas que se encaixam em uma determinada condição
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

'''MIN, MAX, SUM, AVG'''
# as funções min, max, sum e avg são as principais funções de agregação
# funções de agregação -> agregam ou combinam dados de uma tabela em um único resultado
# sum -> todas as linhas e retornar um resultado, assim como as outras
'''SUM'''
# exemplo práito -> select top 10 sum (LineTotal) from Sales.SalesOrderDetail
# add 'apelidos' as colunas -> select top 10 sum (linetotal) as 'soma' from Sales.SalesOrderDetail

'''MIN'''
# exemplo prático -> select top 10 min(LineTotal) from Sales.SalesOrderDetail

'''MAX'''
# exemplo prático -> select top 10 max(LineTotal) from Sales.SalesOrderDetail

'''AVG'''
# exemplo prático -> select top 10 avg(LineTotal) from Sales.SalesOrderDetail

'''GROUP BY'''
# o group by divide o resultado da pesquisa em grupos
# exemplo... você pode aplicar uma função de agregação para grupos de pesquisa especificos
# - calcular a soma dos itens
# - contar o número de itens naquele grupo

# sintaxe
# select coluna1, funcaoAgregacao(coluna2) -> select em uma coluna, função de agre que será app em outra coluna
# from nomeTabela # -> tabela que trará a info
# group by coluna1; -> agrupar na coluna desejada.
# exemplo prático -> select SpecialOfferID, sum (unitprice) from Sales.SalesOrderDetail group by SpecialOfferID
# ex prático -> select ProductID, COUNT (ProductID) as 'contagem' from Sales.SalesOrderDetail group by ProductID
# (agrupou os IDs do produto e conta quantas vezes esse id aparece no banco de dados)
# https://paste.pics/6c9c5b7c99ce9b46ba9071913870f895
# ex prático -> select FirstName, COUNT(FirstName) as 'repeticao de nome' from Person.Person group by FirstName
'''
selecionar a coluna que será retornada, a operação que deseja realizar e no final o agrupamento

select color, AVG (ListPrice) as 'preço médio'
from Production.Product
group by Color
'''

'''HAVING'''
# o having é utilizado junto com o group by para filtrar resultados que já estão agrupados.
# é um tipo de 'where para dados agrupados'
# sintaxe
'''
select coluna1, funcaoAgregacao(coluna2)
from tabela
group by coluna 1
having condicao
'''

# a grande diferença entre having e where
# o group by é app depois que os dados já foram agrupados, enquanto o where é app antes dos dados serem agrupados
'''
exemplo prático

select ProductID, sum(LineTotal) as 'total de vendas por produto'
from Sales.SalesOrderDetail
group by ProductID
having sum(LineTotal) between 162000 and 500000
'''

'''AS'''
# o AS serve para "apelidar" colunas, buscas e etc. É uma ferramenta bem flexivel no SQL
'''
Exemplos Práticos
select top 10 ListPrice as 'Lista de Preço'
from Production.Product

select top 10 avg(listprice) as 'média de preço'
from Production.Product
'''


'''INNER JOIN'''
# o comando JOIN é dos mais usados quando se está trabalhando com querys e precisamos juntar infos de outras tabelas
# até o momento trabalhamos com operações relacionadas a uma única tabela, o join vai nos ajudar a expandir esse
# horizonte de operações com outras tabelas
# existem 3 tipos gerais de joins: inner join, outer join e self join
# cenário de aplicação
'''
imagine que você tenha duas tabelas: cliente (com as infos de clienteid, nome e enderecoid) 
e a tabela Endereco (com as infos de enderecoid, rua e cidade) e precisa trazer infos da tabela endereco para a tabela
cliente

conceitos de chave primária e chave estrangeira
'''

# exemplo prático
'''
select c.clienteid, c.nome, e.rua, e.cidade
from cliente c
inner join endereco e on e.endeecoid = c.enderecoid
'''

# exemplo prático
'''
-- inner join
select p.BusinessEntityID, p.FirstName, p.LastName, pe.EmailAddress
from Person.Person as p
inner join Person.EmailAddress as pe on p.BusinessEntityID = pe.BusinessEntityID
'''

# exemplo prático
'''
select p.Name, p.ProductSubcategoryID,  p.ListPrice
from Production.Product as p
inner join Production.ProductSubcategory as sb on p.ProductSubcategoryID = sb.ProductSubcategoryID
'''

# produto cartesiano -> junção de todas as infos
# exemplo prático
'''
select *
from Person.BusinessEntityAddress as ba
inner join Person.Address as pa on pa.AddressID = ba.AddressID
'''
