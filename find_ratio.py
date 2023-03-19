text = "X-DSPAM-Confidence:    0.8475"
a = text.find('0')
b = text[a:a+6]
print(float(b))
