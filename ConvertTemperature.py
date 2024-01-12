def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin():
    def kelvin_to_celcius(kelvin):
        return (kelvin - 273.15)

def kelvin():
    return (kelvin - 273.15)

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


while True:
    temperature = float(input("Entrez la température : "))
    unit = input("Entrez l'unité (C, F, K) : ").upper()

    if unit == 'C':
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature} °C équivaut à {result} °F")
    elif unit == 'F':
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature} °F équivaut à {result} °C")
    # Ajoutez d'autres conditions pour les unités restantes

    again = input("Voulez-vous convertir une autre température ? (Oui/Non) : ").lower()
    if again != 'oui':
        break


