# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    none_type_0 = None
    none_type_1 = None
    cached_property_0 = module_0.cached_property(none_type_1)
    var_0 = cached_property_0.__get__(none_type_0, none_type_0)


def test_case_1():
    float_0 = 2982.0
    cached_property_0 = module_0.cached_property(float_0)
    cached_property_0.__get__(float_0, cached_property_0)


def test_case_2():
    float_0 = 2982.0
    cached_property_0 = module_0.cached_property(float_0)
