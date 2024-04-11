arr = ['@', 8, 8, 'HATSUNE MIKU', 'uwu', 98069, 'Thats', 'just', 'a', 'THEORY'] #multi value array

print(f"ze hell fire of an arrah: {arr}")

print(f"{arr[0]} {arr[int(len(arr)/2)-1]} {arr[int(len(arr)-1)]}")

mEth = []
for i in range(len(arr)):
    if type(arr[i]) is str:
        for j in range(len(arr[i])):
            mEth.append (ord(arr[i][j]))
    else:
        mEth.append (arr[i])
print(f"don't ask how but we added all of it: {sum(mEth)}")

mEth.sort()
print(f"Lowest and highest value in ze arrah: {mEth[0]} {mEth[len(mEth)-1]}")

ඞ = 0 

for z in arr:
    ඞ += 1
    for w in range(ඞ, len(arr)):
        if z  == arr[w]:
            arr.remove(z)
            break 
print(f"Removes dupes from arrah: {arr}")

arr[0] = 'ඞ'
arr[int(len(arr)/2)-1] = 'ඞ'
arr[int(len(arr)-1)] = 'ඞ'

print(f"Replaced 3 values for something more fun :3 {arr}")