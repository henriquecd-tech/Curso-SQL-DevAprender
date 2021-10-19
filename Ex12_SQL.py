# Desafio 1
# quero saber quais produtos na tabela order details tem o mesmo percentual de desconto
# resolução
# https://paste.pics/a368f297ca08c7f236599b5cb814a22d
'''
select a.ProductID, a.Discount
from [Order Details] as a, [Order Details] as b
where a.Discount = b.Discount
'''