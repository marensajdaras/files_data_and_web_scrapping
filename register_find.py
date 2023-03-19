"""
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
the_dict = {}
for i in handle:
    if len(i.split()) > 2:
        if i.split()[0] == 'From':
            if i.split()[1] in the_dict:
                the_dict[i.split()[1]] += 1
            else:
                the_dict[i.split()[1]] = 1

a = max(the_dict, key = the_dict.get)
b = the_dict.get(a)

print(a, b)
  
