# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    int_0 = 2249
    cached_property_0 = module_0.cached_property(int_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, cached_property_0)
    cached_property_0.__get__(cached_property_0, cached_property_0)


def test_case_1():
    str_0 = "Z7)Z(\rg877x;"
    cached_property_0 = module_0.cached_property(str_0)
    cached_property_0.__get__(str_0, str_0)


def test_case_2():
    none_type_0 = None
    cached_property_0 = module_0.cached_property(none_type_0)
