# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import builtins as module_0
import flutils.namedtupleutils as module_1
import collections as module_2


def test_case_0():
    object_0 = module_0.object()
    module_1.to_namedtuple(object_0)


def test_case_1():
    ordered_dict_0 = module_2.OrderedDict()
    var_0 = module_1.to_namedtuple(ordered_dict_0)
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_1 = module_1.to_namedtuple(var_0)
    var_2 = module_1.to_namedtuple(list_0)
    module_1.to_namedtuple(bool_0)


def test_case_2():
    str_0 = "O"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_1.to_namedtuple(dict_0)
    var_1 = module_1.to_namedtuple(var_0)


def test_case_3():
    ordered_dict_0 = module_2.OrderedDict()
    var_0 = module_1.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = "\x0cvv7]JF{"
    module_1.to_namedtuple(str_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_1.to_namedtuple(tuple_0)


def test_case_6():
    int_0 = -1581
    list_0 = [int_0, int_0]
    str_0 = "CompletedProcess"
    dict_0 = {str_0: list_0, str_0: int_0, str_0: int_0}
    ordered_dict_0 = module_2.OrderedDict(**dict_0)
    var_0 = module_1.to_namedtuple(ordered_dict_0)
    dict_1 = {int_0: list_0}
    var_1 = module_1.to_namedtuple(var_0)
    var_2 = module_1.to_namedtuple(var_0)
    var_3 = module_1.to_namedtuple(dict_1)
    var_4 = module_1.to_namedtuple(dict_1)


def test_case_7():
    dict_0 = {}
    var_0 = module_1.to_namedtuple(dict_0)


def test_case_8():
    dict_0 = {}
    var_0 = module_1.to_namedtuple(dict_0)
    var_1 = module_1.to_namedtuple(var_0)


def test_case_9():
    list_0 = []
    var_0 = module_1.to_namedtuple(list_0)


def test_case_10():
    str_0 = "O"
    list_0 = [str_0, str_0]
    dict_0 = {str_0: str_0, str_0: list_0, str_0: str_0, str_0: list_0}
    ordered_dict_0 = module_2.OrderedDict(**dict_0)
    var_0 = module_1.to_namedtuple(ordered_dict_0)


def test_case_11():
    bytes_0 = b"\xef<(\x1c\n9-\xe1\x91\x9b\xc4\xd2\xea\xb6l"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    module_1.to_namedtuple(dict_0)


def test_case_12():
    str_0 = "%i&\x0b+:`;"
    str_1 = "O"
    list_0 = [str_1, str_0]
    dict_0 = {str_0: str_0, str_1: list_0, str_0: str_0, str_0: list_0}
    ordered_dict_0 = module_2.OrderedDict(**dict_0)
    var_0 = module_1.to_namedtuple(ordered_dict_0)


def test_case_13():
    ordered_dict_0 = module_2.OrderedDict()
    list_0 = [ordered_dict_0]
    var_0 = module_1.to_namedtuple(list_0)
    int_0 = -1581
    list_1 = [int_0, int_0]
    str_0 = "aSBO\x0c"
    dict_0 = {str_0: list_1, str_0: var_0, str_0: var_0}
    ordered_dict_1 = module_2.OrderedDict(**dict_0)
    var_1 = module_1.to_namedtuple(ordered_dict_1)
    dict_1 = {int_0: list_1}
    var_2 = module_1.to_namedtuple(var_1)
    var_3 = module_1.to_namedtuple(list_0)
    var_4 = module_1.to_namedtuple(var_0)
    var_5 = module_1.to_namedtuple(dict_1)
    var_6 = module_1.to_namedtuple(list_1)
    module_1.to_namedtuple(int_0)
