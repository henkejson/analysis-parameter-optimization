# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    bool_0 = False
    module_0.to_namedtuple(bool_0)


def test_case_1():
    int_0 = 4282
    list_0 = [int_0]
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(list_0)


def test_case_2():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_3():
    bytes_0 = b"\xcf\xd7\x95\x0b9-\x86\xf1u\xc9/j\x80-/\xc6"
    module_0.to_namedtuple(bytes_0)


def test_case_4():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_5():
    str_0 = "is_list_like"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_6():
    str_0 = "is_list_like"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_7():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(ordered_dict_0)
    var_2 = module_0.to_namedtuple(var_0)
    var_3 = module_0.to_namedtuple(var_1)
    var_4 = module_0.to_namedtuple(var_2)


def test_case_8():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_9():
    str_0 = "attr_map"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict()
    tuple_0 = (dict_0, ordered_dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_10():
    bool_0 = False
    list_0 = [bool_0]
    str_0 = ":\x0bBKpN<k`nB\x0c:L"
    str_1 = ",M"
    dict_0 = {str_1: list_0, str_0: str_0, str_1: str_1, str_1: str_1}
    var_0 = module_0.to_namedtuple(dict_0)
    module_0.to_namedtuple(str_1)


def test_case_11():
    bytes_0 = b"!\xf6\x93\x91\xb2i\xef\xce\xa9v\xa4\x01k"
    bool_0 = False
    dict_0 = {bytes_0: bool_0, bool_0: bool_0}
    list_0 = [dict_0, dict_0, bool_0, bytes_0]
    module_0.to_namedtuple(list_0)


def test_case_12():
    bool_0 = True
    list_0 = [bool_0]
    str_0 = ":\x0bBKpN<k`nB\x0c:L"
    dict_0 = {str_0: list_0, str_0: str_0, bool_0: bool_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    module_0.to_namedtuple(bool_0)


def test_case_13():
    str_0 = "is_list_like6 "
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    bool_0 = True
    list_0 = [bool_0]
    str_1 = ":\x0bBKp<k`nB\x0c:L"
    dict_1 = {str_1: list_0, str_1: str_1, bool_0: bool_0, str_1: str_1}
    ordered_dict_1 = module_1.OrderedDict(**dict_1)
    bool_1 = False
    var_1 = module_0.to_namedtuple(var_0)
    tuple_0 = (ordered_dict_1, bool_1)
    tuple_1 = (list_0, list_0, bool_0, tuple_0)
    var_2 = module_0.to_namedtuple(tuple_1)
    bool_2 = True
    list_1 = [bool_2, str_1, var_2]
    var_3 = module_0.to_namedtuple(list_1)
    module_0.to_namedtuple(str_1)
