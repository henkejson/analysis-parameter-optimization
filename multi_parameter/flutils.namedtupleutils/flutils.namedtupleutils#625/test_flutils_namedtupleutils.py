# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    complex_0 = 1764.688 - 337.8j
    module_0.to_namedtuple(complex_0)


def test_case_1():
    bool_0 = False
    str_0 = "Y<<O4!k2y[M _[x;G"
    set_0 = {bool_0}
    tuple_0 = (bool_0, bool_0, str_0, set_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    str_0 = "subsequent_indent_len"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    bytes_0 = b"\xc6\r\x8fO,\x19\xd7S\x0b\xf7\xfc\x82[\xe3\xfbK\xa8/"
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    str_0 = "subsequent_indent_len"
    str_1 = ":b0.G;"
    bool_0 = False
    dict_0 = {str_0: str_0, str_1: bool_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_7():
    dict_0 = {}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_9():
    str_0 = "subsequent_indent_len"
    bool_0 = False
    dict_0 = {str_0: str_0, bool_0: bool_0}
    list_0 = [bool_0, bool_0, dict_0, bool_0]
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(list_0)
    var_2 = module_0.to_namedtuple(var_0)
    module_0.to_namedtuple(bool_0)


def test_case_10():
    bool_0 = True
    bytes_0 = b"$\xe3\xabj\xb0\x1f\xb3\x9f\xa0"
    dict_0 = {bytes_0: bytes_0}
    tuple_0 = (bool_0, bytes_0, dict_0)
    module_0.to_namedtuple(tuple_0)


def test_case_11():
    set_0 = set()
    tuple_0 = (set_0,)
    var_0 = module_0.to_namedtuple(tuple_0)
    str_0 = "subsKqulnt_indent_l\x0c"
    str_1 = ":b0.G;"
    bool_0 = False
    dict_0 = {str_0: str_0, str_1: bool_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    list_0 = [ordered_dict_0, bool_0, var_0, dict_0, ordered_dict_0]
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_0.to_namedtuple(list_0)
    var_3 = module_0.to_namedtuple(var_1)
    var_4 = module_0.to_namedtuple(var_3)
