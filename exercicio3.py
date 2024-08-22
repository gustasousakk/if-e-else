valor=int(input("valor="))
valorD= valor-(valor*0.20)
if valor>= 200:
    print(f"O desconto foi aplicado! Total de R${valorD}")
else:
    print(f"Não conseguimos aplicar o desconto, pague R$,{valor}")