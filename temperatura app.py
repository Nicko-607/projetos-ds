temperatura = float(input("Digite a temperatura atual: "))
if temperatura < 0 :
    print("Temperatura abaixo de zero. Está congelando!")
elif temperatura <= 15 :
    print("Temperatura fria. Vista-se adequadamente!") 
elif temperatura <= 25 : 
    print("Temperatura amena. Aproveite o dia!")
elif temperatura <=32 :
    print("Temperatura quente. Hidrate-se e evite exposição prolongada ao sol!")
else :
    print("Temperatura muito quente. Busque ambientes cooler e hidrate-se frequentemente!")