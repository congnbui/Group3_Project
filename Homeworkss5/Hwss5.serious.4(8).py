def get_even_list(l):
    l_even = [i for i in l if i % 2 == 0]
    return(l_even)

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

# the tester called the wrong name of the function. In order to fix this, change the function name in either definition or tester's codes.
