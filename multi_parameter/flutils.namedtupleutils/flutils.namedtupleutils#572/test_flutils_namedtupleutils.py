# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    int_0 = -1201
    module_0.to_namedtuple(int_0)


def test_case_1():
    int_0 = 3246
    bool_0 = False
    tuple_0 = (int_0, bool_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    str_0 = "S0`zc+yZyFRVr<Pp"
    module_0.to_namedtuple(str_0)


def test_case_4():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_5():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_6():
    str_0 = "encode"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_7():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_9():
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    ordered_dict_0 = module_1.OrderedDict()
    var_2 = module_0.to_namedtuple(var_0)


def test_case_10():
    str_0 = "lGyURG"
    str_1 = "r1c^?56"
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_11():
    bytes_0 = b"\x8c\x04\x1ae\x99C\x82"
    list_0 = [bytes_0]
    bool_0 = False
    tuple_0 = (bytes_0, list_0, bool_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    bytes_1 = b";\x7fo\xe8\xd4\xf2~\xcd1\x86\xe3=\xa0\xe6R"
    dict_0 = {bytes_1: bytes_1, bytes_1: bytes_1, bytes_1: bytes_1, bytes_1: bytes_1}
    module_0.to_namedtuple(dict_0)


def test_case_12():
    str_0 = "\x0bGyRG"
    str_1 = "r1c^?56"
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    bool_0 = False
    tuple_0 = (var_0, bool_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    module_0.to_namedtuple(bool_0)
