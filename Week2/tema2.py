
####### FIRST ############################
def your_function(*args, **kwargs):
    sum = 0
    for x in args:
        if type(x) == int or type(x) == float:
            sum += x
    return sum


print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(your_function())
print(your_function(2, 4, 'abc', param_1 = 2))


####### SECOND ###########################
def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

def recursive_odd(n):
    if n <= 0:
        return 0
    elif n % 2 == 0:
        return recursive_odd(n - 1)
    else:
        return n + recursive_odd(n - 2)

def recursive_even(n):
    if n <= 0:
        return 0
    elif n % 2 == 1:
        return recursive_even(n - 1)
    else:
        return n + recursive_even(n - 2)

print(recursive_sum(5))
print(recursive_odd(7))
print(recursive_odd(8))
print(recursive_even(7))
print(recursive_even(8))


####### THIRD ######################
def get_value(x):
    if type(x) == int:
        return x
    return 0

print(get_value(5))
print(get_value('5'))
print(get_value('a'))
