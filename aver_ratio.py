"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output

"""
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s1 = 0
count = 0
for line in fh:
    
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    elif line.startswith("X-DSPAM-Confidence:"):
        a_l = len(line)
        a_0 = line.find('0')
        s1 += float(line[a_0:a_l])
        count += 1
        
        
print("Average spam confidence: "+str(s1/count))

