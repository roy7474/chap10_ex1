'''
Exercise 1: Revise a previous program as follows: 
Read and parse the "From " lines and pull out the addresses from the line. 
Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits by 
creating a list of (count, email) tuples from the dictionary. 
Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
'''

#open program directly for easier testing
fhand = open('mbox-short.txt')
emails = {}
''''
fhand = input('Enter the name of the file that you would like to open. Please include the file format(eg.: file_name.format): ')
try:
    open(fhand)
except FileNotFoundError:
    print('There was a problem while trying to open your file. Please try again')
    exit()
'''
#read_fhand = fhand.read() #read file
# Read and parse the "From " lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary.
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[1] not in emails:
            emails[words[1]] = 1
            
        else:
            emails[words[1]] += 1



# After all the data has been read, print the person with the most commits by 
# creating a list of (count, email) tuples from the dictionary. 

max_key_value = max(emails, key = emails.get)
max_value = emails[max_key_value]
print(max_value, 'by', max_key_value)


