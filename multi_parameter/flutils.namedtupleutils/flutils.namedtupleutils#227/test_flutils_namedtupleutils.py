# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    bool_0 = True
    module_0.to_namedtuple(bool_0)


def test_case_1():
    int_0 = 2877
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.to_namedtuple(list_0)
    ordered_dict_0 = module_1.OrderedDict()
    module_1.namedtuple(ordered_dict_0, ordered_dict_0, module=ordered_dict_0)


def test_case_2():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_3():
    str_0 = '"\x0cc\t0ZCgL\x0bG2jcP /'
    module_0.to_namedtuple(str_0)


def test_case_4():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_5():
    str_0 = "!R\nYqGI&>Q)2`ur,Hmfr"
    list_0 = [str_0]
    dict_0 = {str_0: list_0, str_0: list_0}
    tuple_0 = (list_0, str_0, dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_6():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_7():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_8():
    int_0 = -903
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    tuple_0 = (dict_0,)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_9():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_10():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)
    ordered_dict_0 = module_1.OrderedDict(*var_1)
    str_0 = "initialize_options"
    dict_0 = {str_0: var_1, str_0: var_1, str_0: var_1}
    ordered_dict_1 = module_1.OrderedDict(**dict_0)
    list_0 = [var_0, ordered_dict_1]
    var_2 = module_0.to_namedtuple(list_0)
    var_3 = module_0.to_namedtuple(var_2)


def test_case_11():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    dict_0 = {}
    float_0 = 83.847148
    var_2 = module_0.to_namedtuple(var_0)
    var_3 = module_0.to_namedtuple(dict_0)
    list_0 = []
    dict_1 = {var_3: float_0}
    var_4 = module_0.to_namedtuple(dict_1)
    var_5 = module_0.to_namedtuple(list_0)
    var_6 = module_0.to_namedtuple(var_3)
    ordered_dict_0 = module_1.OrderedDict()
    var_7 = module_0.to_namedtuple(var_1)
    var_8 = module_0.to_namedtuple(var_2)
    str_0 = "initialize_options"
    str_1 = "\x0blauqC"
    dict_2 = {var_1: var_8, str_0: var_2, str_1: ordered_dict_0}
    ordered_dict_1 = module_1.OrderedDict(**dict_2)
    list_1 = [float_0, ordered_dict_1]
    var_9 = module_0.to_namedtuple(list_1)
    var_10 = module_0.to_namedtuple(dict_0)
    list_2 = module_0.to_namedtuple(var_6)
    var_11 = module_0.to_namedtuple(list_2)
    var_12 = module_0.to_namedtuple(var_9)


def test_case_12():
    bytes_0 = b"\x9cX\x05\x06\x89a\x87t\xf0\xceP\x84\x7f\x1eS\xd7"
    dict_0 = {bytes_0: bytes_0}
    bool_0 = True
    bool_1 = False
    tuple_0 = (dict_0, bool_0, bool_1)
    module_0.to_namedtuple(tuple_0)
