# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    bytes_0 = b"{\xc4"
    cached_property_0 = module_0.cached_property(bytes_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, bytes_0)
    cached_property_0.__get__(cached_property_0, none_type_0)


def test_case_1():
    bytes_0 = b"\x16\xed\x00\xec\xbc"
    cached_property_0 = module_0.cached_property(bytes_0)
    cached_property_0.__get__(bytes_0, bytes_0)


def test_case_2():
    int_0 = -267
    cached_property_0 = module_0.cached_property(int_0)
