# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import builtins as module_1
import collections as module_2


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    object_0 = module_1.object()
    dict_0 = {object_0: object_0}
    tuple_0 = (object_0, dict_0, dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    object_0 = module_1.object()
    dict_0 = {object_0: object_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_2.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = "author_email"
    module_0.to_namedtuple(str_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    str_0 = "G}E9&Frc\\xLD4'\r}`"
    tuple_0 = ()
    bytes_0 = b"\x00\x19\xab\xa8\xd2\x90\x83w\x9b\xbf3h\xd5<\x0e\xc9"
    dict_0 = {str_0: tuple_0, str_0: tuple_0, tuple_0: bytes_0, bytes_0: str_0}
    tuple_1 = (str_0, bytes_0, tuple_0, dict_0)
    module_0.to_namedtuple(tuple_1)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    ordered_dict_0 = module_2.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_9():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_10():
    dict_0 = {}
    list_0 = [dict_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_11():
    ordered_dict_0 = module_2.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    str_0 = "izF"
    dict_0 = {var_1: ordered_dict_0, var_1: var_1, str_0: var_1}
    var_2 = module_0.to_namedtuple(var_0)
    var_3 = module_0.to_namedtuple(dict_0)
    var_4 = module_0.to_namedtuple(var_3)
    var_5 = module_0.to_namedtuple(var_3)


def test_case_12():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)
    ordered_dict_0 = module_2.OrderedDict()
    var_1 = module_0.to_namedtuple(ordered_dict_0)
    ordered_dict_1 = module_2.OrderedDict()
    var_2 = module_0.to_namedtuple(ordered_dict_0)
    tuple_0 = (var_2,)
    var_3 = module_0.to_namedtuple(var_2)
    str_0 = "\nzF"
    var_4 = module_0.to_namedtuple(tuple_0)
    dict_0 = {tuple_0: str_0, str_0: tuple_0}
    var_5 = module_0.to_namedtuple(var_2)
    var_6 = module_0.to_namedtuple(tuple_0)
    var_7 = module_0.to_namedtuple(dict_0)
    var_8 = module_0.to_namedtuple(var_2)
    var_9 = module_0.to_namedtuple(var_8)
    var_10 = module_0.to_namedtuple(tuple_0)
    var_11 = module_0.to_namedtuple(var_7)
    var_12 = module_0.to_namedtuple(var_2)
    var_13 = module_0.to_namedtuple(var_12)
    module_2.namedtuple(str_0, var_5, defaults=var_8, module=var_11)
