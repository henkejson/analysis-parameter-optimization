# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    set_0 = set()
    module_0.to_namedtuple(set_0)


def test_case_1():
    int_0 = -142
    int_1 = 5
    tuple_0 = (int_0, int_1)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    int_0 = -2201
    bool_0 = False
    dict_0 = {int_0: bool_0, int_0: int_0, int_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    bytes_0 = b"\x02hE.\xd3"
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    str_0 = "author_email"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    bytes_0 = b"Wu\xb4Zy\xbf"
    ordered_dict_0 = module_1.OrderedDict()
    list_0 = [bytes_0, bytes_0, ordered_dict_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_9():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_10():
    int_0 = 6
    tuple_0 = (int_0, int_0)
    bytes_0 = b"(\xf6\xed\x10\x8c\xf4\xdf\xb6"
    dict_0 = {bytes_0: tuple_0}
    module_0.to_namedtuple(dict_0)


def test_case_11():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_12():
    str_0 = 'oZ "h2dn|0Qtg'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    bool_0 = True
    tuple_0 = module_0.to_namedtuple(dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_0.to_namedtuple(var_1)
    var_3 = module_0.to_namedtuple(var_1)
    dict_1 = {var_1: bool_0}
    var_4 = module_0.to_namedtuple(tuple_0)
    var_5 = module_0.to_namedtuple(dict_1)
    var_6 = module_0.to_namedtuple(var_4)


def test_case_13():
    str_0 = "A8\r"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    bytes_0 = b"n\xe7S\x03"
    tuple_0 = (dict_0, bytes_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    bytes_1 = b"(\xf6\xed\x10\x8c\xf4\xdf\xb6"
    module_0.to_namedtuple(bytes_1)
