import re

class  python_miniproject() :
    def __init__(self):
        print("WELCOME TO WORD FINDER")
        self.count = 0
        self.input_file = open("input.txt", "r")
        self.read_file = self.input_file.read()


    def taking_input(self):
        self.Taking_No_int = int(input("ENTER THE No. OF WORDS YOU WANT TO SEARCH: "))
        for y in range(self.Taking_No_int):
             find_word = input("Enter The Keyword: ")
             x = re.findall(find_word,  self.read_file, re.M | re.I)

             input_file1 = self.read_file.split()

             file_save = find_word+'.txt'
             write_file = open(file_save, 'w+')
             write_file.write('No. of time ' + find_word + ' repeated:' + str(len(x))+'\n')
             print("A NEW TEXT FILE " + find_word + " IS CREATING....")

             for i in range(len(input_file1)):
                word = re.match(find_word, input_file1[i], re.M | re.I)
                if word:
                    self.count += 1

                    str1 = (input_file1[i-1]+' ' + input_file1[i] + ' '+input_file1[i+1])
                    write_file.write(str(self.count) + ' :')
                    write_file.writelines(str(str1) + '\n')
                #close_file = self.input_file.close()

obj = python_miniproject()

obj.taking_input()
