# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    none_type_0 = None
    float_0 = 5478.0
    cached_property_0 = module_0.cached_property(float_0)
    var_0 = cached_property_0.__get__(none_type_0, none_type_0)


def test_case_1():
    bytes_0 = b"L\xa9Q\x87\xa2\x94\x08\x1aQ\xae\x1aZ~!{lZ\xf3}_"
    cached_property_0 = module_0.cached_property(bytes_0)
    cached_property_0.__get__(cached_property_0, cached_property_0)


def test_case_2():
    bytes_0 = b"L\xa9Q\x87\xa2\x94\x08\x1aQ\xae\x1aZ~!{lZ\xf3}_"
    cached_property_0 = module_0.cached_property(bytes_0)
