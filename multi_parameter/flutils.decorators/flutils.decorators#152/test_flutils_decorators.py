# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0
import builtins as module_1


def test_case_0():
    complex_0 = -4714.205652 - 2267.7783824429052j
    cached_property_0 = module_0.cached_property(complex_0)
    str_0 = "initial_indent_len"
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, complex_0)
    var_0.__get__(str_0, cached_property_0)


def test_case_1():
    object_0 = module_1.object()
    cached_property_0 = module_0.cached_property(object_0)
    cached_property_0.__get__(cached_property_0, cached_property_0)


def test_case_2():
    complex_0 = -4714.205652 - 2266.633312j
    cached_property_0 = module_0.cached_property(complex_0)
