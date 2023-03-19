"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dict = {}
for i in handle:
    if len(i.split()) > 2:
        if i.split()[0] == 'From':
            time = i.split()[5]
            time = time[0:2]
            dict[time] = dict.get(time,0)+1
the_list = []
for y in dict.items():
    the_list.append(y)
the_list = sorted(the_list)
for z in the_list:
    print(z[0], end = ' ')
    print(z[1])
