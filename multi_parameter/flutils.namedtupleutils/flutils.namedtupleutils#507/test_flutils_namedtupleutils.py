# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1
import builtins as module_2


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_2():
    str_0 = "jPH"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    bytes_0 = b"\xb0\x9b\xc07k\xc9\\\xd4\xa8\xce\xd0\x8a\x86\xdec"
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    list_0 = [dict_0, dict_0]
    var_0 = module_0.to_namedtuple(list_0)
    module_0.to_namedtuple(bool_0)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    dict_0 = {}
    object_0 = module_2.object(**dict_0)
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_9():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_10():
    bytes_0 = b"q\xcc\x1e\xe02\xe0Us\x9e\xd6\xe9,x\xb6q\x85Q\xca\x15\xe0"
    tuple_0 = (bytes_0, bytes_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    dict_0 = {tuple_0: tuple_0, bytes_0: bytes_0}
    var_1 = module_0.to_namedtuple(tuple_0)
    module_0.to_namedtuple(dict_0)


def test_case_11():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    var_2 = module_0.to_namedtuple(var_0)
    var_3 = module_0.to_namedtuple(var_1)
    var_4 = module_0.to_namedtuple(tuple_0)
    var_5 = module_0.to_namedtuple(var_0)
    str_0 = 'SO&JE"-E'
    var_6 = module_0.to_namedtuple(var_0)
    tuple_1 = (str_0, str_0)
    bool_0 = False
    var_7 = module_0.to_namedtuple(tuple_0)
    dict_0 = {tuple_1: str_0, tuple_1: bool_0, str_0: str_0, tuple_1: bool_0}
    var_8 = module_0.to_namedtuple(var_1)
    var_9 = module_0.to_namedtuple(dict_0)
    var_10 = module_0.to_namedtuple(dict_0)
    tuple_2 = ()
    tuple_3 = ()
    var_11 = module_0.to_namedtuple(tuple_3)
    var_12 = module_0.to_namedtuple(tuple_2)
    var_13 = module_0.to_namedtuple(var_10)
    var_14 = module_0.to_namedtuple(var_10)
    var_15 = module_0.to_namedtuple(dict_0)
    var_16 = module_0.to_namedtuple(tuple_2)
    module_0.to_namedtuple(bool_0)


def test_case_12():
    str_0 = "IZvteu4n "
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_1)
    module_0.to_namedtuple(str_0)
