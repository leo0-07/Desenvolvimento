# sqlite2mysql.

script pata exportação sqlite/mysql.

sqlite2mysql.py

Este é um exemplo de usagem do script de conversão....

1. sqlite.

criando dump dos dados/tabela(s)
sqlite3 sample.db .dump | python sqlite2mysql.py > dump.sql

2. mysql.
importando tabelas/dados exportados.
mysql -h "host" -D "database" -u "user" -p < dump.sql
mysql -h db.local.net -D local -u asl -p dump.sql

