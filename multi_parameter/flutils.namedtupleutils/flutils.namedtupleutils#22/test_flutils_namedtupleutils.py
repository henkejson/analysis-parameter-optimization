# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    bool_0 = True
    module_0.to_namedtuple(bool_0)


def test_case_1():
    dict_0 = {}
    bool_0 = True
    var_0 = module_0.to_namedtuple(dict_0)
    list_0 = [dict_0, bool_0]
    var_1 = module_0.to_namedtuple(list_0)


def test_case_2():
    str_0 = "url"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    bytes_0 = b"h\x9f;b\xceZJi\x0e"
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    bool_0 = True
    bool_1 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_1}
    dict_1 = {bool_0: bool_0, bool_0: bool_0, bool_0: dict_0}
    list_0 = [dict_1]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_9():
    list_0 = []
    list_1 = [list_0, list_0, list_0, list_0]
    var_0 = module_0.to_namedtuple(list_1)


def test_case_10():
    str_0 = "url"
    str_1 = "^tAnH"
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1, str_0: str_1}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(dict_0)
    var_3 = module_0.to_namedtuple(ordered_dict_0)
    module_0.to_namedtuple(str_1)


def test_case_11():
    bytes_0 = b"\xa8\xc6\x97\x0f<\x1c$i\xe6"
    dict_0 = {bytes_0: bytes_0}
    complex_0 = -606 - 319.6j
    tuple_0 = (dict_0, complex_0)
    module_0.to_namedtuple(tuple_0)


def test_case_12():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    object_0 = module_1.OrderedDict(*var_0)
    var_1 = module_0.to_namedtuple(var_0)
    list_0 = [ordered_dict_0, ordered_dict_0]
    tuple_0 = module_0.to_namedtuple(var_1)
    tuple_1 = (list_0, tuple_0, tuple_0, list_0)
    var_2 = module_0.to_namedtuple(tuple_1)
    str_0 = "\nrl"
    str_1 = "^tAnH"
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1, var_1: str_1}
    ordered_dict_1 = module_1.OrderedDict(**dict_0)
    var_3 = module_0.to_namedtuple(list_0)
    var_4 = module_0.to_namedtuple(dict_0)
    var_5 = module_0.to_namedtuple(ordered_dict_1)
    ordered_dict_2 = module_1.OrderedDict(*ordered_dict_0)
    var_6 = module_0.to_namedtuple(dict_0)
    ordered_dict_3 = module_1.OrderedDict()
    module_0.to_namedtuple(str_1)
