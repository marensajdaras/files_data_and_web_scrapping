import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('^F.+:', x)
#  '\S+?@\S+'
print(re.findall('@\S+',x))
