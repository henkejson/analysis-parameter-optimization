# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    none_type_0 = None
    cached_property_0 = module_0.cached_property(none_type_0)
    var_0 = cached_property_0.__get__(none_type_0, cached_property_0)
    cached_property_0.__get__(cached_property_0, none_type_0)


def test_case_1():
    none_type_0 = None
    cached_property_0 = module_0.cached_property(none_type_0)
    cached_property_0.__get__(cached_property_0, cached_property_0)


def test_case_2():
    bytes_0 = b"\x8f\x0f\xc2-\xc0<Pb\xf1*\x9a\xb9`m<\xf3b"
    cached_property_0 = module_0.cached_property(bytes_0)
