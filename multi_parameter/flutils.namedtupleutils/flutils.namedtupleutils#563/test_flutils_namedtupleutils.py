# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    set_0 = set()
    module_0.to_namedtuple(set_0)


def test_case_1():
    int_0 = 1580
    int_1 = 3
    str_0 = "7hIaH/ppezr4?US?+J2M"
    dict_0 = {int_0: int_0, int_0: int_0, int_1: str_0, int_1: int_1}
    list_0 = [int_1, dict_0]
    tuple_0 = (dict_0, list_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    int_2 = 713
    module_0.to_namedtuple(int_2)


def test_case_2():
    str_0 = "path_absent"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_4():
    str_0 = "'VdX"
    module_0.to_namedtuple(str_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_7():
    str_0 = "path_absent"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    str_0 = "AN2RGsAqzU_V1[nV"
    dict_0 = {str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_9():
    bool_0 = False
    ordered_dict_0 = module_1.OrderedDict()
    tuple_0 = (ordered_dict_0, bool_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)
    module_1.OrderedDict(*var_1)


def test_case_10():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_11():
    ordered_dict_0 = module_1.OrderedDict()
    list_0 = [ordered_dict_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_12():
    bytes_0 = b"\xf0\xb8\xd0p\x8d\x80\xb2\xfe"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)
