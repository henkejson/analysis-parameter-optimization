# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    bytes_0 = b"\x7f6\x82u\x9b)\xed\xa1\xf5\x0e\xa1\xd3)V\x94\xed\xb5\x9c"
    cached_property_0 = module_0.cached_property(bytes_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, cached_property_0)
    cached_property_0.__get__(cached_property_0, bytes_0)


def test_case_1():
    bytes_0 = b"\x7f\x7f\x82u\x9b)\xed\xa1\xf5\x0e\xa1\xd3)V\x94\xed\xb5\x9c"
    cached_property_0 = module_0.cached_property(bytes_0)
    cached_property_0.__get__(bytes_0, bytes_0)


def test_case_2():
    none_type_0 = None
    cached_property_0 = module_0.cached_property(none_type_0)
