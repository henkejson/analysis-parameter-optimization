# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import builtins as module_1
import collections as module_2


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    object_0 = module_1.object()
    set_0 = {object_0, object_0}
    ordered_dict_0 = module_2.OrderedDict()
    tuple_0 = (set_0, ordered_dict_0, set_0, object_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    float_0 = -2703.9875
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_2.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    bytes_0 = b""
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    str_0 = "K\nH\rT0EcRK H37G.)n"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_7():
    ordered_dict_0 = module_2.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_9():
    str_0 = "@8jAr8"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_10():
    bytes_0 = b"\xd2Kk?\x96~D\xa1\xf7$\xb1\x15\xb2C\xd1"
    dict_0 = {bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_11():
    str_0 = "\x0cjAr8H"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(dict_0)


def test_case_12():
    str_0 = "cherry_pick"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
