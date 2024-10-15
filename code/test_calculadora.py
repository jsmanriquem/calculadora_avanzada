# Calculadora Avanzada: Test
# Autor: Juan Sebastian Manrique Moreno - 20202107016

# Librerías para hacer test y módulo principal
import pytest
from calculadora import calculadora, calculadora_avanzada

# Crea los objetos para las pruebas
calc_simple = calculadora()
"""Se instancia el objeto para la calculadora simple."""
calc_avanzada = calculadora_avanzada()
"""Se instancia el objeto para la calculadora avanzada."""

# Test para la calculadora simple

# Test suma
def test_suma():
    """ Pruebas a realizar para la suma:

        - **calc_simple.suma(0, 7)** debe ser igual a **7** :math:`(0 + 7 = 0)`.
        - **calc_simple.suma(-10, -5)** debe ser igual a **-15** :math:`((-10) + (-5) = -15)`.
        - **calc_simple.suma(1.5, 2.5)** debe ser igual a **4** :math:`(1.5 + 2.5 = 4)`.
    """
    assert calc_simple.suma(0, 7) == 7
    assert calc_simple.suma(-10, -5) == -15
    assert calc_simple.suma(1.5, 2.5) == 4

# Test resta
def test_resta():
    """ Pruebas a realizar para la resta:

        - **calc_simple.resta(100, 50)** debe ser igual a **50** :math:`(100 - 50 = 50)`.
        - **calc_simple.resta(-5, 10)** debe ser igual a **-15** :math:`((-5) - 10 = -15)`.
        - **calc_simple.resta(3.2, 1.2)** debe ser igual a **2** :math:`(3.2 - 1.2 = 2)`.
    """
    assert calc_simple.resta(100, 50) == 50
    assert calc_simple.resta(-5, 10) == -15
    assert calc_simple.resta(3.2, 1.2) == 2

# Test producto
def test_producto():
    r""" Pruebas a realizar para el producto:

        - **calc_simple.producto(7, 6)** debe ser igual a **42** :math:`(7 \cdot 6 = 42)`.
        - **calc_simple.producto(-3, 7)** debe ser igual a **-21** :math:`(-3 \cdot 7 = -21)`.
        - **calc_simple.producto(1.1, 2)** debe ser igual a **2.2** :math:`(1.1 \cdot 2 = 2.2)`.
    """
    assert calc_simple.producto(7, 6) == 42
    assert calc_simple.producto(-3, 7) == -21
    assert calc_simple.producto(1.1, 2) == 2.2

# Test cociente
def test_cociente():
    r""" Pruebas a realizar para el cociente:

        - **calc_simple.cociente(100, 5)** debe ser igual a **20** :math:`(100 \div 5 = 20)`.
        - **calc_simple.cociente(3, 2)** debe ser igual a **1.5** :math:`(3 \div 2 = 1.5)`.
        - Verifica que se lance un error al dividir por cero.
    """
    assert calc_simple.cociente(100, 5) == 20
    assert calc_simple.cociente(3, 2) == 1.5
    with pytest.raises(ValueError):
        calc_simple.cociente(10, 0)

# Test para la calculadora avanzada

# Test potencia
def test_potencia():
    """ Pruebas para la potencia:

        - **calc_avanzada.potencia(5, 2)** debe ser igual a **25** :math:`(5^{2} = 25)`.
        - **calc_avanzada.potencia(4, 3)** debe ser igual a **64** :math:`(4^{3} = 64)`.
        - **calc_avanzada.potencia(-2, 3)** debe ser igual a **-8** :math:`((-2)^{3} = -8)`.
    """
    assert calc_avanzada.potencia(5, 2) == 25
    assert calc_avanzada.potencia(4, 3) == 64
    assert calc_avanzada.potencia(-2, 3) == -8

# Test raíz
def test_raiz():
    r""" Pruebas para la raíz cuadrada:

        - **calc_avanzada.raiz(25)** debe ser **5** :math:`(\sqrt{25} = 5)`.
        - **calc_avanzada.raiz(144)** debe ser **12** :math:`(\sqrt{144} = 12)`.
        - Verifica que se lance un error al calcular la raíz cuadrada de un número negativo.
    """
    assert calc_avanzada.raiz(25) == 5
    assert calc_avanzada.raiz(144) == 12
    with pytest.raises(ValueError):
        calc_avanzada.raiz(-9)

# Test módulo
def test_modulo():
    r""" Pruebas para el módulo:

        - **calc_avanzada.modulo(20, 6)** debe ser igual a **2** :math:`(20\mod{6} = 2)`.
        - **calc_avanzada.modulo(18, 5)** debe ser igual a **3** :math:`(18\mod{5} = 3)`.
        - Verifica que se lance un error al calcular el módulo por cero.
    """
    assert calc_avanzada.modulo(20, 6) == 2
    assert calc_avanzada.modulo(18, 5) == 3
    with pytest.raises(ValueError):
        calc_avanzada.modulo(15, 0)