# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    str_0 = "b?"
    cached_property_0 = module_0.cached_property(str_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, cached_property_0)
    list_0 = []
    cached_property_1 = module_0.cached_property(list_0)
    cached_property_1.__get__(cached_property_1, cached_property_1)


def test_case_1():
    list_0 = []
    cached_property_0 = module_0.cached_property(list_0)
    cached_property_0.__get__(list_0, list_0)


def test_case_2():
    none_type_0 = None
    cached_property_0 = module_0.cached_property(none_type_0)
