import re
import requests
file_url = 'http://py4e-data.dr-chuck.net/regex_sum_1759901.txt'
f = requests.get(file_url).text
f = f.split()
the_sum = 0

for i in f:
    if len(re.findall('[0-9]+',i)) > 0:
        the_sum += int(''.join(re.findall('[0-9]+',i)))
print(the_sum)
    
    
