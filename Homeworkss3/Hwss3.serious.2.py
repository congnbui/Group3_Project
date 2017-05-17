flock = [5, 7, 300, 90, 24, 50, 75]
default_size = 8
months = 6
price = 2

print ("Hello, my name is Cong and these are my sheep sizes")
print(flock)
biggest = max(flock)
print("Now my biggest sheep has size {0} let's sheer it".format(biggest))

print("After sheering, here is my flock")

index = [i for i, j in enumerate(flock) if j == biggest]
flock[index[0]] = default_size
print(flock)

for m in range(months):
    print("MONTH ",m + 1)
    print("One month has passed, now here is my flock")
    
    for i, val in enumerate(flock):
          flock[i] = val + 50
    print(flock)

    if m < months - 1:
        biggest = max(flock)
        print("Now my biggest sheep has size {0} let's sheer it".format(biggest))
        print("After sheering, here is my flock")
        index = [i for i, j in enumerate(flock) if j == biggest]
        flock[index[0]] = default_size
        print(flock)
    else:
        total_size = sum(flock)
        print("My flock has a total size of: ", total_size)
        print("I would get {0} * {1}$ = {2}$".format(total_size, price, total_size * price))
