# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import builtins as module_1
import collections as module_2


def test_case_0():
    bool_0 = True
    module_0.to_namedtuple(bool_0)


def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.to_namedtuple(list_0)
    object_0 = module_1.object()
    module_0.to_namedtuple(object_0)


def test_case_2():
    bytes_0 = b"f\x83g"
    dict_0 = {bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_3():
    str_0 = "HHHH"
    list_0 = [str_0, str_0, str_0, str_0]
    dict_0 = {str_0: list_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_4():
    bytes_0 = b"\xba\xc7\xef\xa5"
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    int_0 = 4
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
    set_0 = set()
    tuple_0 = (int_0, int_0, dict_0, set_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    module_0.to_namedtuple(int_0)


def test_case_7():
    str_0 = "\x0bX4[7"
    list_0 = [str_0, str_0, str_0, str_0]
    dict_0 = {str_0: list_0, str_0: str_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_2.OrderedDict(**dict_0)
    tuple_0 = (ordered_dict_0,)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)
    bool_0 = True
    module_0.to_namedtuple(bool_0)


def test_case_8():
    str_0 = "HHHH"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_2.OrderedDict(**dict_0)
    tuple_0 = (ordered_dict_0,)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_0)
    var_3 = module_0.to_namedtuple(var_2)
    var_4 = module_0.to_namedtuple(var_2)
    var_5 = module_0.to_namedtuple(var_1)


def test_case_9():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_10():
    str_0 = "\nHHh"
    list_0 = [str_0, str_0, str_0, str_0]
    dict_0 = {str_0: list_0, str_0: str_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_2.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(dict_0)
    module_1.object(**var_0)
