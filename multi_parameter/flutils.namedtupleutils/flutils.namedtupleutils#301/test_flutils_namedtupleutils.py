# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    bool_0 = True
    list_0 = []
    ordered_dict_0 = module_1.OrderedDict(*list_0)
    list_1 = [bool_0, ordered_dict_0, ordered_dict_0]
    var_0 = module_0.to_namedtuple(list_1)


def test_case_2():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = "I"
    module_0.to_namedtuple(str_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_7():
    str_0 = "x6m"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    ordered_dict_0 = module_1.OrderedDict()
    list_0 = [ordered_dict_0]
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_1)
    module_1.namedtuple(var_1, ordered_dict_0, defaults=var_0)


def test_case_9():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_10():
    str_0 = "46O"
    tuple_0 = (str_0,)
    ordered_dict_0 = module_1.OrderedDict()
    dict_0 = {tuple_0: tuple_0, tuple_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    tuple_1 = (var_0, str_0)
    var_2 = module_0.to_namedtuple(ordered_dict_0)
    var_3 = module_0.to_namedtuple(tuple_1)


def test_case_11():
    bool_0 = True
    set_0 = set()
    bytes_0 = b"\x90e\xc2TD\x92\xe9L\x1f\xea\xf6\xa9\x06\xab\xab"
    dict_0 = {bool_0: set_0, bool_0: bytes_0, bytes_0: bool_0}
    module_0.to_namedtuple(dict_0)


def test_case_12():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(list_0)
    tuple_0 = ()
    var_2 = module_0.to_namedtuple(tuple_0)
    var_3 = module_0.to_namedtuple(var_0)
    var_4 = module_0.to_namedtuple(var_2)
    str_0 = "x6 "
    tuple_1 = (str_0,)
    var_5 = module_0.to_namedtuple(tuple_0)
    var_6 = module_0.to_namedtuple(tuple_1)
    var_7 = module_1.OrderedDict(*list_0)
    ordered_dict_0 = module_1.OrderedDict()
    dict_0 = {tuple_1: tuple_1, tuple_1: str_0, str_0: str_0}
    var_8 = module_0.to_namedtuple(dict_0)
    var_9 = module_0.to_namedtuple(var_8)
    var_10 = module_0.to_namedtuple(ordered_dict_0)
    var_11 = module_0.to_namedtuple(list_0)
    bool_0 = True
    module_0.to_namedtuple(bool_0)
