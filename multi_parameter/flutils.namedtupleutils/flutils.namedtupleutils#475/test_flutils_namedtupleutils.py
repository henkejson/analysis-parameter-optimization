# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1
import builtins as module_2


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    str_0 = "[R@\tZ:od1w"
    bool_0 = False
    tuple_0 = (str_0, bool_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    str_0 = "aID"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_4():
    str_0 = "T8umOs^w\\\x0cGoCWma!*!_"
    module_0.to_namedtuple(str_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    bytes_0 = b"\xf97\xc2Q\x19"
    tuple_0 = (bool_0, dict_0, bytes_0)
    tuple_1 = (bool_0, tuple_0, bytes_0)
    list_0 = [tuple_1, bytes_0, dict_0, dict_0]
    bool_1 = False
    list_1 = [list_0, bool_1, bytes_0]
    list_2 = [list_1, list_0]
    var_0 = module_0.to_namedtuple(list_2)
    int_0 = -326
    dict_1 = {}
    var_1 = module_0.to_namedtuple(dict_1)
    module_0.to_namedtuple(int_0)


def test_case_7():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_8():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_9():
    str_0 = "T8umOs^w\\\x0cGoCWma!*!_"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    list_0 = [ordered_dict_0, str_0, ordered_dict_0, str_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_10():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_11():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)
    list_0 = [dict_0, dict_0]
    var_1 = module_0.to_namedtuple(list_0)


def test_case_12():
    str_0 = "\x0cH"
    str_1 = "t8vO9yppdP`A%&u!\x0b5"
    str_2 = "uI}B?*&'w\x0cTiMiqr4u"
    dict_0 = {str_0: str_0, str_1: str_1, str_1: str_1, str_2: str_1}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_13():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    bytes_0 = b"\xf97\xc2Q\x19"
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_2.object()
    dict_1 = {bytes_0: bool_0}
    module_0.to_namedtuple(dict_1)
