# Desafio 1
# encontre todos os endereços que estão no estado de Alberta, pode trazer todas as informações
# resolução
# https://paste.pics/8979d02088f5c0bae4f843e4e6630aeb
'''
select *
from Person.Address
where StateProvinceID in (select StateProvinceID from Person.StateProvince where Name = 'alberta')

resolução alternativa com inner join
select addres.AddressLine1, addres.StateProvinceID, state.Name
from Person.Address as addres
inner join Person.StateProvince as state on addres.StateProvinceID = state.StateProvinceID and state.Name = 'alberta'
'''