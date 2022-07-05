#/usr/local/bin/bash
SRCHOST="192.168.100.81"
#
#
#
#
echo "Clonando Diretório do usuário:" $(whoami)

scp -r $SRCHOST:~/Documentos  ~/.
scp -r $SRCHOST:~/Cursos ~/.
scp -r $SRCHOST:~/Vídeos ~/.
scp -r $SRCHOST:~/Música ~/.
scp -r $SRCHOST:~/Imagens ~/.
scp -r $SRCHOST:~/Modelos ~/.

echo "Arquivos restaurados!" 
