# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    list_0 = []
    none_type_0 = None
    cached_property_0 = module_0.cached_property(list_0)
    var_0 = cached_property_0.__get__(none_type_0, none_type_0)
    var_0.__get__(list_0, none_type_0)


def test_case_1():
    tuple_0 = ()
    cached_property_0 = module_0.cached_property(tuple_0)
    cached_property_0.__get__(tuple_0, tuple_0)


def test_case_2():
    dict_0 = {}
    cached_property_0 = module_0.cached_property(dict_0)
