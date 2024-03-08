# USO DE *args y **kwargs UNPACKING VARIABLES
print("Ejemplo 1")
users = ['tony', 'andy', 'james']
print (users)
user1, user2, user3 = users
print (user1, user2, user3)
print(user1)
print()

print("Ejemplo 2")
def test_var_args(f_arg, *argv):
    print("primer argumento normal:", f_arg)
    for arg in argv:
        print("argumentos de *argv:", arg)

test_var_args('python', 'foo', 'bar')
print()

print("Ejemplo 3")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print("green:", green)
print("yellow:", yellow)
print("red:", red)