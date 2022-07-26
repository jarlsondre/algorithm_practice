from random import sample


integers = [*range(100)]
rand_list = sample(integers, 40)


print(f"random list is: \n {rand_list}")
print(f"sorted list is \n {sorted(rand_list)}")


