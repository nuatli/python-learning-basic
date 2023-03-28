def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before original function \n')
        original_func()
        print('Some extra code, after original function \n')
        
    return wrap_func
    
'''    
def func_needs_decorator():
    print('I want to be decorated !! \n')

decorated_func = new_decorator(func_needs_decorator)
decorated_func()
'''

@new_decorator
def annotation_decorator():
    print("Hayda")
    
annotation_decorator()