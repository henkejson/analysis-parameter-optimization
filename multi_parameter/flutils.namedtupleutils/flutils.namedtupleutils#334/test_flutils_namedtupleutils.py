# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1
import builtins as module_2


def test_case_0():
    bool_0 = False
    module_0.to_namedtuple(bool_0)


def test_case_1():
    int_0 = 1074
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)
    list_0 = [var_0, int_0, var_0, var_0, var_0]
    var_1 = module_0.to_namedtuple(list_0)
    module_0.to_namedtuple(int_0)


def test_case_2():
    int_0 = 1074
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = '^0\x0cPG7n,?jprG";m'
    module_0.to_namedtuple(str_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_7():
    str_0 = "name"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_9():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_1)


def test_case_10():
    int_0 = 1074
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    str_0 = "\x0b~xmyr1RS\x0cf8}CotW@13"
    dict_1 = {var_0: str_0, str_0: str_0}
    var_2 = module_0.to_namedtuple(dict_1)


def test_case_11():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    int_0 = 1063
    var_1 = module_0.to_namedtuple(var_0)
    object_0 = module_2.object(*var_1)
    list_0 = [object_0, int_0, object_0, object_0, object_0]
    var_2 = module_0.to_namedtuple(list_0)
    var_3 = module_0.to_namedtuple(list_0)
    str_0 = "\x0chown"
    dict_0 = {object_0: str_0, str_0: str_0}
    var_4 = module_0.to_namedtuple(dict_0)
    var_5 = module_0.to_namedtuple(var_4)
    object_1 = module_2.object()


def test_case_12():
    bytes_0 = b"\x87_\xa5\x00\xab\x95"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)
