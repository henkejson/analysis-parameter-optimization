# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    bool_0 = True
    module_0.to_namedtuple(bool_0)


def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_2():
    str_0 = "qr"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_4():
    bytes_0 = b"81\xd5\xe8\xfc\xb2\xdd^\x8a\xaa\xf8P\x04L\xf1hsl"
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    complex_0 = 653.178 - 3225j
    dict_0 = {complex_0: complex_0}
    var_0 = module_0.to_namedtuple(dict_0)
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_7():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_8():
    str_0 = "chown"
    bytes_0 = b"\x83O\x97\x94h\xe3\xb3\xd5\xfd\xa4\xfbR\x16\xa58i\x18"
    str_1 = "t%Z{9\rl(c"
    dict_0 = {str_0: bytes_0, str_1: bytes_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_9():
    bytes_0 = b"H|i\xcc\xe8Bx\xc7U\xea\xdd\x88"
    dict_0 = {bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_10():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_11():
    str_0 = "3/18~h;"
    dict_0 = {str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    list_0 = [ordered_dict_0, dict_0]
    tuple_0 = (list_0,)
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    tuple_1 = ()
    var_2 = module_0.to_namedtuple(tuple_1)
    var_3 = module_0.to_namedtuple(list_0)
    var_4 = module_0.to_namedtuple(tuple_1)
    var_5 = module_0.to_namedtuple(var_4)
    var_6 = module_0.to_namedtuple(var_0)
    var_7 = module_0.to_namedtuple(var_0)
    var_8 = module_0.to_namedtuple(tuple_1)


def test_case_12():
    str_0 = "iV\r"
    none_type_0 = None
    dict_0 = {
        str_0: none_type_0,
        str_0: none_type_0,
        str_0: none_type_0,
        str_0: none_type_0,
    }
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(dict_0)
    list_0 = [var_1, var_1, none_type_0, none_type_0]
    var_2 = module_0.to_namedtuple(list_0)
    var_3 = module_0.to_namedtuple(var_1)
    module_1.namedtuple(none_type_0, str_0)
