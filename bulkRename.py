#change filenames 
import os

path = raw_input('Enter path: ')
tempate_name=raw_input('Enter the name you want in the bulk rename: ')
template_extension = raw_input('Enter the extension: ')

j=0
os.chdir(path)
for i in os.listdir(path):
	os.rename(i,template_name+ str(j)+template_extension')
	j+=1
