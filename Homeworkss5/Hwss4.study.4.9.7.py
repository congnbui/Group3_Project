def sum_to(n):
    """Sum of all integers up to n"""
    a = 0
    for i in range(n):
        a = a + i + 1
    return a

while True:

    n = int(input("Enter a positive integer: "))
    print("The sum of all integers up to ", n," is: ",sum_to(n))
