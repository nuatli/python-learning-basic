import time

def func_one(n):
	return [str(num) for num in range(n)]
	
print(func_one(10))

def func_two(n):
	return list(map(str,range(n)))
	
print(func_two(10))


## 2 daha kısa sürede bitti 1.000.000 tanesi için

#CURRENT TIME BEFORE
start_time = time.time()
#RUN CODE
result = func_two(1000000)
#CURRENT TIME AFTER RUNNING CODE
end_time = time.time()
#ELAPSED TIME
elapsed_time = end_time - start_time

print(elapsed_time)


import timeit


stmnt = '''
    func_one(100)
'''

setup = '''
    def func_one(n):
        return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmnt,setup,number=1000000))