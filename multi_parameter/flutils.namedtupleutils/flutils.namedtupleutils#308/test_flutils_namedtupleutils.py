# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    float_0 = 2152.56059
    module_0.to_namedtuple(float_0)


def test_case_1():
    complex_0 = 1113 - 1703.5j
    str_0 = "pL"
    dict_0 = {
        complex_0: str_0,
        complex_0: str_0,
        str_0: complex_0,
        str_0: str_0,
        str_0: complex_0,
    }
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_2():
    complex_0 = 1113 - 1703.5j
    str_0 = "pL"
    dict_0 = {complex_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    bytes_0 = b"\xd4ql\x0fn\xc5"
    module_0.to_namedtuple(bytes_0)


def test_case_4():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_5():
    bytes_0 = b"\xe1\x0c\x8d\x85\x19\xb1\xaf"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_6():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_7():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(var_0)
    tuple_0 = (var_1, var_0, var_0, var_1)
    var_2 = module_0.to_namedtuple(tuple_0)


def test_case_8():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_9():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_10():
    str_0 = "^xE`{l'6V+wht5F?"
    float_0 = -1425.0
    dict_0 = {str_0: str_0, str_0: float_0, str_0: float_0, float_0: float_0}
    tuple_0 = (str_0, dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    bytes_0 = b"\xc6\xe6)\x99x\x92\xcd\xe6\xbd\x0fyyz+\x1e\xfcn"
    module_1.namedtuple(bytes_0, bytes_0)


def test_case_11():
    complex_0 = 1113 - 1703.5j
    str_0 = "cv\t"
    dict_0 = {complex_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_1)
    ordered_dict_0 = module_0.to_namedtuple(var_0)
    list_0 = [ordered_dict_0, var_1, ordered_dict_0]
    var_3 = module_0.to_namedtuple(ordered_dict_0)
    tuple_0 = (list_0, var_0, var_3)
    var_4 = module_0.to_namedtuple(tuple_0)
    var_5 = module_0.to_namedtuple(var_3)
    module_1.namedtuple(var_3, var_0, rename=var_5, defaults=var_2, module=var_3)
