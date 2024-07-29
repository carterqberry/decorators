# carter quesenberry cs 3270 lab 4 decorators

# define the tracking decorator:
def track(f):
    # create cache to store function results:
    cache = {}

    # create the wrapper function which adds caching:
    def wrapper(*args, **kwargs):
        # create a key for the function call based on the arguments:
        key = str(args) + str(kwargs)
        # if the function call with the same arguments is found in cache:
        if key in cache:
            # print that the result was found in cache
            print(f"{args}{kwargs} found in cache")
            # return the cache result
            return cache[key]
        else:
            # increase the function call count:
            wrapper.count += 1
            # call the original function:
            result = f(*args, **kwargs)
            # put the result in cache:
            cache[key] = result
            return result
    # create a variable to count the number of function calls:
    wrapper.count = 0
    return wrapper

# create the logging decorator:
def log(f):
    #create the wrapper functino which adds logging
    def wrapper(*args, **kwargs):
        # call the original function:
        result = f(*args, **kwargs)
        # write to log.txt file:
        with open('log.txt', 'a') as logfile:
            logfile.write(f"{f.__name__}{args} = {result}\n")
        return result
    return wrapper

# decorate the fib() function with the tracking and logging decorators:
@track
@log
def fib(n):
    return n if n in (0, 1) else fib(n - 1) + fib(n - 2)
print(fib(10), 'calls =', fib.count)

