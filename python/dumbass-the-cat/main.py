z = [48,5,69,452,102,78,3560]
print("Assorted array a:" , z)
y = [58,8469,526,59,26,4,11]
print("Assorted array b:" , y)

z.sort()
print("Sorted array a:" , z)

def bubbleSort(y):
  n = len(y)
  swapped = False
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if y[j] > y[j + 1]:
        swapped = True
        y[j], y[j + 1] = y[j + 1], y[j]
    if not swapped:
      return

bubbleSort(y)
print(f"Bubble sorted array b: {y}")