# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    float_0 = 1198.593917
    module_0.to_namedtuple(float_0)


def test_case_1():
    bool_0 = False
    str_0 = "$7fbM]Scxr\x0c"
    tuple_0 = (bool_0, bool_0, str_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    bytes_0 = b"\xde!)z\xf8XqH\xab("
    module_0.to_namedtuple(bytes_0)


def test_case_4():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_5():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_6():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_7():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_8():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_9():
    float_0 = 2048.8911871529012
    str_0 = "create_module"
    dict_0 = {str_0: float_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_10():
    str_0 = "name=%r package=%r"
    str_1 = "%_{Ad*2O16nzNR"
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    list_0 = [ordered_dict_0]
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(ordered_dict_0)


def test_case_11():
    bytes_0 = b"\xc0\xb1rc\x07#V\x89\xf1\xc3"
    dict_0 = {bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_12():
    float_0 = 2048.8911871529012
    str_0 = "create_module"
    dict_0 = {str_0: float_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
