# This code has errors in it!
# Let use print() to help debug it.
# Then we'll use the debugger later...


num_people = 3
num_registered = 0

def a_function():
    result = 2 + 2

# function registers person and then increments number_registered
def register():

    number_registered += 1
    a_function()


while num_registered >= num_people:
    register()


print(f"There are {num_registered} registered people.\n")
print("Done registering")


# ... continue with other code

