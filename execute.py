# coding=UTF-8	

# ###################
# Descrição:
#		Execute os autômatos e outros scripts necessários para a tradução dos
#		arquivos do banco de dados do Cronus.
#
# Autor: Rodrigo Azevedo
# ###################

import sys

if sys.argv[1] == 'item_db.conf':
	exec(open('automata/automata.py').read())
elif sys.argv[1] == 'mob_db.conf':
	exec(open('automata/automata.py').read())
elif sys.argv[1] == 'mob_poring.txt' or sys.argv[1] == 'mob_boss.txt' or sys.argv[1] == 'mob_branch.txt':
	exec(open('automata/mobsreplace.py').read())
else:
	print '\033[91m Não há a possibilidade de tradução deste arquivo. \033[0m'