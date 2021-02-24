import re

count=0


input_file=open("input.txt", "r")

read_file =input_file.read()

find_word=input("ENTER THE WORD YOU WANT TO SEARCH: ")

x=re.findall(find_word,  read_file, re.M|re.I)

input_file1=read_file.split()

file_save= find_word+'.txt'
write_file=open(file_save,'w+')

for i in range(len(input_file1)):
    word = re.match(find_word, input_file1[i], re.M | re.I)
    if word:
        count+=1
        str1=(input_file1[i-1]+' '+ input_file1[i]+ ' '+input_file1[i+1])
        write_file.write(str(str1) + '\n')
        write_file.write(str(count) + ' :')


write_file.write('No. of time word repeated:'+ str(len(x))+'\n')
#with open("input.txt") as openfile:
    #for line in openfile:
        #for part in line.split():

            #if find_word in part:
                #count += 1
                #
                #write_file.write(str(part)+'\n')

