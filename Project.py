import re

input_file=open("input.txt", "r")
read_file =input_file.read()
find_word=input("ENTER THE WORD YOU WANT TO SEARCH: ")
x=re.findall(find_word,  read_file, re.M|re.I)

file_save= find_word+'.txt'
write_file=open(file_save,'w+')
write_file.write(str(x)+'\n')
write_file.write('No. of time word repeated:'+ str(len(x)))
