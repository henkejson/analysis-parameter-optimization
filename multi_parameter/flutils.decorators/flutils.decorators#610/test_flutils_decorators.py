# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    set_0 = set()
    cached_property_0 = module_0.cached_property(set_0)
    none_type_0 = None
    cached_property_1 = module_0.cached_property(none_type_0)
    var_0 = cached_property_0.__get__(none_type_0, cached_property_1)


def test_case_1():
    bytes_0 = b"\xc3\xb5\x0b\xb6\xa7?\xd3"
    cached_property_0 = module_0.cached_property(bytes_0)
    cached_property_0.__get__(cached_property_0, bytes_0)


def test_case_2():
    int_0 = 2527
    cached_property_0 = module_0.cached_property(int_0)
