Módulo de *testing*
===================

Esta es la documentación para el módulo de test ``test_calculadora.py``, el cual, como su nombre lo indica, se encarga de revisar que el módulo principal ``calculadora.py`` funcione correctamente.

.. automodule:: test_calculadora
   :members:
   :undoc-members:
   :show-inheritance:

Salida en consola
-----------------

Tras haber realizado el test con el comando específico, la salida correspondiente debe tener la forma:

.. code-block::

   ================================================================== test session starts ===================================================================
   platform win32 -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0 -- C:<venv>\Scripts\python.exe
   cachedir: .pytest_cache
   rootdir: C:<venv>\Calculadora Avanzada
   collected 7 items

   code/test_calculadora.py::test_suma PASSED                                                                                                          [ 14%] 
   code/test_calculadora.py::test_resta PASSED                                                                                                         [ 28%] 
   code/test_calculadora.py::test_producto PASSED                                                                                                      [ 42%]
   code/test_calculadora.py::test_cociente PASSED                                                                                                      [ 57%] 
   code/test_calculadora.py::test_potencia PASSED                                                                                                      [ 71%] 
   code/test_calculadora.py::test_raiz PASSED                                                                                                          [ 85%] 
   code/test_calculadora.py::test_modulo PASSED                                                                                                        [100%] 

   =================================================================== 7 passed in 0.14s ====================================================================