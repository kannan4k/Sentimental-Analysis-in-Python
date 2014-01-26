import subprocess
import os
split_pages = 1
hashDelimiter = "\n#################################################\n"
fo = open('split_pages.txt', 'wb')
fo.close()
for i in range(1,15):
	p = subprocess.Popen(['pdf2txt.py', '-p',str(i),'carlo.pdf'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
#	print out
	if out != '':
		if out.find('The New York Times Company. All Rights Reserved.') != -1:
			print 'New page'
			# Open a file
			with open("split_pages.txt", "a") as fo:
				fo.write(hashDelimiter)
				fo.write(out)
				split_pages = split_pages+1
				# Close opend file
				fo.close()
		else:
			print 'Previos Page'
			split_pages =split_pages-1
			with open('split_pages.txt', "a") as myfile:
				myfile.write(out)


