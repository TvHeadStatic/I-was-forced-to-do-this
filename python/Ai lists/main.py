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

#print("1. Vytvořte seznam s různými druhy dat. (čísla, string, minimálně 10 různých hodnot).")
#seznam = [
    #"fafs",
    #2.2,
    #69,
    #'R',
    #"hi",
    #86,
    #"fafs",
    #'A',
    #9,
    #420
#]
#print(seznam)

#print("\n2. Pomocí indexu vypište první, střední a poslední zadané hodnoty.")
#print(f"{seznam[0]} {seznam[round((len(seznam)-1)/2)]} {seznam[len(seznam)-1]}")

#print("\n4. Sečtěte prvky seznamu a vypište jejich výsledek.")
#soucet = 0
#for i in range(len(seznam)):
    #if type(seznam[i]) is str:
        #for j in range(len(seznam[i])):
            #soucet += ord(seznam[i][j])
    #else:
       # soucet += seznam[i]
#print(soucet)

#print("\n5. Vypište nejmenší a největší hodnotu v seznamu.")
#newseznam = []
#newsoucet = 0
#for i in range(len(seznam)):
   # if type(seznam[i]) is not str:
       # newseznam.append(int(seznam[i]))
       # continue
    #for j in range(len(seznam[i])):
        #newsoucet += int(ord(seznam[i][j]))
    #newseznam.append(newsoucet)
    #newsoucet = 0
#newnewseznam = sorted(newseznam)
#print(f"{seznam[newseznam.index(newnewseznam[0])]} {seznam[newseznam.index(newnewseznam[len(newnewseznam)-1])]}")

#print("\n6. Pokud se v seznamu objevují stejná data ze seznamu je odstraňte a znovu vypište.")
#key = 0
#for x in seznam:
    #key += 1
    #for y in range(key, len(seznam)):
        #if x == seznam[y]:
           # seznam.remove(x)
           # break
#print(seznam)

#print("\n7. Vyměňte 3 hodnoty seznamu za libovolné hodnoty. (První, střední a poslední) - znovu vypište upravený seznam.")
#seznam[0] = "fafdsa"
#seznam[1] = 69420
#seznam[2] = 'S'      
