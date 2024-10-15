# Calduladora Avanzada
# Autor: Juan Sebastian Manrique Moreno - 20202107016
# Versión: 1.0

# Manejo de matemáticas
import math

# Primera clase
class calculadora:
    """ Esta primera clase está diseñada para una calculadora
        simple que realiza: *suma*, *resta*, *multiplicación* y
        *división*.
    """
    
    # Función para la suma
    def suma(self, a: float, b: float) -> float:
        """ Esta función suma dos números **a** y **b**.
        
            Args:
                a (float): primer número.
                b (float): segundo número.
            
            Returns:
                *float*: La suma de **a** y **b**.
        """
        return a + b

    # Función para la resta
    def resta(self, a: float, b: float) -> float:
        """ Esta función resta dos números **a** y **b**.
        
            Args:
                a (float): primer número.
                b (float): segundo número.
            
            Returns:
                *float*: La resta de **a** y **b**.
        """
        return a - b

    # Función para la multiplicación
    def producto(self, a: float, b: float) -> float:
        """ Esta función multiplica dos números **a** y **b**.
        
            Args:
                a (float): primer número.
                b (float): segundo número.
            
            Returns:
                *float*: El producto de **a** y **b**.
        """
        return a * b

    # Función para la división
    def cociente(self, a: float, b: float) -> float:
        """ Esta función divide dos números **a** y **b**.
        
            Args:
                a (float): primer número (numerador).
                b (float): segundo número (denominador).
            
            Returns:
                *float*: El cociente de **a** y **b**.
            
            Raises:
                ValueError: si **b == 0** :math:`(b = 0)`.
        """
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b

# Segunda clase
class calculadora_avanzada():
    """ Esta segunda clase está diseñada para una calculadora
        avanzada que realiza: *potencia*, *raíz cuadrada* y
        *módulo*.
    """
    
    # Función para la potenciación
    def potencia(self, a: float, b: float) -> float:
        """ Esta función calcula la potencia de un número **a**
            elevado a un número **b**.
        
            Args:
                a (float): primer número (base).
                b (float): segundo número (exponente).
            
            Returns:
                *float*: El resultado de **a** elevado **b** :math:`(a^b)`.

            Raises:
                ValueError: si **a == 0 and b == 0** :math:`(a = b = 0)`.
        """
        if a == 0 and b == 0:
            raise ValueError("Elevar cero a la cero es indeterminado.")
        return a ** b

    # Función para la raíz cuadrada
    def raiz(self, a: float) -> float:
        r""" Esta función calcula la raíz cuadrada de un número **a**.
        
            Args:
                a (float): número al que se le aplica la función raíz cuadrada.
            
            Returns:
                float: El resultado de la raíz de **a** :math:`(\sqrt{a})`.
            
            Raises:
                ValueError: si **a** es negativo.
        """
        if a < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(a)

    # Función para el módulo o residuo
    def modulo(self, a: float, b: float) -> float:
        r""" Esta función calcula el módulo de dos números **a** y **b** que es el residuo de la división entera entre **a** y **b**.
        
            Args:
                a (float): primer número (numerador).
                b (float): segundo número (denominador).
            
            Returns:
                *float*: el módulo de **a** y **b** :math:`(a\mod{b})`.
            
            Raises:
                ValueError: si **b == 0** :math:`(b = 0)`.
        """
        if b == 0:
            raise ValueError("No se puede calcular el módulo con el denominador igual a cero.")
        return a % b

def main():
    """ Esta es la función que ejecuta las operaciones de la
        calculadora y la calculadora avanzada.
    
        De inicio indica la calculadora que usará, así, solicita al
        usuario los **Parámetros** para ejecutar las operaciones.
        
        Finalmente, muestra los resultados obtenidos.
    """
    # Crea el objeto calculadora
    calc = calculadora()

    # Solicita los parámetros para la calculadora simple
    print("Operaciones básicas:")
    a = float(input("Ingrese el primer número (a): "))
    b = float(input("Ingrese el segundo número (b): "))

    # Realizar las operaciones de la calculadora simple
    suma_res = calc.suma(a,b)
    resta_res = calc.resta(a,b)
    producto_res = calc.producto(a,b)
    
    # Detecta el error de la función
    try:
        cociente_res = calc.cociente(a, b)
    except ValueError as e:
        cociente_res = str(e)

    # Mostrar resultados de la calculadora simple
    print(f"Suma: {suma_res}")
    print(f"Resta: {resta_res}")
    print(f"Multiplicación: {producto_res}")
    print(f"División: {cociente_res}")

    # Crea el objeto calculadora avanzada
    calc_avanzada = calculadora_avanzada()

    # Solicita los parámetros para la calculadora avanzada
    print("Operaciones avanzadas:")

    # Potencia
    base = float(input("Ingrese la base de la potencia (a): "))
    exponente = float(input("Ingrese el exponente de la potencia (b): "))
    # Raíz cuadrada
    radicando = float(input("Ingrese el radicando de la raíz cuadrada (a): "))
    # Módulo
    numerador = float(input("Ingrese el numerador (a): "))
    denominador = float(input("Ingrese el denominador (b): "))

    # Realizar las operaciones de la calculadora avanzada
    potencia_res = calc_avanzada.potencia(base, exponente)

    # Detecta el error de las funciones
    try:
        raiz_res = calc_avanzada.raiz(radicando)
    except ValueError as e:
        print(f"Error en raíz cuadrada: {e}")
    try:
        modulo_res = calc_avanzada.modulo(numerador,denominador)
    except ValueError as e:
        print(f"Error en módulo: {e}")

    # Mostrar resultados de la calculadora avanzada
    print(f"Potencia: {potencia_res}")
    print(f"Raíz Cuadrada: {raiz_res}")
    print(f"Módulo: {modulo_res}")


# Ejecución del programa
if __name__ == "__main__": main()