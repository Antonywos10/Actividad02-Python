def verificar_tributacion():
    try:
        
        edad = int(input("Introduce tu edad: "))
        ingresos = float(input("Introduce tus ingresos mensuales en euros: "))

        
        if edad > 16 and ingresos >= 1000:
            print("Debes tributar.")
        else:
            print("No debes tributar.")
    except ValueError:
        print("Por favor, introduce datos válidos para la edad y los ingresos.")

verificar_tributacion()
