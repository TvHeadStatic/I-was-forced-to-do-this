y = [[5,9.00089,6],[4,7,0.09],[4,59,6]]
print(y) #prints variable
print(y[2][1]) #prints the 2nd number of the 3rd column in set variable
print(len(y)) #prints the length of said variable
print(y[1])  #prints the 2nd column in variable 

print("2d matrix under:")


def print_2d_matrix(y): 
  for i in range (len(y)):
    print(y[i])
#defines a '2d matrix' making each column be printed underneath eachother rather than inline 

print_2d_matrix(y) #prints said variable in a 2d matrix