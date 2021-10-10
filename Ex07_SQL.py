# Desafio 1
# quantas pessoas tem o mesmo MiddleName agrupado por MiddleName
# resolução -> select MiddleName, COUNT(MiddleName) as 'reps' from Person.Person group by MiddleName
# https://paste.pics/d6dcfc0fb7eb9c472283291f00928eb0

'''
Dicas - Desafio 1
- as infos estão na tabela person.person
- usar group by e uma função de agregação
'''


# Desafio 2
# precisamos saber em média, qual é a quantidade (quantity) que cada produto é vendido na loja
# select ProductID, avg(OrderQty) as 'média de quantidade vendida' from Sales.SalesOrderDetail group by ProductID
# https://paste.pics/5739211dc74ba281c84b0e4b2249761d


# Desafio 3
# Como saber quais foram as 10 vendas que no total tiveram os maiores valores de venda (line total) por produto
# do maior valor para o menor)
# resolução -> select top 10 Productid, SUM(linetotal) from Sales.SalesOrderDetail group by ProductID
# order by sum(LineTotal) desc;
# https://paste.pics/a1db00c2bcd3d43fdd2f63cc6aef31a8
'''
Dicas - Desafio 3
- usar a tabela sales.salesorderdetail
- usar group by e uma função de agregação
- se atentar a ordenação
'''


# Desafio 4
# quantos produtos e qual quantidade média de produtos temos cadastrados nas nossas ordem de serviços (workorder),
# agrupados por productID
# resolução -> select ProductID, COUNT(ProductID) as 'contagem', AVG(OrderQty) as 'media' from Production.
# WorkOrder group by ProductID
# https://paste.pics/b75699644840602ab307fb5af62dcb6c

'''
Dicas - Desafio 4
- usar a tabela production.workorder
- group by e uma unfunção de agregaçã
'''


'''
-- exemplo 1
select * from Sales.SalesOrderDetail

select SpecialOfferID, SUM(UnitPrice) as 'soma'
from Sales.SalesOrderDetail
group by SpecialOfferID


-- exemplo 2
select *
from Sales.SalesOrderDetail

select ProductID, COUNT(OrderQty) as 'vendidos'
from Sales.SalesOrderDetail
group by ProductID


-- exemplo 3
select *
from Person.Person

select FirstName, COUNT(FirstName) as 'contagem'
from Person.Person
group by FirstName


-- exemplo 4 
select *
from Production.Product

select Color, AVG(ListPrice) as 'preço médio'
from Production.Product
where color = 'silver'
group by Color

-- desafio 1 
select *
from Person.Person

select MiddleName, COUNT(MiddleName) as ' qts de pessoas com o mesmo sobrenome'
from Person.Person
group by MiddleName

-- desafio 2
select *
from Sales.SalesOrderDetail

select ProductID, AVG(OrderQty) as 'media de vendas'
from Sales.SalesOrderDetail
group by ProductID

-- desafio 3
select * 
from Sales.SalesOrderDetail

select top 10 ProductID, sum(LineTotal)
from Sales.SalesOrderDetail 
group by ProductID
order by sum(LineTotal) desc

-- desafio 4
select ProductID, AVG(StockedQty) as 'qtd estoque'
from Production.WorkOrder
group by ProductID
'''