# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1
import builtins as module_2


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    int_0 = 70
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_1)
    var_3 = module_1.OrderedDict()
    var_4 = module_0.to_namedtuple(var_1)
    module_0.to_namedtuple(int_0)


def test_case_2():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    bytes_0 = b"ob\xe2\x12\x17\x08\xfd^\xaf\xe5\xeaM{\xdc\x84\xd0\xaa\xb0\xd2"
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    str_0 = "K"
    list_0 = [str_0, str_0, str_0]
    dict_0 = {str_0: list_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    str_0 = "K"
    list_0 = [str_0, str_0, str_0]
    dict_0 = {str_0: list_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_9():
    str_0 = "+&?\r<NAb\nkO2J\n"
    dict_0 = {str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    int_0 = 949
    module_0.to_namedtuple(int_0)


def test_case_10():
    str_0 = "+&?\r<NAb\nkJ\n"
    dict_0 = {str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_0.to_namedtuple(dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_1.OrderedDict()


def test_case_11():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_12():
    bytes_0 = b'\xaa\xa5\xb4\x1d\xe6\xec\xa2\x9e}\x8a\x01\xfa"\xd4\xf0_\xb3\xde\x13\xa2'
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)
    dict_0 = {bytes_0: list_0}
    module_0.to_namedtuple(dict_0)


def test_case_13():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    str_0 = "K\x0c"
    list_0 = [str_0, str_0, str_0]
    var_2 = module_0.to_namedtuple(list_0)
    var_3 = module_0.to_namedtuple(list_0)
    dict_0 = {str_0: list_0}
    var_4 = module_0.to_namedtuple(dict_0)
    object_0 = module_2.object()
    var_5 = module_1.OrderedDict()
    var_6 = module_0.to_namedtuple(var_0)
    object_1 = module_2.object()
    var_7 = module_0.to_namedtuple(var_4)
    module_0.to_namedtuple(object_0)
