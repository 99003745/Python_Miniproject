import re

count = 0


input_file = open("input.txt", "r")

read_file = input_file.read()


Taking_No_int = int(input("ENTER THE No. OF WORDS YOU WANT TO SEARCH: "))

for y in range(Taking_No_int):
    find_word = input("Enter The Keywods: ")
    x = re.findall(find_word,  read_file, re.M | re.I)

    input_file1 = read_file.split()

    file_save = find_word+'.txt'
    write_file = open(file_save, 'w+')
    write_file.write('No. of time ' + find_word + ' repeated:' + str(len(x))+'\n')

    for i in range(len(input_file1)):
        word = re.match(find_word, input_file1[i], re.M | re.I)
        if word:
             count += 1

             str1 = (input_file1[i-1]+' ' + input_file1[i] + ' '+input_file1[i+1])
             write_file.write(str(count) + ' :')
             write_file.write(str(str1) + '\n')
             #print("A NEW TEXT FILE " + find_word + " IS CREATED")
close_file = input_file.close()
