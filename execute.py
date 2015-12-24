# coding=UTF-8	

import sys

if sys.argv[1] == 'item_db':
	exec(open('automata/automata.py').read())
elif sys.argv[1] == 'mob_db':
	exec(open('automata/automata.py').read())