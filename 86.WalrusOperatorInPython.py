# In this class we shall learn about the Walrus Operator.

a = True
print(a:=False) # So, simple. Walrus Operator --> ':='

foods = list()
# Normal Tarika
# while True :
#     food = input("What food do you like? :")
#     if food == 'quit' :
#         break
#     foods.append(food)
#
    #  USING WALRUS OPERATOR
while (food := input("What food do you like? :")) != "quit" :
    foods.append(food)
