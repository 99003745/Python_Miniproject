"""
This code take the user input up to five input  as a keyword
search the particular keyword in given text file
create a new text file with same name as a keyword
and have count in it.
Author: Ujjawal Kumar
Contact: ujjawal.kumar@ltts.com
PS No.: 99003745
Date of creation: 23/02/2021
"""
import re


class Pythonminiproject:

    def __init__(self):
        print("##########$$_WELCOME TO WORD FINDER_$$##########")
        # print the Heading for our console
        self.count = 0
        self.input_file = open("input.txt", "r")
        # opening the given file
        self.read_file = self.input_file.read()
        # reading the given file

    def taking_input(self):
        taking_no_int = int(input("ENTER THE NUMBER OF WORDS YOU WANT TO SEARCH: "))
        # taking the total number of input by the user
        if taking_no_int > 5:
            # this loop will run if user input is more than five input
            print("Give up TO Five input")
            print("Re Run The Project")

        else:

            for y in range(taking_no_int):

                find_word = input("Enter The Keyword: ")
                # taking the keyword we want to search
                x = re.findall(find_word,  self.read_file, re.M | re.I)
                # finding the word in the opened text file

                input_file1 = self.read_file.split()
                # splitting the text file

                file_save = find_word+'.txt'
                # creating the text file in the name of searched keyword
                write_file = open(file_save, 'w+')
                # opening the created file for saving the keyword
                write_file.write('No. of time ' + find_word + ' repeated:' + str(len(x))+'\n')
                # adding line in the file  for count
                print("A NEW TEXT FILE " + find_word + " IS CREATING....")
                # printing instruction

                for i in range(len(input_file1)):
                    word = re.match(find_word, input_file1[i], re.M | re.I)
                    # for matching word in the file

                    if word:
                        self.count += 1

                        str1 = (input_file1[i-1]+' ' + input_file1[i] + ' '+input_file1[i+1])
                        # printing command for one word before and after
                        # write_file.write(str(self.count) + ' :')
                        write_file.writelines(str(str1) + '\n')
                        # appending the search word in created file


obj = Pythonminiproject()

obj.taking_input()

print("PROJECT ENDS")
