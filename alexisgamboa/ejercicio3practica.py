#ejercicio3
renta = float(input("Introduce tu renta anual: "))

if renta < 10000:
    tipo_impositivo = "10"
elif 10000 <= renta < 20000:
    tipo_impositivo = "15"
elif 20000 <= renta < 35000:
    tipo_impositivo = "20"
elif 35000 <= renta < 60000:
    tipo_impositivo = "25"
else:
    tipo_impositivo = "45"

print(f"Tu tipo impositivo es: {tipo_impositivo}%")
