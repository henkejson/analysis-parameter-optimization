# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1
import builtins as module_2


def test_case_0():
    bool_0 = False
    module_0.to_namedtuple(bool_0)


def test_case_1():
    bool_0 = False
    tuple_0 = (bool_0,)
    tuple_1 = ()
    var_0 = module_0.to_namedtuple(tuple_1)
    var_1 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_3():
    str_0 = "OP\\[PR2KM_*t"
    module_0.to_namedtuple(str_0)


def test_case_4():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_5():
    str_0 = "C79"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_6():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_7():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_9():
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_10():
    str_0 = "p\\`\nB1Y("
    str_1 = "\x0c}UZ\r|jZuV)mu7z=,x<"
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_11():
    int_0 = 651
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.to_namedtuple(list_0)
    bytes_0 = b"\xf4\xb3\xbd\x80\xd9\x93B\x88\xa5\xf5\xde\xcf\xd3W,"
    bool_0 = False
    dict_0 = {bytes_0: bool_0}
    module_0.to_namedtuple(dict_0)


def test_case_12():
    str_0 = "convert_escaped_utf8_literal"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_13():
    ordered_dict_0 = module_1.OrderedDict()
    str_0 = "xNb\x0c"
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    object_0 = module_2.object(**ordered_dict_0)
    tuple_0 = (var_0, object_0, object_0, object_0)
    var_1 = module_0.to_namedtuple(var_0)
    dict_0 = {str_0: tuple_0, tuple_0: tuple_0, var_1: tuple_0}
    var_2 = module_0.to_namedtuple(dict_0)
    var_3 = module_0.to_namedtuple(dict_0)
    var_4 = module_0.to_namedtuple(var_2)
    var_5 = module_0.to_namedtuple(var_2)
    module_0.to_namedtuple(str_0)
