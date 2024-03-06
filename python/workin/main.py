a_ray = [[9,13,422,9,18],[5,.16,300,88,2.1],[73,58,98,444,666],[28,3000,.001,809,75]] #1

print(f"Thou array: {a_ray}")

print(f"Length of thou array: {len(a_ray)}") #2

print(f"Array in the 3rd position in thou array: {a_ray[2]}") #3

print(f"The 2nd number in the 3rd array in thou array: {a_ray[2][1]}") #4

add = []

for i in range(4):
    add += a_ray[i]

print(f"all the arrays added together: {add}")  #5

def print_2d_matrix(array):
  for i in range(len(array)):
    print(array[i])

print_2d_matrix(a_ray) #6

a = [[0.]*4]*2
print(a)
for y in range(1):
    a[y][2] = 69.

print(f"Creates an array with changed number: {a}") #7

b = [[0.]*4 for _ in range(5)]
print("Created an array with 5 rows and 3 columns:") #8
print_2d_matrix(b)

b[1][1] = 4.
print("Thee changed number in array") #9
print_2d_matrix(b)