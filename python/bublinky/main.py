x = [59,56,35,1,25,8]

def bubble_sort(x):
  n = len(x)
  for i in range(n):
    for j in range(n-i-1):
      if x[j] > x[j + 1]:
        x[j], x[j + 1] = x[j + 1], x[j]

  return x
    
print(x)
print(bubble_sort(x)) 

y= [95,67,49,489,182,2]

def selection_sort(y):
  n = len(y)
  for i in range(n):
    min_index = i
    for j in range(i+1, n):
      if y[j] < y[min_index]:
        min_index = j
    y[i], y[min_index] = y[min_index], y[i]
  return y

print(y)
print(selection_sort(y))

z = [58,46,89,185,354,0]

def insertion_sort(z):
  for i in range(1, len(z)):
    key = z[i]
    j = i-1
    while j >=0 and key < z[j] :
      z[j+1] = z[j]
      j -= 1
    z[j+1] = key
  return z

print(z)
print(insertion_sort(z))

