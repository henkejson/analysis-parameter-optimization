# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    bytes_0 = b"\xe4\x9b\xae\xb8C(\xf5\xbfW\xa0\x0b\xab\x8a\x1d\x9e\x99\x9e"
    cached_property_0 = module_0.cached_property(bytes_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, cached_property_0)
    var_0.__get__(cached_property_0, bytes_0)


def test_case_1():
    bytes_0 = b"\xe4\x9b\xae\xb8xC(\xf5\xbfW\xa0\xdb\x0b\xab\x8a\x1d\x9e\x99\x9e"
    cached_property_0 = module_0.cached_property(bytes_0)
    cached_property_0.__get__(bytes_0, bytes_0)


def test_case_2():
    none_type_0 = None
    cached_property_0 = module_0.cached_property(none_type_0)
