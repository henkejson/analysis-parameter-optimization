# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    int_0 = 2447
    cached_property_0 = module_0.cached_property(int_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, none_type_0)
    cached_property_0.__get__(var_0, cached_property_0)


def test_case_1():
    int_0 = 1611
    cached_property_0 = module_0.cached_property(int_0)
    cached_property_0.__get__(int_0, int_0)


def test_case_2():
    int_0 = 1611
    cached_property_0 = module_0.cached_property(int_0)
