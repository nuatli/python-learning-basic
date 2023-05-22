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


'''
    110 Regular Expressions Part Two
'''
text = "My phone number is 506-428-8699"

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
###phone = re.search(r'\d{3}-\d{3}-\d{4}',text)

print(phone.group())
print("*********************************")


phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))
print("*********************************")

'''
    111 Regular Expressions Part Three
    Additional Regex Syntax
'''

result = re.search(r'cat|dog', 'The cat is here')
print(result)
print("*********************************")
result_1 = re.findall(r'at','The cat in the hat sat there.')
print(result_1)
print("*********************************")
result_2 = re.findall(r'.at','The cat in the hat sat there.')
print(result_2)
print("*********************************")
result_3 = re.findall(r'^\d','1 is a number ') ## Tüm textin basına bakıyor eger sayı varsa onu dönüyor
print(result_3)
print("*********************************")
phrase = "there are 3 numbers 34 inside 5 this sentence"
pattern = r'[^\d]'

result_4 = re.findall(pattern,phrase)
print(result_4)
print("*********************************")
pattern = r'[^\d]+'

result_5 = re.findall(pattern,phrase)
print(result_5)
print("*********************************")

test_phrase = 'This is a string! But it has puctuation. How can we remove it?'
pattern = r'[^!.?]+' ## ! . ve ? işaretlerini almadan ayır
result_6 = re.findall(pattern,test_phrase)
print(result_6)
print("*********************************")

pattern = r'[^!.? ]+' ## ! . ? ve boşluk işaretlerini almadan ayır
result_6 = re.findall(pattern,test_phrase)
print(result_6)
print("*********************************")

print(' '.join(result_6)) ## boşluk bırakarak yazmak
print("*********************************")


text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
pattern = r'[\w]+-[\w]+'  ## -> ['hypen-words','long-ish']
result_7 = re.findall(pattern,text)
print(result_7)
print("*********************************")
