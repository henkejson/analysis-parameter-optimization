# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    float_0 = 5188.03
    module_0.to_namedtuple(float_0)


def test_case_1():
    int_0 = 128
    tuple_0 = (int_0,)
    list_0 = [tuple_0, tuple_0, int_0, int_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_2():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_4():
    bytes_0 = b"\x1d\xf3\xeew<\x91\t\x7f:B"
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_7():
    str_0 = "C"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_1)


def test_case_8():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_9():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_10():
    bytes_0 = b"\x1f\x88\xf9\x8b\x1c\xff\xc3\xc4vh"
    dict_0 = {bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_11():
    str_0 = " Cannot be a builtin name."
    str_1 = "C"
    dict_0 = {str_0: str_0, str_1: str_1, str_1: str_1, str_0: str_1}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_12():
    str_0 = "C\x0b"
    str_1 = "bi7SlG{:p7\x0bO$w["
    dict_0 = {
        str_0: str_0,
        str_1: str_1,
        str_0: str_0,
        str_0: str_1,
        str_1: str_1,
        str_1: str_1,
    }
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    bool_0 = True
    tuple_0 = (ordered_dict_0, str_0, bool_0, ordered_dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    bool_1 = False
    dict_1 = {bool_1: bool_1}
    tuple_1 = ()
    var_1 = module_0.to_namedtuple(dict_1)
    var_2 = module_0.to_namedtuple(var_0)
    var_3 = module_0.to_namedtuple(tuple_1)
    module_0.to_namedtuple(bool_0)
