# Desafio 1
# criar um join que retore as seguintes infos: businessentityid, name, phonenumbertypeid, phonenumber
# tabela -> person.phonenumbertype
# tabela -> person.personphone
# resolução
'''
select *
from person.PhoneNumberType

select *
from Person.PersonPhone

select pp.BusinessEntityID, pt.Name, pt.PhoneNumberTypeID, pp.PhoneNumber
from Person.PhoneNumberType as pt
inner join Person.PersonPhone as pp on pt.PhoneNumberTypeID = pp.PhoneNumberTypeID
'''
# https://paste.pics/148da82f3f262ae889aba98b2a94618b


# Desafio 2
# criar um join que retore as seguintes infos: adressid, city, stateprovinceid, nome do estado
# tabelas -> person.stateprovince
# tabelas -> person.address
# resolução
'''
select *
from Person.StateProvince

select *
from Person.Address

select addres.AddressID, addres.City, addres.StateProvinceID, state.Name
from Person.Address as addres
inner join Person.StateProvince as state on addres.StateProvinceID = state.StateProvinceID
'''
# https://paste.pics/f794f732cd95ab816967d4fcf70d8c90

