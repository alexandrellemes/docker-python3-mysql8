#!/bin/bash

echo 'Excluir maquinas ... fase 1'
sudo docker ps -a | awk '{ print $14 }' | xargs sudo docker rm $0
echo 'Excluir maquinas ... fase 2'
sudo docker ps -a | awk '{ print $15 }' | xargs sudo docker rm $0

echo 'Monta os containers...'
sudo docker-compose up -d --build

#echo 'Atualiza a maquina virtual'
#sudo docker-compose exec php-apache apt update
#sudo docker-compose exec php-apache apt -y upgrade

echo 'Roda a aplicacao de exemplo - datasample.py'
sudo docker-compose exec python3 sh -c "python datasample.py"


