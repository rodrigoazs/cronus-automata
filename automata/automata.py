# coding=UTF-8	

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
			return undefined_name


class automata:
	i = 0
	state = 0
	comment_state = 0
	id = ""
	name = ""
	name_pos = 0
	number_id = 0

	tokens = [
			'//',
			'/*',
			'Id',
			'Name',
			'AegisName',
			'\n',
			'*/',
			':',
			'"',
			'SpriteName']

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

def replace_str(old_str, start, end, new_word):
	return old_str[0 : start] + new_word + old_str[end : len(old_str)]

def change():
	global str_text
	global database
	global automata

	new_word = database.get(int(automata.id), automata.name)

	str_text = replace_str(str_text, automata.name_pos, automata.name_pos+len(automata.name), new_word)
	automata.i = automata.i + len(new_word) - len(automata.id)

f = open(name_db+'.conf', 'r+')
str_text = f.read()

automata = automata()
database = database()
exec(open('db/'+name_db+'.py').read())

while(automata.i < len(str_text)):
	if automata.state == 0:

		if str_text[automata.i : automata.i + 2] == automata.tokens[0]:
			automata.comment_state = 0
			automata.state = 1
			automata.i = automata.i + 1
		elif str_text[automata.i : automata.i + 2] == automata.tokens[1]:
			automata.comment_state = 0
			automata.state = 2
			automata.i = automata.i + 1
		elif str_text[automata.i : automata.i + 2] == automata.tokens[2]:
			automata.state = 3
			automata.i = automata.i + 1
		elif (str_text[automata.i : automata.i + 4] == automata.tokens[3] and str_text[automata.i-5 : automata.i + 4] != automata.tokens[4] and str_text[automata.i-6 : automata.i + 4] != automata.tokens[9]):
			automata.state = 6
			automata.i = automata.i + 3

	elif automata.state == 1:

		if str_text[automata.i] == automata.tokens[5]:
			automata.state = automata.comment_state

	elif automata.state == 2:

		if str_text[automata.i : automata.i + 2] == automata.tokens[6]:
			automata.state = automata.comment_state
			automata.i = automata.i + 1

	elif automata.state == 3:

		if str_text[automata.i : automata.i + 1] == automata.tokens[7]:
			automata.state = 4
			automata.id = ""
			automata.number_id = automata.number_id + 1
		elif str_text[automata.i : automata.i + 2] == automata.tokens[0]:
			automata.comment_state = 3
			automata.state = 1
			automata.i = automata.i + 1
		elif str_text[automata.i : automata.i + 2] == automata.tokens[1]:
			automata.comment_state = 3
			automata.state = 2
			automata.i = automata.i + 1

	elif automata.state == 4:

		if str_text[automata.i].isdigit():
			automata.name_pos = automata.i
			automata.id = automata.id + str(str_text[automata.i])
			automata.state = 5
		elif str_text[automata.i :automata.i + 2] == automata.tokens[0]:
			automata.comment_state = 4
			automata.state = 1
			automata.i = automata.i + 1
		elif str_text[automata.i : automata.i + 2] == automata.tokens[1]:
			automata.comment_state = 4
			automata.state = 2
			automata.i = automata.i + 1

	elif automata.state == 5:

		if str_text[automata.i].isdigit():
			automata.id = automata.id + str(str_text[automata.i])
		else:
			automata.state = 0

	elif automata.state == 6:

		if str_text[automata.i : automata.i + 1] == automata.tokens[7]:
			automata.state = 7
			automata.name = ""

	elif automata.state == 7:

		if str_text[automata.i : automata.i + 1] == automata.tokens[8]:
			automata.name_pos = automata.i + 1
			automata.state = 8

	elif automata.state == 8:

		if str_text[automata.i : automata.i + 1] != automata.tokens[8]:
			automata.name = automata.name + str(str_text[automata.i])
		else:
			automata.state = 0
			log(0, "id " + str(automata.id) + " (" + str(round(int(automata.i) / float(len(str_text)) * 100, 2)) + "% concluido)")
			change()

	automata.i = automata.i + 1

log(2, "(100% concluido) "+name_db+".conf traduzido.")

if len(database.db) / automata.number_id == 1:
	st = 2
else:
	st = 1
log(st, str(len(database.db)) +' de '+str(automata.number_id)+' traduzidos ('+str(round(len(database.db) / float(automata.number_id) * 100, 2))+' % da tradução feita)')

s = open('new_'+name_db+'.conf', 'w')
s.write(str_text)

s = open('log/'+name_db+'.txt', 'w')
s.write(log_text)

s = open('non_db/'+name_db+'.py', 'w')
s.write(database.non_db)