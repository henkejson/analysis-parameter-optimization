# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import builtins as module_1
import collections as module_2


def test_case_0():
    bool_0 = True
    module_0.to_namedtuple(bool_0)


def test_case_1():
    object_0 = module_1.object()
    list_0 = [object_0, object_0, object_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_2():
    float_0 = -4252.2
    str_0 = "t"
    dict_0 = {str_0: str_0, float_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_4():
    str_0 = "f]E-Xg>jNb7^2-T^\\"
    module_0.to_namedtuple(str_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    list_0 = []
    ordered_dict_0 = module_2.OrderedDict(*list_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_7():
    list_0 = []
    ordered_dict_0 = module_2.OrderedDict(*list_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    str_0 = "~NT\x0cq1:"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    ordered_dict_0 = module_2.OrderedDict(**dict_0)


def test_case_9():
    list_0 = []
    ordered_dict_0 = module_0.to_namedtuple(list_0)


def test_case_10():
    bytes_0 = b"\xf0\xd2\xff\x1a"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_11():
    float_0 = -4252.2
    tuple_0 = (float_0, float_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    list_0 = [var_0, var_0, var_0, var_0]
    object_0 = module_1.object()
    var_1 = module_0.to_namedtuple(list_0)
    str_0 = "\x0b\ts"
    dict_0 = {str_0: str_0, var_0: list_0}
    var_2 = module_0.to_namedtuple(dict_0)
    ordered_dict_0 = module_0.to_namedtuple(list_0)
    var_3 = module_0.to_namedtuple(ordered_dict_0)
    var_4 = module_0.to_namedtuple(ordered_dict_0)
    var_5 = module_0.to_namedtuple(var_4)
    module_0.to_namedtuple(object_0)
