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

'''TIPOS DE JOINS'''
# https://terminalroot.com.br/2019/10/inner-join-left-join-right-join-mysql.html
# quando estamos trabalhando com o join, temos que ter em mente a existência de dois lados; dir e esq
# quando estamos trabalhando com o join na estrutura, a primeira tabela (no from) é o lado ESQUERDO
# a tabela que será usada na estrutura do on é a tabela do lado direito (começamos da esquerda para a direita)

'''INNER JOIN'''
# retorna apenas os valores que existem em ambas as tabelas
# https://paste.pics/484a6a599fd14edce48ffff6f905c663

'''FULL OUTER JOIN'''
# é considerado o join mais completo, retorna o conjunto de todos os registros correspondentes e preenche os valores
# não correspondentes com null
# https://paste.pics/c718eba9ac5db34f6d1b7e4f72b8d368


'''LEFT E RIGHT OUTER JOIN'''
# tem um conceito parecido com o full outer join mas exclui as informações do lado B (ou lado direito da operação)
# retorna um conjunto de todos os registros da tabela A e os registros correndespontes das infos que estão na B tbm
# quando não existe um valor correspondente, preenche com null
# https://paste.pics/ade059144cdefd61711dc0f07913d381
# exemplo práticp
'''
-- Quais pessoas tem um cartão de crédito registrado? 
select *
from Person.Person

select * 
from sales.PersonCreditCard

select pp.BusinessEntityID, FirstName, pp.LastName, pc.CreditCardID
from Person.Person as pp
left join Sales.PersonCreditCard as pc on pp.BusinessEntityID = pc.BusinessEntityID

para saber quais pessoas não possuem um cartão de crédito
select pp.BusinessEntityID, FirstName, pp.LastName, pc.CreditCardID
from Person.Person as pp
left join Sales.PersonCreditCard as pc on pp.BusinessEntityID = pc.BusinessEntityID
where pc.CreditCardID is null

é importante usar o left join nesse cenário porque ele retorna como null os registros que não existem na outra tabela,
diferente do inner join que se retornar os registros correspondentes nas duas tabelas
usando inner join -> retorno de 19118 linhas
usando o left join -> retorno de 19972 linhas (porque trouxe os valores que não estão registrados na outra tabela)
'''

'''UNION'''
# o operador union combina dois ou mais resultados de um select em um único resultado
# além de juntar as informações de tabelas diferentes, o union remove informações duplicadas
# sintaxe
# também é possivel ordenar o retorno das informações dadas pelo union como um única resultado
'''
select tabela1, tabela2
from tabela1
union
select coluna1, coluna2
from tabela2
'''
# exemplo prático
'''
select ProductID, Name, ProductNumber
from Production.Product
where Name like '%Chain%'
union
select ProductID, Name, ProductNumber
from Production.Product
where name like '%Decal%'
order by Name
'''

# exemplo prático
'''
select FirstName, Title, MiddleName
from Person.Person
where Title = 'mr.'
union
select FirstName, Title, MiddleName
from Person.Person
where MiddleName = 'a'
'''

'''DATEPART'''
# a função datepart permite extrair diversas infos de uma coluna que tem o tipo data.
# link documentação -> https://docs.microsoft.com/pt-br/sql/t-sql/functions/datepart-transact-sql?view=sql-server-ver15
# exemplo prático
'''
select SalesOrderID, DATEPART(MONTH, OrderDate) as 'mês de venda'
from Sales.SalesOrderHeader

select coluna1, datepart(tipo de info, onde eu vou buscar essa info) as apelido
from tabela que contém a info
'''

'''MANIPULAÇÃO DE STRINGS'''
# doc-> https://docs.microsoft.com/pt-br/sql/t-sql/functions/string-functions-transact-sql?view=sql-server-ver15

# exemplo prático
# concatenação
'''
select CONCAT(FirstName, ' ', LastName)
from Person.Person
'''

# funções upper e lower
'''
select UPPER(FirstName), LOWER(LastName)
from Person.Person
'''

# contagem de caracteres
'''
select FirstName,LEN(FirstName)
from Person.Person
'''

# função substring (extrai informações de uma string)
'''
select FirstName,SUBSTRING(FirstName, 1, 3) as 'iniciais'
from Person.Person

substring(coluna onde buscar a string, indice inicio, inidice final)
'''

# Replace -> substitui um item na string
'''
select ProductNumber, REPLACE(ProductNumber, '-', '#') as 'usando replace'
from Production.Product

replace(coluna onde vai fazer a substituição, 'string que será subs', 'nova string')
'''

'''FUNÇÕES MATEMÁTICAS EM SQL'''
# Soma, subtração, divisão, multiplicação seguem a mesma lógica.
'''
select UnitPrice + LineTotal as 'ops soma'
from Sales.SalesOrderDetail
'''

# função round -> arredondamento de valores
'''
select LineTotal, ROUND(LineTotal,2) as 'round function'
from Sales.SalesOrderDetail

round(coluna onde os valores serão arrendodados, precisão / casas decimais)
'''

# função sqrt -. raiz quadrada
'''
select SQRT(LineTotal) as 'raiz quadrada'
from Sales.SalesOrderDetail
'''
