# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    complex_0 = 445 + 1444.7992j
    module_0.to_namedtuple(complex_0)


def test_case_1():
    bool_0 = True
    tuple_0 = (bool_0,)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_1)


def test_case_2():
    str_0 = "V"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    bytes_0 = b"\n5\xaf\x9caQ\xd7Lnl\x1e*?\xb7H\x8f\xdfgg"
    module_0.to_namedtuple(bytes_0)


def test_case_4():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_5():
    complex_0 = -683.67 + 1561.4j
    bool_0 = False
    dict_0 = {complex_0: bool_0, complex_0: complex_0}
    list_0 = [dict_0, dict_0, bool_0]
    var_0 = module_0.to_namedtuple(list_0)
    tuple_0 = ()
    var_1 = module_0.to_namedtuple(tuple_0)
    var_2 = module_0.to_namedtuple(tuple_0)
    var_3 = module_0.to_namedtuple(tuple_0)
    var_4 = module_0.to_namedtuple(var_2)
    module_0.to_namedtuple(complex_0)


def test_case_6():
    str_0 = ""
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    tuple_0 = (dict_0, str_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_1.OrderedDict()
    bool_0 = False
    var_2 = module_0.to_namedtuple(dict_0)
    var_3 = module_1.OrderedDict(**var_1)
    var_4 = module_0.to_namedtuple(var_1)
    var_5 = module_0.to_namedtuple(var_2)
    module_0.to_namedtuple(bool_0)


def test_case_7():
    str_0 = ""
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    list_0 = []
    tuple_0 = (dict_0, str_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(dict_0)
    bool_0 = False
    var_2 = module_0.to_namedtuple(dict_0)
    var_3 = module_0.to_namedtuple(list_0)
    var_4 = module_0.to_namedtuple(var_1)
    var_5 = module_0.to_namedtuple(var_2)
    module_0.to_namedtuple(bool_0)


def test_case_8():
    bytes_0 = b"\x0c\xe8-\xcd\xf3M\x19\x93\xe1\x7f\x18\x165"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    bool_0 = True
    list_0 = [dict_0, bytes_0, bytes_0, bool_0]
    module_0.to_namedtuple(list_0)


def test_case_9():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_10():
    str_0 = "W "
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    list_0 = []
    tuple_0 = module_0.to_namedtuple(list_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_0.to_namedtuple(tuple_0)
    var_3 = module_0.to_namedtuple(var_2)
    bool_0 = False
    var_4 = module_0.to_namedtuple(var_0)
    module_0.to_namedtuple(bool_0)
