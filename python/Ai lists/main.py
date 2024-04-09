arr = ['@', 28, 8, 'HATSUNE MIKU', [96,69,6.9], 98069, 'Thats', 'just', 'a', 'THEORY']

print(f"{arr[0]} {arr[int(len(arr)/2)-1]} {arr[int(len(arr)-1)]}")

mEth = 0
for i in range(len(arr)):
    if type(arr[i]) is str:
        for j in range(len(arr[i])):
            mEth += ord(arr[i][j])
    else:
        mEth += arr[i]
print(mEth)
























# 1. Vytvořte arr s různými druhy dat. (čísla, string, minimálně 10 různých hodnot).
#2. Pomocí indexu vypište první, střední a poslední zadané hodnoty.
#4. Sečtěte prvky arru a vypište jejich výsledek.
#5. Vypište nejmenší a největší hodnotu v arru.
#6. Pokud se v arru objevují stejná data ze arru je odstraňte a znovu vypište.
#7. Vyměňte 3 hodnoty arru za libovolné hodnoty. (První, střední a poslední) - znovu vypište upravený arr.