import subprocess
import os
from sent import *
split_pages = 1
hashDelimiter = "\n#################################################\n"
fo = open('split_pages.txt', 'wb')
fo.close()
for i in range(1,200):
	p = subprocess.Popen(['pdf2txt.py', '-p',str(i),'carlo.pdf'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
#	print out
	if out != '':
		if out.find('The New York Times Company. All Rights Reserved.') != -1:
			print 'New page',i
			
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

file_writer = open('result.csv', 'wb')
file_writer.close()
fileReader = open('split_pages.txt')
full_paper = fileReader.read()

split_paper = full_paper.split('\n#################################################\n')
for i in range(1,len(split_paper)):
	print split_paper[i].split('The New York Times\n')[0].split('\n')[-5:-1]
	titCountList = getArticleCount(split_paper[i].split('The New York Times\n')[0].split('\n')[-5:-1][0])
	artCountList = getArticleCount(split_paper[i].split('The New York Times Company. All Rights Reserved.')[1])
	forWriteToFile = split_paper[i].split('The New York Times\n')[0].split('\n')[-5:-1]
	with open('result.csv', 'a') as result_file:
		file_writer = csv.writer(result_file)
		#for i in range(item_length):
		file_writer.writerow([x for x in forWriteToFile])
		file_writer.writerow([x for x in titCountList])
		file_writer.writerow([x for x in artCountList])

		
		
	
