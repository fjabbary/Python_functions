# ==================================================================== 
# ===================// Task 1 - The Calculator App //================
# ==================================================================== 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
opertion = input("Please enter the opreration: add, subtract, multiply or divide: ")

def calculate():
  if opertion == "add":
    return num1 + num2
  elif opertion == "subtract":
    return num1 - num2
  elif opertion == "multiply":
    return num1 * num2
  elif opertion == "divide":
    if num2 == 0:
       return "Error! Division by zero is not allowed."
    else:
      return num1 / num2

print(calculate());

  
# ==================================================================== 
# ===================// Task 1 - The Calculator App //================
# ====================================================================  
  
def shopping():
  shopping_list = []
  while True:
    action = input("What would you like to do? Please type add, remove, or quit: ")
    if action == 'add':
      item = input("Enter the name of item you want to add: ")
      shopping_list.append(item)
      print("Items in your cart so far => ", shopping_list) 
      print("\n")
    
    elif action == 'remove':
      item = input("Enter the name of item you want to remove: ")
      if item in shopping_list:
        shopping_list.remove(item)
        print("Items in your cart so far => ", shopping_list) 
        print("\n")
      else:
        print(f"You don't have {item} in your shopping list")
      
    elif action == 'quit':
      break
    
  return f"Final items: {shopping_list}"  
  
  
print(shopping())  