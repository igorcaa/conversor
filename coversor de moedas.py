class Moeda:
    def __init__(self, nome, cotacao):
        self.nome = nome
        self.cotacao = cotacao

    def para_real(self, valor):
        return valor * self.cotacao

    def de_real(self, valor):
        return valor / self.cotacao


moedas = {
    "dolar": Moeda("dólar", 5.20),
    "euro": Moeda("euro", 4.60),
    "peso": Moeda("peso argentino", 0.005),
    "iene": Moeda("iene japonês", 0.035),
}

print("Olá! Bem-vindo ao conversor de moedas.")

continuar = "sim"

while continuar == "sim":
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
                resultado = round(moeda.para_real(valor), 2)
                print()
                print(f"{valor} {moeda.nome} valem R$ {resultado} hoje.")
            else:
                resultado = round(moeda.de_real(valor), 2)
                print()
                print(f"R$ {valor} valem {resultado} {moeda.nome} hoje.")
        else:
            print("Opa, essa opção não existe. Tente 1 ou 2.")
    else:
        print("Hmm, não conheço essa moeda. Tente uma da lista!")

    print()
    continuar = input("Quer fazer outra conversão? (sim/nao): ").lower()