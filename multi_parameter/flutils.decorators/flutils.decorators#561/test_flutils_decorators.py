# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    bytes_0 = b"I:\xf82\x9e$W\xaf\xed\xb6\xda\x07\xfbZ\xe7#U\xea"
    cached_property_0 = module_0.cached_property(bytes_0)
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, cached_property_0)
    cached_property_0.__get__(bytes_0, bytes_0)


def test_case_1():
    str_0 = "Wxlh~$%XMxP+_p7[E>a&"
    cached_property_0 = module_0.cached_property(str_0)
    cached_property_0.__get__(cached_property_0, str_0)


def test_case_2():
    bytes_0 = b"\x8f\xd9\xe7\xdc\xd5\xf4\xad\x7f\xdb\xa7\xec\xafo\xdet\xab~"
    cached_property_0 = module_0.cached_property(bytes_0)
