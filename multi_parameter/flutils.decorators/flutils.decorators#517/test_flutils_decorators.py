# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    bytes_0 = b">\x9c\xe0P\xb2\xcc\\\x1a"
    cached_property_0 = module_0.cached_property(bytes_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, none_type_0)
    cached_property_0.__get__(cached_property_0, bytes_0)


def test_case_1():
    bytes_0 = b"\x1e\x9c\xe0.P\xb2\xcc&\x1a"
    cached_property_0 = module_0.cached_property(bytes_0)
    cached_property_0.__get__(bytes_0, cached_property_0)


def test_case_2():
    bytes_0 = b"\x1e\x9c\xe0.P\xb2\xcc&\x1a"
    cached_property_0 = module_0.cached_property(bytes_0)
