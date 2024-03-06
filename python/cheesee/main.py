x = "Static"
y = "Television"
z= " 3"
xy = x + ' ' +  y

print("Greatings I am: " + y + ' ' + x)
print(len(xy))
print(len(x))
print(len(y))
print(y.upper() + ' ' + x.lower())
print(xy.count("i"))
print(x.startswith('T'))
print(y.endswith('sion'))
print(y.replace('l', 'r'))
print(xy.strip())
print(z.lstrip())
print('a' not in y)
print(y.index('e'))
print(y.index('e', 1))
print(x * 3)
print('%s?' % xy)
print('{0}:3'.format(xy))