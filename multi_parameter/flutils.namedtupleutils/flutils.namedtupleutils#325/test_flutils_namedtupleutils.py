# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    set_0 = set()
    module_0.to_namedtuple(set_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_1)


def test_case_2():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_3():
    bytes_0 = b"\xe2#g\xa8\x1d\xf8-\xaf!}\xcf\x0f\xd6\x05\x9b\xff\xa4!F"
    module_0.to_namedtuple(bytes_0)


def test_case_4():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_5():
    str_0 = "ceatx_module"
    dict_0 = {
        str_0: str_0,
        str_0: str_0,
        str_0: str_0,
        str_0: str_0,
        str_0: str_0,
        str_0: str_0,
    }
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_6():
    str_0 = "Rf88A@"
    float_0 = 48.438866
    dict_0 = {str_0: str_0, str_0: float_0, float_0: float_0}
    list_0 = [dict_0, dict_0]
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_7():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_8():
    str_0 = "Rf88A@"
    float_0 = 55.938599377188126
    dict_0 = {str_0: str_0, str_0: float_0, float_0: float_0}
    list_0 = [dict_0, dict_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_9():
    str_0 = "crate_modul\t"
    float_0 = 48.438866
    dict_0 = {str_0: str_0, str_0: float_0, float_0: float_0}
    list_0 = [dict_0, dict_0]
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(list_0)
    var_2 = module_1.OrderedDict()


def test_case_10():
    bytes_0 = b"\x1a\x8e\\\x93\xfc]\xa2p5\xcc\xf8\xe0?\xa0k\xd5\x9b\xcb\xb3"
    dict_0 = {bytes_0: bytes_0}
    list_0 = [dict_0]
    ordered_dict_0 = module_1.OrderedDict(*list_0)
    module_0.to_namedtuple(dict_0)
