
def make_pizza(toppings,cheese_type):
    print("bake the dough")
    print(f"add {toppings}")
    print(f"sprinkle {cheese_type} on top")
    print("put inside the oven")
    print("serve fresh")

for i in range(100):
   topping = input("what topping do you want ")
   cheese = input("what type of cheese do you want ")
   make_pizza(topping,cheese)