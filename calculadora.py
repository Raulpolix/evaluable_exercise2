import math

# Creamos la clase
class CalculadoraFisica:
    def __init__(self):
        pass

    # Definimos las opciones de la calculadora
    def obtener_opcion_usuario(self):
        print("\nMenú de la Calculadora Física:")
        print("1. Ecuaciones Cinemáticas")
        print("2. Fuerza Gravitacional")
        print("3. Cálculos de Energía")
        print("4. Salir")
        opcion = input("Ingresa tu elección (1-4): ")
        return opcion

    # Definimos la opción de ecuaciones cinemáticas
    def ecuaciones_cinematicas(self):
        print("\nEcuaciones Cinemáticas:")

        # Valores que introducimos
        velocidad_inicial = float(input("Ingresa la velocidad inicial (m/s): "))
        velocidad_final = float(input("Ingresa la velocidad final (m/s): "))
        aceleracion = float(input("Ingresa la aceleración (m/s^2): "))
        tiempo = float(input("Ingresa el tiempo (s): "))

        # Las propias ecuaciones cinemáticas
        desplazamiento = (velocidad_inicial + velocidad_final) * tiempo / 2
        velocidad_final_cuadrada = velocidad_inicial**2 + 2 * aceleracion * desplazamiento

        # Los resultados
        print(f"Desplazamiento: {desplazamiento} metros")
        print(f"Velocidad Final (al cuadrado): {velocidad_final_cuadrada} m^2/s^2")

    # Ahora con la opción de fuerza gravitacional
    def fuerza_gravitacional(self):
        print("\nFuerza Gravitacional:")

        # Valores que introducimos
        masa1 = float(input("Ingresa la masa del objeto 1 (kg): "))
        masa2 = float(input("Ingresa la masa del objeto 2 (kg): "))
        distancia = float(input("Ingresa la distancia entre los objetos (m): "))

        # Fórmula de la fuerza gravitacional
        fuerza_gravitacional = (6.674 * 10**-11) * (masa1 * masa2) / distancia**2

        # Resultados
        print(f"Fuerza Gravitacional: {fuerza_gravitacional} Newtons")

    # Por último, con la opción de cálculos energéticos
    def calculos_energeticos(self):
        print("\nCálculos Energéticos:")

        # Valores que introducimos
        masa = float(input("Ingresa la masa (kg): "))
        altura = float(input("Ingresa la altura (m): "))
        aceleracion_gravitacional = 9.8  # Aceleración debida a la gravedad

        # Fórmula de la energía potencial
        energia_potencial = masa * aceleracion_gravitacional * altura

        # Resultados
        print(f"Energía Potencial: {energia_potencial} Julios")

    # Hacemos que nuestro programa funcione
    def ejecutar_calculadora(self):
        while True:
            opcion = self.obtener_opcion_usuario()

            if opcion == '1':
                self.ecuaciones_cinematicas()
            elif opcion == '2':
                self.fuerza_gravitacional()
            elif opcion == '3':
                self.calculos_energeticos()
            elif opcion == '4':
                print("Saliendo de la Calculadora Física. ¡Adiós!")
                break
            else:
                print("Opción inválida. Por favor, ingresa un número entre 1 y 4.")

if __name__ == "__main__":
    calculadora_fisica = CalculadoraFisica()
    calculadora_fisica.ejecutar_calculadora()
