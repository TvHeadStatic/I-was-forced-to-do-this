x = [[8,72,555],[420,69,15],[34,156,999]]


def bubble_sort(x):
  n = len(x)
  for k in range(n):
    for i in range(len(x[k])):
      for j in range(n-i-1):
        if x[k][j] > x[k][j + 1]:
          x[k][j], x[k][j + 1] = x[k][j + 1], x[k][j]

  return x
    



def selection_sort(y):
  n = len(y)
  for k in range(n):
    for i in range(len(y[k])):
      min_index = i
      for j in range(i+1, n):
        if y[k][j] < y[k][min_index]:
          min_index = j
      y[k][i], y[k][min_index] = y[k][min_index], y[k][i]
  return y


def insertion_sort(z):
  for k in range(1, len(z)):
    for i in range(1, len(z[k])):
      key = z[k][i]
      j = i-1
      while j >=0 and key < z[k][j] :
        z[k][j+1] = z[k][j]
        j -= 1
      z[k][j+1] = key
    return z

def print_2d_matrix(array):
  for i in range(len(array)):
    print(array[i])


def partition(unsortedArray, low, high):
    pivot = unsortedArray[high]
    i = low - 1
    for j in range(low, high):
        if unsortedArray[j] <= pivot:
            i = i + 1
            (unsortedArray[i], unsortedArray[j]) = (unsortedArray[j], unsortedArray[i])
    (unsortedArray[i + 1], unsortedArray[high]) = (unsortedArray[high], unsortedArray[i + 1])
    return i + 1
 
def quick_sort(unsortedArray, low, high):
  if low < high:
    part = partition(unsortedArray, low, high)
    quick_sort(unsortedArray, low, part - 1)
    quick_sort(unsortedArray, part + 1, high)

def quick_sort_2d(unsortedArray):
  for i in range (len(unsortedArray)):
    quick_sort(unsortedArray[i], 0, len(unsortedArray[i]) - 1)

def print_2d_matrix(v):
  for i in range(len(v)):
    print(v[i])


print("\nUnsorted array:")
print_2d_matrix(x)

print("\nBubble sorter array:")
print_2d_matrix(bubble_sort(x)) 

print("\nSelection sorted array:")
print_2d_matrix(selection_sort(x))

print("\nInsertion sorted array:")
print_2d_matrix(insertion_sort(x))

print("\nQuick sorted array:")
quick_sort_2d(x)
print_2d_matrix(x)