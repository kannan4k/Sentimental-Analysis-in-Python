import subprocess
import os
from sent import *
 
def divide(fileName):
	split_pages = 1
	print fileName
	hashDelimiter = "\n#################################################\n"
	fo = open(fileName.split('.')[0]+'.txt', 'wb')
	fo.close()
	for i in range(1,500):
		p = subprocess.Popen(['pdf2txt.py', '-p',str(i),fileName], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		out, err = p.communicate()
	#	print out
		if out != '':
			if out.find('The New York Times Company. All Rights Reserved.') != -1:
				print 'Reading Page',i
				
				# Open a file
				with open(fileName.split('.')[0]+".txt", "a") as fo:
					fo.write(hashDelimiter)
					fo.write(out)
					split_pages = split_pages+1
					# Close opend file
					fo.close()
			else:
				print 'Reading Page',i
				split_pages =split_pages-1
				with open(fileName.split('.')[0]+'.txt', "a") as myfile:
					myfile.write(out)
	
	file_writer = open(fileName.split('.')[0]+'.csv', 'wb')
	file_writer.close()
	fileReader = open(fileName.split('.')[0]+'.txt')
	full_paper = fileReader.read()
	
	split_paper = full_paper.split('\n#################################################\n')
	for i in range(1,len(split_paper)):
		print 'Analyzing Page',i
		#print split_paper[i].split('The New York Times\n')[0].split('\n')[-5:-1]
		titCountList = getArticleCount(split_paper[i].split('The New York Times\n')[0].split('\n')[-5:-1][0])
		artCountList = getArticleCount(split_paper[i].split('The New York Times Company. All Rights Reserved.')[1])
		forWriteToFile = split_paper[i].split('The New York Times\n')[0].split('\n')[-5:-1]
		with open(fileName.split('.')[0]+'.csv', 'a') as result_file:
			file_writer = csv.writer(result_file)
			#for i in range(item_length):
			mergedList = forWriteToFile+titCountList+artCountList
			file_writer.writerow([x for x in mergedList])
	return 1




# Enter Your File names like the below format		
#divide('carlo.pdf')

divide('US_NTY_MOR_01.pdf')



