

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division par zéro"


num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le deuxième nombre : "))
operation = input("Entrez l'opération (+, -, *, /) : ")


if operation == '+':
    resultat = addition(num1, num2)
elif operation == '-':
    resultat = soustraction(num1, num2)
elif operation == '*':
    resultat = multiplication(num1, num2)
elif operation == '/':
    resultat = division(num1, num2)
else:
    resultat = "Opération non valide"

print(f"Résultat : {resultat}")
