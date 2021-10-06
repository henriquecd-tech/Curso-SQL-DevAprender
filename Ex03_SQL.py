# DESAFIO 1
# a equipe de produção precisa do nome de todas as peças que pesam mais de 500kg mas não mais de 700kg para inspeção
# -- weight (informação)
# resolução -> SELECT * FROM Production.Product WHERE Weight > 500 and Weight < 700;
# correção / alternativa -> SELECT Name FROM Production.Product WHERE Weight > 500 and Weight <= 700
# http://paste.pics/8227f66a83c6d738af2b4d463bd9b34b


# DESAFIO 2
# foi pedido pelo marketing uma relação de todos os colaboradores (employees) que são casados
# (single = solteiro, married = casados) e são assalariados
# resolução -> select * from HumanResources.Employee where MaritalStatus = 'm' and SalariedFlag = 'true';
# http://paste.pics/1f757ebe6e81c6d0ac98c81b2b0946ce

# DESAFIO 3
# um usuário chamado Peter Krebs está devendo um pagamento, consigo o e-mial dele para que possamos enviar uma cobrança
# tabela person.person e depois consultar a tabela person.emailaddress)
# resolução 1 -> select * from Person.Person where FirstName = 'peter' and LastName = 'krebs';
# print 1 -> http://paste.pics/3a375289a71e5fa477b72f93949159b3
# resolução 2 -> select * from Person.EmailAddress where BusinessEntityID = 26;
# print 2 -> http://paste.pics/e4294a7155533fcb7fa157a285b61d7c

