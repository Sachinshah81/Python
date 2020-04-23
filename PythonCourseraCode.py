
## Installing packages in python using PIP
# The following command will install the latest version of a module and its dependencies from the Python Packaging Index:
#Cmd>  python -m pip install <package name>

# python -m pip install --upgrade <package name>


#String
#str1 = 'hello'
#str2 = 'world'

#print (str1+str2)

#Working with files
#FileHandle = open("filename", "optional: mode=r,w")

#Counting the number of lines in a file
#MyFilehandle = open('mailbox.txt', 'r')
# count = 0
# for line in MyFilehandle:
	# count  = count + 1
# print("Number of lines in file: mailbox.txt = ", count)
#output = Number of lines in file: mailbox.txt =  1909

#Count the number of new-line characters in the file
# MyFilehandle = open('mailbox.txt', 'r')
# FileContent = MyFilehandle.read()  #Gives the content of entire file in a single sequence of characters
# count = FileContent.count ('\n')
# print("\nNumber of new-line char in file: mailbox.txt = ", count)
# print(FileContent)


#Searching through a file. Print a line that contains certain word(s)
# count=0
# for line in MyFilehandle:
	# if line.startswith('From'):
		# count= count + 1
		# print(line.rstrip())
# print(count)



# Fname = input("Enter the File Name:")

# try:
	# MyFilehandle = open(Fname, 'r')
# except:
	# print("The file name:",Fname, " couldnot be opened. Quitting program execution")
	# quit()
	
# count=0
# for line in MyFilehandle:
	# #if line.startswith('Subject:'):
	# if '@umich.edu' in line:
		# count= count + 1
		# print(line.rstrip())
# #print("There were - ", count, " Subject: lines in ", Fname)
# print("There were - ", count, " \"@umich.edu\" in", Fname)


#Read a file from the console input and print all the contents in UPPER case as it is.

# Fname = input("Enter the File Name:")
# FileHandle = open(Fname)
# FileContent = FileHandle.read()

# print(FileContent.upper().rstrip())




#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.


#Fname = input("Enter the file-name:")
#FileHandle = open(Fname, 'r')

# FileHandle = open ('mbox-short.txt', 'r')

# count = 0
# FloatingNumber = 0 
# for line in FileHandle:
	# if 'X-DSPAM-Confidence:' in line:
		# count = count + 1
		# StartPos = line.find("X-DSPAM-Confidence:")
		# ExtractedString = line[StartPos+20:StartPos+26]
		# print (ExtractedString)
		
		# FloatingNumber = float(ExtractedString) + FloatingNumber
# print (FloatingNumber)		
# print("Count of matching string====", count)

# AverageNumber = FloatingNumber/count
# print ("Average spam confidence:", AverageNumber)




# List
# Dictionary
# Tuples

#MyList = ['banana', 'apple', ['111', '22', '33333'], 'lemon']
#print (len(MyList[2][0]))

# range function returns a list of integers [0, 1, 2, 3 ....upto size specified]
#print(range(4)) # prints output: range(0, 4)

#Fruits = ['mango', 'orange', 'apple', 'banana']

# for i in range(len(Fruits)):
	# print("I like to eat:", Fruits[i])
	
#Prints 
#I like to eat: apple
#I like to eat: banana
#I like to eat: mango
#I like to eat: orange

# Lists can be concatenated and sliced like a string.
#Fruits.sort()
#print(Fruits)

#### Assignment:
#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words


# FileName = input("Enter the file name:")
# FileHandle = open(FileName)

# MyNewList = list()
# MyTempList = list()

# for line in FileHandle:
	# MyTempList = line.rstrip().split()
	# for element in MyTempList:
		# if element not in MyNewList:
			# MyNewList.append(element)
# MyNewList.sort()
# print(MyNewList)


#### Assignment
#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt


# FileName = input("Enter the file name:")
# FileHandle = open(FileName)

# MyList = list()
# count = 0
# for line in FileHandle:
	# line = line.rstrip()
	# if line.startswith('From'):
		# MyList = line.split()
		# if MyList[0] == 'From':	#Making sure the line starts with exactly 'From' and NOT 'From:' or 'From::' etc.
			# count = count + 1
			# print(MyList[1])
# print("There were ", count, " lines in the file with From as the first word")
#output count=27

############################
##### Dictionaries

# MyDictionary = dict()
# MyDictionary = {'Rambo':2, 'Terminator':1, 'Godfather':4}
# MyDictionary['Rambo'] = 0
# print("Godfather value=", MyDictionary['Godfather'])
# print(MyDictionary)

# for movie in MyDictionary:
	# print(movie, MyDictionary[movie])

######## Build a dictionary of most repeated names.

# names = list()
# names = ['pratt', 'jolie', 'cruz', 'pitt', 'pratt', 'khan', 'jolie', 'pitt', 'pitt']
# MyDict = dict()
# for name in names:
	# # Dictionary.get(key, 0) ====> returns the value held by the key in the Dictionary. if key doesn't exist, default=0 is returned. below Statement increments the existing value/count by 1 for the matching key=name.
	# MyDict[name] = MyDict.get(name, 0) + 1 
	
	# #### OR below code works 
	
	# # if name in MyDict:
		# # MyDict[name] = MyDict[name] + 1
	# # else:
		# # MyDict[name] = 1
# print(MyDict)

################### Retrieving list of keys, values or both from a dictionary
# MyDictionary = {'year': 2020, 'color': 'red', 'car': 'BMW', 'Model': 8989}
# ListOfKeys = MyDictionary.keys()
# ListOfValues = MyDictionary.values()
# ListOfKeyValuePair = MyDictionary.items()

# print(ListOfKeys)
# print(ListOfValues)
# print(ListOfKeyValuePair)

########## 2-iteration variables : we can iterate key, value in the list of items retrived from a dictionary

# for mykey in MyDictionary:
	# print("Key =====", mykey)
	#print("Value = ", MyDictionary[mykey])
	
	
	
########## Assignment :
############### Find the word repeated the most in a given file	

# FileHandle = open("temp.txt")

# MyDictionary = dict()
# for line in FileHandle:
	# wordlist = line.split()
	# for word in wordlist:
		# MyDictionary[word] = MyDictionary.get(word,0) + 1 # This builds the dictionary() with key-value as word-count
		
# BigWord = None
# BigCount = 0

# for word, count in MyDictionary.items():
	# print(word, count)
	# if count>BigCount: # Get the highest count over a loop for all values/count from the dictionary/histogram
		# BigWord = word
		# BigCount = count
		
# print("Max repeated word and count=", BigWord, BigCount)


##### Revision:
# # # What is a collection?
# # # List vs. dictionaries
# # # Dictionary contants
# # # The most common word
# # # Using the get() method
# # # Hashing and lack of order
# # # Writing dictionary loops
# # # Sneek peek: tuples
# # # Sorting dictionaries



###### Assignment:
# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.



# FileHandle = open("mbox-short.txt")
# EmailDict = dict()

# MyList = list()
# count = 0
# for line in FileHandle:
	# line = line.rstrip()
	# if line.startswith('From'):
		# MyList = line.split()
		# if MyList[0] == 'From':	#Making sure the line starts with exactly 'From' and NOT 'From:'
			# #Below builds the dictionary() with key:value as Email:count
			# EmailDict[MyList[1]] = EmailDict.get(MyList[1], 0) + 1
		
# HighestRepeatedEmailID = None
# MaxCount = 0

# for email, count in EmailDict.items():
	# if count>MaxCount: # Get the highest count over a loop for all values/count from the dictionary/histogram
		# HighestRepeatedEmailID = email
		# MaxCount = count
		
# print(HighestRepeatedEmailID, MaxCount)




########################## Tuples
##################################################################

# # Tuples are similar to list(). It is immutable, meaning it's content cannot be changed.
# # Tuples can be compared to each other.

# tup1 = (0, 11, 22)
# tup2 = (5, 6, 99)

# if tup1 < tup2: print ("TRUE: tup1 < tup2") # Returns true since 0<5

# # 1) 1st item is compared and decision is made without moving to the next item in the tuple for comparison.
# # 2) If 1st item in a tuple are same, it moves over to the next item for comparison
# # 3) In a string comparison, alphabetical order is followed.

# tup3 = ("Janet", "Arnold")
# tup4 = ("Janet", "Zolly")

# if tup3 < tup4: print ("TRUE: tup3 < tup4") # Returns true since Z is greater than A.

############ Sorting of tuples by keys using sorted() - function
# di = {'Z': 33, 'A':99, 'J':11}
# print(di.items())
# print(sorted(di.items()))

############ Sorting of tuples by values; Build a reverse list of value-key and use sort() function on it.
# templist = list ()

# for k,v in di.items():
	# templist.append((v,k)) # For every key-value from dictionary, build a list of value-key items.

# print("Reversed value-key list", templist)

# templist = sorted(templist, reverse=True) # set reverse=True for Descending order
# print("sorted list with descending order of values", templist)



##################### Assignment 
###########   Find the top 5 most repeadted words from a file


# FileHandle = open("mbox-short.txt")
# EmailDict = dict()

# MyList = list()
# count = 0
# for line in FileHandle:
	# line = line.rstrip()
	# if line.startswith('From'):
		# MyList = line.split()
		# if MyList[0] == 'From':	#Making sure the line starts with exactly 'From' and NOT 'From:'
			# #Below builds the dictionary() with key,value as Email,count
			# EmailDict[MyList[1]] = EmailDict.get(MyList[1], 0) + 1
		
# HighestRepeatedEmailID = None
# MaxCount = 0

# tempList = list()
# FinalList = list()
# for email, count in EmailDict.items():
	# #print("Email, Count:", email, count)
	# tempList.append((count, email)) # reversing the key-value and building a new list for further sorting
	
# tempList = sorted(tempList, reverse=True) # Sorting in Descending order of count
# #print(tempList)
# for k,v in tempList:
	# FinalList.append((v,k)) # Building the original email-count list back for final printing.
# print("Top 5 emails and their count:", FinalList[0:5])

########## List comprehension ===== creates a dynamic list. In this case we make a list of reversed tuples and then sort it.
di = {'Z': 33, 'A':99, 'J':11}
print(sorted([(v,k) for (k,v) in di.items()], reverse=True))
# Gives output as a reverse sorted list of tuples: [(99, 'A'), (33, 'Z'), (11, 'J')]

#### Tuples - summary
# Tuple Syntax
# Immutability
# Comparability
# Sorting
# Tuples in Assignment statement
# Sorting dictionaries in either key or value



#################### Assignment
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# Expected output:
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1


# FileHandle = open("mbox-short.txt")
# HourDict = dict()
# MyList = list()
# MyFinalList = list()

# for line in FileHandle:
	# line = line.rstrip()
	# if line.startswith('From'):
		# MyList = line.split()
		# if MyList[0] == 'From':	#Making sure the line starts with exactly 'From' and NOT 'From:'
			# #Extract the HH(hour) from the 6th element.
			# TimeStamp = MyList[5].split(':')
			# #Below builds the dictionary() with key:value as Hour:count
			# HourDict[TimeStamp[0]] = HourDict.get(TimeStamp[0], 0) + 1

# MyFinalList = sorted(HourDict.items(), reverse=False)

# for k,v in MyFinalList:
	# print(k, v)
	
	
################################ 
# Remove duplicate chars in a given string:
# str = "constantinople"
# MyTempList = list()
# for i in str:
	# MyTempList.append(i)

# MyFinalList = list()
# for letter in MyTempList:
	# if letter in MyFinalList:
		# continue
	# else:
		# MyFinalList.append(letter)

# print(MyFinalList)





















 
 
 
 
 
 
 







