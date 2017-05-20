def extract_even(l):
    l_even = [i for i in l if i % 2 == 0]
    return(l_even)

print(extract_even([1, 4, 5, -1, 10]))
      
