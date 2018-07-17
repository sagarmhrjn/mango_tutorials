number = (1, 2, 3, 4, 5, 6, 7)
def sum_all(*n):
    return(sum(n))


def main():
    print("Sum of the number{} in a tuple is: {}".format(number, sum_all(1, 2, 3, 4, 5, 6, 7)))


if __name__ == "__main__":
    main()
