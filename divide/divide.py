import subprocess
import os

for i in range(13,15):
	p = subprocess.Popen(['pdf2txt.py', '-p',str(i),'carlo.pdf'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
#	print out
	if out != '':
		if out.find('The New York Times Company. All Rights Reserved.') != -1:
			print 'New page'
			# Open a file
			fo = open(str(i)+".txt", "wb")
			fo.write(out);

			# Close opend file
			fo.close()
		else:
			print 'Previos Page'

