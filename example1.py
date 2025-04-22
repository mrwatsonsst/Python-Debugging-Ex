# example.py

def speak():
    print(f'Hello {name}!')


def some_func():
    name = "Ari"   #input("What's your name? ")
    speak()


def a_func():
    some_func()


# call a_func()
a_func()


