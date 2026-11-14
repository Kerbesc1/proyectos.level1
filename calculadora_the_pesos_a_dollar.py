def sumar(a,b): return a + b
def restar(a,b): return a - b
def dividir(a,b): return a / b if b != 0 else "Error: No se puede dividir por cero"
def multiplicar(a,b): return a * b
def pesos_a_dolares(pesos, tasa=60.5):
        return pesos / tasa
    
def dolares_a_pesos(dolares, tasa=60.5):
        return dolares * tasa
    
    
while True: 
    print("/n--- CALCULADORA CON CONVERSOR ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. dividir")
    print("5. salir")
    
    opcion = input("Elige una opcion (1-5); ")
    
    if opcion == "5":
                    print("¡Hasta luego!")
                    break

    if opcion in ["1", "2", "3", "4"]:
                    num1 = float(input("Ingresa el primer numero: "))
                    num2 = float(input("Ingresa el segundo numero: "))
                    
                    if opcion =="1":
                        
                        resultado = sumar(num1, num2)
                    elif opcion == "2":
                        
                        resultado = restar(num1, num2)
                    elif opcion == "3":
                        
                        resultado = multiplicar(num1, num2)
                    elif opcion == "4":
                        
                        resultado = dividir(num1, num2)
                        
                    print(f"\nResultado: {resultado}")  
                        
                        #Si el resultado es un numero (no es el mensaje de error al dividir por 0)
                        
                    if isinstance(resultado, (int , float)):    
                            convertir = input("\n¿Convertir resultado? (1: pesos a dolares / 2: Dolares a peso / Entre para omitir ): ")
                            if convertir == "1":
                            
                                (f"Equivale a: ${pesos_a_dolares(resultado): .2f} USD")
    elif convertir == "2":
                        
                    print(f"Equivale a: RD${dolares_a_pesos(resultado):.2f}")
    else:
        print("opcion no valida Intenta de nuevo.")