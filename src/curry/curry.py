def _curry_call(fn, max_n, args):
    if max_n < 0: raise Exception("Arity passed is negative")
    if len(args) == max_n:
        try:
            return fn(*args)
        except TypeError as e:
            if 'positional argument' in str(e):
                raise Exception("Incorrect amount of arguments passed to curry")
            raise e
    if len(args) < max_n:
        return lambda x: _curry_call(fn, max_n, args + [x])

def curry(fn, max_n):
    """Каррирует функцию fn для max_n первых аргументов"""
    return _curry_call(fn, max_n, [])

def uncurry(fn, n):
    """Обращает каррирование функции fn для первых max_n аргументов"""
    if n < 0: raise Exception("Arity passed is negative")
    def _inner(*args):
        if len(args) != n:
            raise Exception("Wrong argument number")
        cur = fn(args[0])
        for i in range(1, n):
            cur = cur(args[i])
            if not callable(cur) and i != n - 1:
                raise Exception("Incorrect number of arguments passed to uncurry")
        return cur
    return _inner

def sum(a,b,c):
    print(a,b,c)
    return a+b+c

curried_sum = curry(sum, 4)
print(curried_sum(1)(2)(3))
