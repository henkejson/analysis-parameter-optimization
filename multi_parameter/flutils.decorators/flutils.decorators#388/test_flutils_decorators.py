# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    bytes_0 = b'8\x7f\xa2/"\xd5\x85\xd5\xfa\x9d$?_(^'
    cached_property_0 = module_0.cached_property(bytes_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, none_type_0)
    var_0.__get__(bytes_0, cached_property_0)


def test_case_1():
    bytes_0 = b'8\x7f\xa2/"\xcb\x85\xd5\xfa\x9d$\xb3?_(^'
    cached_property_0 = module_0.cached_property(bytes_0)
    cached_property_0.__get__(bytes_0, cached_property_0)


def test_case_2():
    bytes_0 = b'8\x7f\xa2/"\xcb\x85\xd5\xfa\x9d$\xb3?_(^'
    cached_property_0 = module_0.cached_property(bytes_0)
