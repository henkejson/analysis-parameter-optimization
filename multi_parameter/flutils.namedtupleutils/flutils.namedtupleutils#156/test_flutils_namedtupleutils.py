# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    bool_0 = False
    module_0.to_namedtuple(bool_0)


def test_case_1():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)
    int_0 = -1231
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_0.to_namedtuple(var_1)
    list_0 = [int_0, int_0]
    var_3 = module_0.to_namedtuple(list_0)
    var_4 = module_0.to_namedtuple(list_0)


def test_case_2():
    ordered_dict_0 = module_1.OrderedDict()
    list_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_3():
    str_0 = "\x0b&[k=eYf\x0bhw*j3?8$"
    module_0.to_namedtuple(str_0)


def test_case_4():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_5():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_6():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_7():
    str_0 = "utf8"
    dict_0 = {str_0: str_0, str_0: str_0}
    list_0 = [str_0, dict_0]
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.to_namedtuple(list_1)
    module_0.to_namedtuple(str_0)


def test_case_8():
    str_0 = "utf8"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_9():
    str_0 = "Ov,\\MKx/e/nL"
    dict_0 = {str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    ordered_dict_1 = module_1.OrderedDict()


def test_case_10():
    int_0 = 927
    str_0 = "__doc__"
    dict_0 = {int_0: int_0, str_0: int_0, str_0: str_0}
    list_0 = [dict_0]
    var_0 = module_0.to_namedtuple(list_0)
    int_1 = 268
    module_0.to_namedtuple(int_1)


def test_case_11():
    str_0 = "Ov,\\MKx/e/nL"
    dict_0 = {str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    ordered_dict_1 = module_1.OrderedDict()


def test_case_12():
    str_0 = "\nutf8"
    dict_0 = {str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    list_0 = [ordered_dict_0, dict_0]
    list_1 = [list_0, list_0, list_0]
    list_2 = [list_1, ordered_dict_0, ordered_dict_0, list_0]
    var_0 = module_0.to_namedtuple(list_1)
    var_1 = module_0.to_namedtuple(list_2)
    tuple_0 = (list_2, var_1, var_0)
    var_2 = module_0.to_namedtuple(tuple_0)
    list_3 = []
    module_1.namedtuple(list_3, list_2)


def test_case_13():
    bytes_0 = b"1L\x97\xdf\x0b"
    dict_0 = {bytes_0: bytes_0}
    list_0 = [dict_0]
    module_0.to_namedtuple(list_0)
