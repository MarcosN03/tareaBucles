def numero(num):
    for i in range(1, num+1, 2):
        print(i, end=",")
num = int(input("Introduce un numero positivo:"))    
numero(num)
