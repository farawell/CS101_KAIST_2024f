def fibonacci(upper_bound):
    fib_list = [0, 1]
    while True:
        next_num = fib_list[-1] + fib_list[-2]
        if next_num < 1000: fib_list.append(next_num)
        else: return fib_list

print(fibonacci(1000))
