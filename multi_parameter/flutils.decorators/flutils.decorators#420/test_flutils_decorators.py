# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    bytes_0 = b"\xc4"
    cached_property_0 = module_0.cached_property(bytes_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, none_type_0)
    cached_property_0.__get__(cached_property_0, bytes_0)


def test_case_1():
    str_0 = "o<"
    cached_property_0 = module_0.cached_property(str_0)
    cached_property_0.__get__(str_0, str_0)


def test_case_2():
    bool_0 = True
    cached_property_0 = module_0.cached_property(bool_0)
