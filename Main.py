# Creating a large data set from random number 
import random
large_dataset = [random.randint(0, 1000000) for _ in range(100000)] #generates 100,000 numbers
print(large_dataset)