from functools import reduce

#list of numbers in a tuple:
number = (1, 2, 3, 4, 5, 6, 7)

def sum_all(*n):
    return(sum(n))

def sum_all1(numbers):
    result = 0
    for i in numbers:
        result = result + i
    return result

def main():
    print("Sum of the given numbers{} in a tuple is: {}".format(number, sum_all(1, 2, 3, 4, 5, 6, 7)))
    print("Sum of numbers using for loop: %d" % sum_all1(number))
    print("Sum of numbers in a tuple using reduce function: " + str(reduce((lambda x, y : x + y), number)))
    
if __name__ == "__main__":
    main()
