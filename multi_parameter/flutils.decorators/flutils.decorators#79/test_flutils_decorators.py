# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    none_type_0 = None
    dict_0 = {}
    cached_property_0 = module_0.cached_property(dict_0)
    var_0 = cached_property_0.__get__(none_type_0, none_type_0)


def test_case_1():
    bytes_0 = b"\x9a\x12*\x99\x0be\xe42v\x8d\x12\x88I\x06\x81\x06+\xee"
    cached_property_0 = module_0.cached_property(bytes_0)
    cached_property_0.__get__(bytes_0, bytes_0)


def test_case_2():
    bytes_0 = b"\x9a\x12*\x99\x0be\xe42v\x8d\x12\x88I\x06\x81\x06+\xee"
    cached_property_0 = module_0.cached_property(bytes_0)
