from collections import Counter
from collections import defaultdict
from collections import namedtuple
mylist = [1,1,1,1,1,2,2,2,2,3,3,3]
sentence = "Nazım Utku ATLI"
print(Counter(mylist))

print(Counter(sentence.split()))
print(Counter(list(sentence.lower())))


#### icerde cagrilan deger yoksa hata atar ama defaultdict'te icerde verilen default degeri doner

d = defaultdict(lambda:0)

d['correct']=100
print(d['correct'])
print(d['WRONG'])



Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age=5,breed='Husky',name='Sam')
print(type(sammy))
print(sammy)
print(sammy.age)
print(sammy[0])

