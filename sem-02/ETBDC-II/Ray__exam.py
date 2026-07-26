
# Soham Bhattacharya
# Reg.No.: B2430059
# RKMVERI

# ~ Distributed Computing
# ~ Marks 30
# ~ Given a list of 10,000 integers, compute the square of each number using Remote function and using Actor
# ~ in Ray. Sort them, and return the first 10 smallest squared values.


import ray
import random

ray.init()

# Random 10,000 integers generated. Ekhane took the range (-10,10)
data = [random.randint(999, 10000) for _ in range(10000)]
print(data[4995:5005]) # Checking whether the data is generated properly


# ================== REMOTE function use kore ==========================
# Ray remote function to compute square

print("\n================== using only REMOTE function =================")

@ray.remote
def square(x):
    return x * x

# Distribute the task
futures = [square.remote(x) for x in data]

# Gather results
squared = ray.get(futures)

# Sort and get first 10 smallest squared values
sorted_remote = sorted(squared)[:10]
print("Smallest 10 squared values (Remote Function):", sorted_remote)



# ================== ACTOR function use kore ===========================


print("\n====================== using ACTOR class ======================")

@ray.remote
class Squarer:
    def square(self, x):
        return x * x


actor = Squarer.remote() # instance of the Actor class 'Squarer'
futures = [actor.square.remote(x) for x in data] # distributes the task

squared = ray.get(futures) # receives the aggregated results
# Ekhane returns the squares of the values

# Sort and get first 10 smallest squared values
sorted_actor = sorted(squared)[:10]
print("Smallest 10 squared values (Actor):", sorted_actor)


# ============================== END ===================================
