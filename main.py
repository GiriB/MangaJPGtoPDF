from os import walk
import util

f = []
for (dirpath, dirnames, filenames) in walk('./images'):
	# if on MAC, rmeove .DS_Store file
	if '.DS_Store' in filenames:
		filenames.remove('.DS_Store')
  
	#We want the files to be sorted based on page number
	# name = shingeki_no_kyojin_72_18.jpg
	# split('_'), get the last part , then extract number
	filenames = sorted(filenames,key=lambda name:int(name.split('_')[::-1][0].split('.')[0]))


	file_list = []
	for i in filenames:
		file_list.append(dirpath+'/'+i)

	# print file_list
	print "Working For :",dirpath
	util.make_pdf(dirpath,file_list)

 



