#!/bin/bash
mysql --html -h asl-sl.com.br -D asldb -u waiter -p11224477 < select2.sql  > answer.txt
cat header.htmp answer.txt footer.htmp > old.html
scp old.html www.asl-sl.net:~/expert/public_html/.
