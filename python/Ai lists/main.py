arr = ['@', 28, 8, 'HATSUNE MIKU', 'uwu', 98069, 'Thats', 'just', 'a', 'THEORY'] #multi value array

print(f"{arr[0]} {arr[int(len(arr)/2)-1]} {arr[int(len(arr)-1)]}")

mEth = []
for i in range(len(arr)):
    if type(arr[i]) is str:
        for j in range(len(arr[i])):
            mEth.append (ord(arr[i][j]))
    else:
        mEth.append (arr[i])
print(sum(mEth))

mEth.sort()
print(f"{mEth[0]} {mEth[len(mEth)-1]}")




