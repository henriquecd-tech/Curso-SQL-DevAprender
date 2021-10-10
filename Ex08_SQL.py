# Desafio 01
# Estamos querendo identificar as proviciais (stateProvinceID) com o maior número de cadastros no nosso sistema, então
# é preciso encontrar quais provincias estão registradadas no banco de dados mais que 1000 vezes
# resolução ->
# select StateProvinceID, COUNT(StateProvinceID) as 'provincianos'
# from Person.Address
# group by StateProvinceID
# having COUNT(StateProvinceID) > 1000
# https://paste.pics/0329a26885e759c0e021664a785a5e6a


# Desafio 2
# os gerentes de uma multinacional querem saber quais produtos (productID) não estão trazendo no minimo 1 milhão em
# total de vendas (linetotal)
# resolução ->
# select ProductID, avg(LineTotal) as 'total de vendas'
# from Sales.SalesOrderDetail
# group by ProductID
# having avg(LineTotal) < 1000000
# https://paste.pics/a7f7da1e46711de6725981a8fbd89a11