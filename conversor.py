class Conversor:
    def __init__(self, nome, fator=None):
        self.nome = nome
        self.fator = fator

    def para_base(self, valor):
        return valor * self.fator

    def de_base(self, valor):
        return valor / self.fator

    def fahrenheit_para_kelvin(self, valor):
        return (valor - 32) * 5 / 9 + 273.15

    def kelvin_para_fahrenheit(self, valor):
        return (valor - 273.15) * 9 / 5 + 32


moedas = {
    "dolar": Conversor("dólar", 5.20),
    "euro": Conversor("euro", 4.60),
    "peso": Conversor("peso argentino", 0.005),
    "iene": Conversor("iene japonês", 0.035),
}

comprimentos = {
    "km": Conversor("quilômetro", 1000),
    "m": Conversor("metro", 1),
    "cm": Conversor("centímetro", 0.01),
    "mm": Conversor("milímetro", 0.001),
}

massas = {
    "kg": Conversor("quilograma", 1000),
    "g": Conversor("grama", 1),
    "mg": Conversor("miligrama", 0.001),
}

volumes = {
    "l": Conversor("litro", 1),
    "ml": Conversor("mililitro", 0.001),
}

grandezas = {
    "3": comprimentos,
    "4": massas,
    "5": volumes,
}

temperatura = Conversor("temperatura")

print("Olá! Bem-vindo ao conversor.")

continuar = "sim"

while continuar == "sim":
    print()
    print("Qual tipo de conversão você quer?")
    print("1 - Moedas")
    print("2 - Temperatura")
    print("3 - Comprimento")
    print("4 - Massa")
    print("5 - Volume")
    tipo = input("Digite de 1 a 5: ")

    if tipo == "1":
        print()
        print("Moedas disponíveis: dolar, euro, peso, iene")
        escolha = input("Qual moeda você quer usar? ").lower()

        if escolha in moedas:
            moeda = moedas[escolha]

            print()
            print("O que você quer fazer?")
            print("1 - Transformar", moeda.nome, "em reais")
            print("2 - Transformar reais em", moeda.nome)
            operacao = input("Digite 1 ou 2: ")

            if operacao == "1" or operacao == "2":
                valor = float(input("Qual o valor? "))

                if operacao == "1":
                    resultado = round(moeda.para_base(valor), 2)
                    print()
                    print(f"{valor} {moeda.nome} valem R$ {resultado} hoje.")
                else:
                    resultado = round(moeda.de_base(valor), 2)
                    print()
                    print(f"R$ {valor} valem {resultado} {moeda.nome} hoje.")
            else:
                print("Opa, essa opção não existe. Tente 1 ou 2.")
        else:
            print("Hmm, não conheço essa moeda. Tente uma da lista!")

    elif tipo == "2":
        print()
        print("O que você quer fazer?")
        print("1 - Transformar Fahrenheit em Kelvin")
        print("2 - Transformar Kelvin em Fahrenheit")
        operacao = input("Digite 1 ou 2: ")

        if operacao == "1" or operacao == "2":
            valor = float(input("Qual o valor? "))

            if operacao == "1":
                resultado = round(temperatura.fahrenheit_para_kelvin(valor), 2)
                print()
                print(f"{valor} °F valem {resultado} K.")
            else:
                resultado = round(temperatura.kelvin_para_fahrenheit(valor), 2)
                print()
                print(f"{valor} K valem {resultado} °F.")
        else:
            print("Opa, essa opção não existe. Tente 1 ou 2.")

    elif tipo in grandezas:
        unidades = grandezas[tipo]

        print()
        print("Unidades disponíveis:", ", ".join(unidades))
        origem = input("Converter de qual unidade? ").lower()
        destino = input("Para qual unidade? ").lower()

        if origem in unidades and destino in unidades:
            valor = float(input("Qual o valor? "))

            na_base = unidades[origem].para_base(valor)
            resultado = round(unidades[destino].de_base(na_base), 4)
            print()
            print(f"{valor} {origem} valem {resultado} {destino}.")
        else:
            print("Hmm, não conheço essa unidade. Tente uma da lista!")

    else:
        print("Opa, essa opção não existe. Tente de 1 a 5.")

    print()
    continuar = input("Quer fazer outra conversão? (sim/nao): ").lower()