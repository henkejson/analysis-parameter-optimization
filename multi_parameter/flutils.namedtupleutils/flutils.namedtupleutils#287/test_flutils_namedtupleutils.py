# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    set_0 = set()
    tuple_0 = (set_0,)
    var_0 = module_0.to_namedtuple(tuple_0)
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_2():
    str_0 = "loadermaintainer"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_4():
    str_0 = "X"
    module_0.to_namedtuple(str_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    int_0 = 1
    dict_0 = {int_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)
    tuple_0 = ()
    var_1 = module_0.to_namedtuple(tuple_0)


def test_case_7():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_8():
    bytes_0 = b"m\xa1\xbb\xdd\xc4E^\x96\xbc"
    list_0 = [bytes_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_9():
    int_0 = 1
    dict_0 = {int_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_0)


def test_case_10():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_11():
    bytes_0 = b"\xbd\x99\xb9\xda9\xde"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_12():
    str_0 = "loadermaintainer"
    str_1 = "4'OKNeWX)O: #\n-X@^CC"
    dict_0 = {str_0: str_0, str_1: str_0, str_0: str_1, str_0: str_1}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    list_0 = [ordered_dict_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_13():
    str_0 = "\t\nYQF1QTS1"
    dict_0 = {str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    module_0.to_namedtuple(str_0)
