# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    bytes_0 = b"\xbb\x95\xaf\xd8\xdd8\xe6IW`\xc2\xa5\xb6\xb5\xbe:\xb9\xab\xe26"
    cached_property_0 = module_0.cached_property(bytes_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, none_type_0)
    cached_property_0.__get__(bytes_0, bytes_0)


def test_case_1():
    bytes_0 = b"\x02h\xa8\xff%\xaa5"
    cached_property_0 = module_0.cached_property(bytes_0)
    cached_property_0.__get__(cached_property_0, cached_property_0)


def test_case_2():
    str_0 = "/Fu"
    cached_property_0 = module_0.cached_property(str_0)
