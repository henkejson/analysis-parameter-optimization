# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    bytes_0 = b"\xeeh"
    cached_property_0 = module_0.cached_property(bytes_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, cached_property_0)
    cached_property_0.__get__(cached_property_0, cached_property_0)


def test_case_1():
    bytes_0 = b""
    cached_property_0 = module_0.cached_property(bytes_0)
    cached_property_0.__get__(bytes_0, bytes_0)


def test_case_2():
    complex_0 = 4399.4307 - 2158j
    cached_property_0 = module_0.cached_property(complex_0)
