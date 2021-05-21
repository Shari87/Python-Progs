# Program to generate a christmas tree pattern

num = int(input("enter the number of rows : " ))

for i in range(1, num+1):
    print(" "*(num-i)+"* "*i)

for j in range(num-(num//2)):
    print(" "*(num-1)+"*")

#print(type(range(4)))