# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    float_0 = -149.73
    none_type_0 = None
    cached_property_0 = module_0.cached_property(none_type_0)
    cached_property_1 = module_0.cached_property(cached_property_0)
    var_0 = cached_property_1.__get__(none_type_0, cached_property_0)
    cached_property_2 = module_0.cached_property(var_0)
    cached_property_0.__get__(float_0, float_0)


def test_case_1():
    none_type_0 = None
    cached_property_0 = module_0.cached_property(none_type_0)
    cached_property_0.__get__(cached_property_0, none_type_0)


def test_case_2():
    none_type_0 = None
    cached_property_0 = module_0.cached_property(none_type_0)
