# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    bool_0 = False
    none_type_0 = None
    int_0 = 1406
    cached_property_0 = module_0.cached_property(int_0)
    var_0 = cached_property_0.__get__(none_type_0, none_type_0)
    var_0.__get__(bool_0, bool_0)


def test_case_1():
    bool_0 = False
    cached_property_0 = module_0.cached_property(bool_0)
    cached_property_0.__get__(bool_0, bool_0)


def test_case_2():
    none_type_0 = None
    cached_property_0 = module_0.cached_property(none_type_0)
