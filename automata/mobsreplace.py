# coding=UTF-8	

# ###################
# Descrição:
#		Script desenvolvido para traduzir os arquivos relacionados aos mobs do Cronus
#
# Autor: Rodrigo Azevedo
# ###################

name_db = sys.argv[1]

class database:
	#db = []
	db = {}
	non_db = ""

	def set(self, id, name):
		#self.db.append([id, name])
		self.db[id] = name

	def get(self, id, undefined_name):
		#for element in self.db:
		#	if element[0] == id:
		#		return element[1]
		#return undefined_name
		try:
			return self.db[id]
		except:
			self.non_db = self.non_db + 'database.set('+str(id)+', \''+undefined_name.replace('\'', '\\\'')+'\')\n'
			log(1, 'id '+str(id)+' não possui nome associado no db')
			return '#Error#'

log_text = ""
def log(type, text):
	global log_text

	if type == 0:
		color = ''
		status = '[Checando]'
	elif type == 1:
		color = '\033[93m'
		status = '[Atenção]'
	elif type == 2:
		color = '\033[92m'
		status = '[Ok]'
	log_text = log_text + status +' ' + text + '\n'
	print color + status + '\033[0m '+text

f = open(name_db, 'r+')
str_text = f.read()

database = database()
exec(open('db/mob_db.py').read())

total_mobs = 0;
mobs_translated = 0;

pos = 0
lines = str_text.split('\n')
for elm in lines:
	pos += 1
	arg = elm.split(',')
	if arg[0].isdigit():
		total_mobs += 1
		log(0, "id " + str(arg[0]) + " (" + str(round(pos / float(len(lines)) * 100, 2)) + "% concluido)")
		new_name = database.get(int(arg[0]), arg[1])
		if new_name != '#Error#':
			str_text = str_text.replace(','+arg[1]+',', ','+new_name+',')
			mobs_translated += 1

log(2, "(100% concluido) "+name_db+".conf traduzido.")

if total_mobs / mobs_translated == 1:
	st = 2
else:
	st = 1
log(st, str(mobs_translated) +' de '+str(total_mobs)+' traduzidos ('+str(round(mobs_translated / float(total_mobs) * 100, 2))+' % da tradução feita)')

s = open('new_'+name_db, 'w')
s.write(str_text)

s = open('log/'+name_db, 'w')
s.write(log_text)

s = open('non_db/'+name_db+'.py', 'w')
s.write(database.non_db)