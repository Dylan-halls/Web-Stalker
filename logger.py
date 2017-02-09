class Logger(object):

	def __init__(self):
		pass

	def info(self, text):
		with open('Stalker-RunTime.log', 'a') as file:
			file.write('G - '+text+'\n')

	def warn(self, text):
		with open('Stalker-RunTime.log', 'a') as file:
			file.write('Y - '+text+'\n')

	def error(self, text):
		with open('Stalker-RunTime.log', 'a') as file:
			file.write('R - '+text+'\n')

if __name__ == '__main__':
	log = Logger()
	log.info('This is some information')
	log.warn('This is a warning')
	log.error('This is a error')