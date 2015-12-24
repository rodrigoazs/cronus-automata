# Cronus Automata
Script desenvolvido em Python para tradução automática do banco de dados do Cronus.

As traduções atuais foram obtidas através do idnum2itemdisplaynametable.txt disponibilizado pelo bRO para os itens e do banco de dados do antigo Cronus para os mobs.

### Como usar
Deposite o arquivo desejado para a tradução na mesma pasta onde consta o arquivo _execute.py_. Os arquivos que possuem capacidade de serem traduzidos atualmente são:

* item_db.conf
* mob_db.conf
* mob_branch.txt
* mob_poring.txt
* mob_boss.txt
* pet_db.txt

Após o depósito do arquivo, inicialize o script através de um console digitando o seguinte comando:

`python execute.py item_db.conf`

O programa se responsibilizará da tradução do arquivo junto com o histórico das informações projetadas no console (na pasta log/) e do itens ou mobs que não foram traduzidos (estes serão criados na pasta non_db/).
