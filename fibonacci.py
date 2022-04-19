import math

def fibonacci(n) :
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci (n-2)

x = input("Quelle est votre valeur ?")
print("Le résultat est :")
print(fibonacci(int(x)))
