# coding=UTF-8	

# ###################
# Descrição:
#		Arquivo para exportar o banco de dados
#
# Autor: Rodrigo Azevedo
# ###################

class database:
	#db = []
	db = {}
	non_db = ""

	def set(self, id, name):
		#self.db.append([id, name])
		self.db[id] = name

	def export(self, start, end):
		for i in range(start, end):
			name = self.get(i, '')
			if(name != ''):
				print 'database.set('+str(i)+', \''+name.replace('\'', '\\\'')+'\')'

	def get(self, id, undefined_name):
		#for element in self.db:
		#	if element[0] == id:
		#		return element[1]
		#return undefined_name
		try:
			return self.db[id]
		except:
			return undefined_name

database = database()

# insira novos dados aqui

exec(open('db/item_db.py').read())

database.export(1,1000000)
