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
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)
    tuple_0 = (bool_0, dict_0, bool_0, bool_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    var_2 = module_0.to_namedtuple(var_1)
    module_0.to_namedtuple(bool_0)


def test_case_2():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = "P>G["
    module_0.to_namedtuple(str_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    str_0 = "description"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_7():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(ordered_dict_0)


def test_case_8():
    str_0 = "h:x"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    module_1.namedtuple(ordered_dict_0, str_0)


def test_case_9():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_10():
    str_0 = "description"
    dict_0 = {str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    tuple_0 = (ordered_dict_0,)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_11():
    str_0 = "\nXr"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_0.to_namedtuple(dict_0)
    var_3 = module_0.to_namedtuple(var_0)
    var_4 = module_0.to_namedtuple(var_0)
    list_0 = []
    var_5 = module_0.to_namedtuple(list_0)
    var_6 = module_0.to_namedtuple(var_5)
    var_7 = module_0.to_namedtuple(var_5)
    var_8 = module_2.object()
    none_type_0 = None
    var_9 = module_0.to_namedtuple(dict_0)
    var_10 = module_0.to_namedtuple(list_0)
    var_11 = module_0.to_namedtuple(var_5)
    module_0.to_namedtuple(none_type_0)


def test_case_12():
    bytes_0 = b"R\\\x1d5\xf3\xdd"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    tuple_0 = (bytes_0, dict_0)
    list_0 = [tuple_0, tuple_0]
    module_0.to_namedtuple(list_0)
