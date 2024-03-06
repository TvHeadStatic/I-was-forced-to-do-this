
x = 0
y = 0
choice = input("set numbers or input? 1/2\n")
if len(choice) == 1:
  if choice == "1": 
    x = 69
    y = 420
    op = '+'
  elif choice == "2":
    try:
      x = float(input("Input number x: "))
      y = float(input("Input number y: "))
      op = input("Input desired mathematical operation ( + ; - ; * ; / ; % ;): \n")
    except Exception:
      print("There was an Error in input")
      raise
    if y == 0 and op == '/' or y == 0 and op == '%':
      print("can't devide by zero bucko")
      exit()
  match op:
    case '+':
      print(f"You've chosen addition of the numbers {x}, {y} which equals to {x + y}")
    case '-':
      print(f"You've chosen subtraction of the numbers {x}, {y} which equals to {x - y}")
    case '*':
      print(f"You've chosen multiplication of the numbers {x}, {y} which equals to {x * y}")
    case '/':
      print(f"You've chosen division of the numbers {x}, {y} which equals to {x / y}")
    case '%':
      print(f"You've chosen division of the numbers {x}, {y} which has the reminder of {x % y}")
    case '+':
      print(f"You've chosen addition of the numbers {x}, {y} which equals to {x + y}")
else:
  print("Bilek would be disapointed")


print("\nSnakes counting to ten HOLY MOLY")

for i in range(1, 11):
  print(i)


print("\nSnakes can add all numbers to 10 together")

z = 0
for i in range(1, 11):
  z += i
print(z)

print("\nSnakes can identify even numbers to ten excluding zero")

q = 0
while q <= 10:
  if q % 2 == 0 and q !=0 :
    print(q)
  q += 1 


print("\nSnakes multiplying numbers to five HOLY SH!T")

gay = 1
gae = 1
while gay <= 5:
  gae *= gay
  gay += 1
print(gae)