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
    str_0 = ""
    list_0 = [bool_0, str_0, str_0, bool_0]
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(list_0)


def test_case_2():
    str_0 = "wHR8S"
    dict_0 = {str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = "}[_yj]3\\V#;dS"
    module_0.to_namedtuple(str_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    object_0 = module_2.object(*var_0)
    module_0.to_namedtuple(bool_0)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    bytes_0 = b"\xce\x93\x9f\xba%\xad\xa8\x04q\x94\nw\xc1\x08\x88>j"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_9():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_10():
    str_0 = "wHR8S"
    str_1 = "uh,P"
    dict_0 = {str_0: str_1, str_1: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_11():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_12():
    bytes_0 = b"\xa6U\xb9\x8cb\xa97"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_13():
    str_0 = "ty,)C\"fST<)'xN&u"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    list_0 = []
    var_1 = module_0.to_namedtuple(list_0)
    var_2 = module_0.to_namedtuple(list_0)
    str_1 = "wHR8 "
    var_3 = module_0.to_namedtuple(var_0)
    str_2 = "uh,P"
    dict_1 = {str_1: dict_0, str_2: str_1}
    var_4 = module_0.to_namedtuple(dict_1)
    ordered_dict_0 = module_1.OrderedDict(**dict_1)
    var_5 = module_0.to_namedtuple(ordered_dict_0)
    var_6 = module_0.to_namedtuple(dict_0)
    list_1 = [dict_1, var_5, str_2, dict_0, dict_1]
    var_7 = module_0.to_namedtuple(list_1)
    var_8 = module_0.to_namedtuple(dict_0)
    var_9 = module_0.to_namedtuple(var_1)
    var_10 = module_0.to_namedtuple(var_2)
