# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.to_namedtuple(list_0)
    module_0.to_namedtuple(bool_0)


def test_case_2():
    str_0 = "Vv"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = "08FK5/::v^#ifx"
    module_0.to_namedtuple(str_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0}
    bool_1 = True
    dict_0 = {bool_0: bool_1, bool_1: bool_0}
    tuple_0 = (bool_0, set_0, dict_0, bool_1)
    list_0 = [tuple_0, tuple_0, tuple_0, bool_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_7():
    str_0 = "Vv"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    str_0 = "+Fp\x0c,O+L+"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    tuple_0 = (str_0, dict_0, str_0)
    list_0 = [tuple_0]
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_0)
    var_3 = module_0.to_namedtuple(var_2)


def test_case_9():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_10():
    bytes_0 = b"\xb7$"
    dict_0 = {bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_11():
    str_0 = "\tP"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    int_0 = 2123
    tuple_0 = (str_0, dict_0, int_0)
    list_0 = [tuple_0]
    var_1 = module_0.to_namedtuple(list_0)
    var_2 = module_0.to_namedtuple(var_0)
    var_3 = module_0.to_namedtuple(var_1)
    str_1 = "08FK5/::v^#ifx"
    module_0.to_namedtuple(str_1)
