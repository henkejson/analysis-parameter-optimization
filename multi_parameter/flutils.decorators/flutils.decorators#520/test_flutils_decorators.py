# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import builtins as module_0
import flutils.decorators as module_1


def test_case_0():
    object_0 = module_0.object()
    cached_property_0 = module_1.cached_property(object_0)
    object_1 = module_0.object()
    none_type_0 = None
    var_0 = cached_property_0.__get__(none_type_0, object_0)
    var_0.__get__(object_1, cached_property_0)


def test_case_1():
    bool_0 = True
    cached_property_0 = module_1.cached_property(bool_0)
    cached_property_0.__get__(cached_property_0, cached_property_0)


def test_case_2():
    object_0 = module_0.object()
    cached_property_0 = module_1.cached_property(object_0)
