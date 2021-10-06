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
