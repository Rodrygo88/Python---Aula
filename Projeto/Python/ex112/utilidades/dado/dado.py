def leiaDinheiro(texto="Digite o preço: R$"):
    while True:
        digito = input(texto).strip()
        digito = digito.replace('R$', '').replace(',', '.').strip()
        
        try:
            valor = float(digito)
            return valor
        except ValueError:
            print("ERRO! Digite um valor numérico válido.")