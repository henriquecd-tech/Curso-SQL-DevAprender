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
