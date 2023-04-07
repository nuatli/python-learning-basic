##Regex

'''
Phone number
    (555)-555-5555
Regex pattern
    r"(\d\d\d)-\d\d\d-\d\d\d\d"
 
    r"(\d{3})-\d{3}-\d{4}"
 '''
 
text = "The agent's phone number is 408-555-1234. Call soon!"
boolean = 'phone' in text
print(boolean)



import re
pattern = 'phone'
print(re.search(pattern,text))

pattern = 'NOT IN TEXT'
print(re.search(pattern,text))


'''
    match.start()
    match.end()
'''

text = 'my phone once, my phone twice'

match = re.search('phone',text)

print(match)


matches = re.findall('phone',text)
print(matches)


for match in re.finditer('phone',text):
    print(match.span())
    print(match.group())