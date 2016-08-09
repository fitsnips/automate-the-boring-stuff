#! python3

import traceback
try:
	raise Exception('This is a error message')
except:
	errorFile = open('errorInfo.txt','a')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info was written to errorInfo.txt')

