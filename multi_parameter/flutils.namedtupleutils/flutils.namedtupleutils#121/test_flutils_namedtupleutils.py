# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1
import builtins as module_2


def test_case_0():
    complex_0 = -960.63276 - 1713.655928j
    module_0.to_namedtuple(complex_0)


def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_0)
    list_1 = [var_0, var_0, list_0]
    var_3 = module_0.to_namedtuple(list_1)
    var_4 = module_0.to_namedtuple(list_1)


def test_case_2():
    str_0 = ")Mn+"
    dict_0 = {str_0: str_0}
    object_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_4():
    str_0 = "9N~cHEyV8S93aY1\\z="
    module_0.to_namedtuple(str_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    list_0 = module_0.to_namedtuple(dict_0)
    ordered_dict_0 = module_1.OrderedDict(*list_0)
    var_2 = module_0.to_namedtuple(ordered_dict_0)


def test_case_7():
    str_0 = "n"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    str_0 = ")Mn+"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_9():
    str_0 = "_pG9%q[CtyLcf([_>4A"
    list_0 = [str_0, str_0]
    var_0 = module_0.to_namedtuple(list_0)
    list_1 = [var_0, str_0, list_0]
    str_1 = "0vK\rTW[jF2<3"
    tuple_0 = (list_1, str_1, str_0)
    var_1 = module_0.to_namedtuple(tuple_0)


def test_case_10():
    complex_0 = 474.3 + 1833.7128j
    bool_0 = False
    tuple_0 = (complex_0, bool_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    dict_0 = {var_0: tuple_0, complex_0: bool_0}
    var_1 = module_0.to_namedtuple(dict_0)
    tuple_1 = ()
    var_2 = module_0.to_namedtuple(tuple_1)
    var_3 = module_0.to_namedtuple(tuple_1)
    var_4 = module_0.to_namedtuple(tuple_1)


def test_case_11():
    str_0 = "aZ9w"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_12():
    str_0 = "\x0bL"
    bool_0 = True
    dict_0 = {bool_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_0.to_namedtuple(var_0)
    dict_1 = {str_0: str_0}
    tuple_0 = (dict_1, dict_1)
    list_0 = [tuple_0, str_0]
    var_3 = module_0.to_namedtuple(list_0)
    var_4 = module_0.to_namedtuple(list_0)
    var_5 = module_0.to_namedtuple(dict_1)
    var_6 = module_0.to_namedtuple(var_4)
    var_7 = module_0.to_namedtuple(var_5)
    bool_1 = True
    var_8 = module_0.to_namedtuple(dict_1)
    list_1 = [bool_1, tuple_0, var_8, var_3]
    var_9 = module_0.to_namedtuple(list_1)
    module_0.to_namedtuple(bool_0)


def test_case_13():
    object_0 = module_2.object()
    bool_0 = True
    bytes_0 = b"\xd6\xeb\x9e\xca\xeb\x11n\x95\x85v(C\xa4?f\xa2"
    set_0 = {bool_0, bytes_0}
    dict_0 = {object_0: object_0, bytes_0: bool_0, bool_0: set_0, bool_0: bool_0}
    tuple_0 = (object_0, bool_0, set_0, dict_0)
    module_0.to_namedtuple(tuple_0)
