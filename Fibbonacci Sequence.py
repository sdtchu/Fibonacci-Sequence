def is_num_even(x):
    if x == 0:
        return True
    elif x == 1:
        return False
    else:
        return is_num_even(x - 2)

def my_fibonacci(x):
    #will take number and add previous num to it
    if x <= 1:
        return x
    else:
        return (my_fibonacci(x-1)) + (my_fibonacci(x-2))

def main():
    x = int(input("Enter a number: "))
    print("The number", x, " is ", is_num_even(x))
    y = int(input("Enter a number: "))
    print("The number", y, " is ", is_num_even(y))
    f = int(input("Enter a number for the Fibonacci sequence: "))
    for i in range(f):
        print(my_fibonacci(i))
main()

