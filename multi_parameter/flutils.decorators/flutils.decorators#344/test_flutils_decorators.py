# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    complex_0 = -2207.7703 - 1486.9651997163953j
    cached_property_0 = module_0.cached_property(complex_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, none_type_0)
    cached_property_0.__get__(var_0, complex_0)


def test_case_1():
    complex_0 = -284.2 - 1293.398292j
    cached_property_0 = module_0.cached_property(complex_0)
    cached_property_0.__get__(complex_0, complex_0)


def test_case_2():
    complex_0 = -284.2 - 1293.398292j
    cached_property_0 = module_0.cached_property(complex_0)
