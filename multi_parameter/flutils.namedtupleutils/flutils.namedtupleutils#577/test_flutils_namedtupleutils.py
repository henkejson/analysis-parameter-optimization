# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_1 = module_0.to_namedtuple(var_0)
    tuple_0 = (bool_0, list_0, var_0)
    tuple_1 = (bool_0, tuple_0, var_0, bool_0)
    var_2 = module_0.to_namedtuple(tuple_1)
    ordered_dict_0 = module_1.OrderedDict(*var_1)


def test_case_2():
    int_0 = -882
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = "#sQ1"
    module_0.to_namedtuple(str_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    str_0 = "h74\\Rzg{%t\tIT&Ht"
    int_0 = -882
    dict_0 = {str_0: str_0, str_0: str_0, str_0: int_0, int_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    str_0 = ", is invalid."
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_9():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_10():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_11():
    bytes_0 = b"\n\x9e\x0eyHE\xb9=\x8d\xdaT"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_12():
    str_0 = "JEg1"
    dict_0 = {}
    dict_1 = {str_0: dict_0, str_0: dict_0}
    var_0 = module_0.to_namedtuple(dict_1)


def test_case_13():
    list_0 = []
    str_0 = "exec_module"
    dict_0 = {str_0: list_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_14():
    list_0 = []
    str_0 = "exec_modul\t"
    dict_0 = {str_0: list_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(*list_0, **dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    list_1 = [str_0, ordered_dict_0, var_0, var_0]
    var_1 = module_0.to_namedtuple(list_1)
    ordered_dict_1 = module_1.OrderedDict()
    bool_0 = False
    bool_1 = True
    dict_1 = {bool_0: bool_0, bool_0: bool_1}
    var_2 = module_0.to_namedtuple(dict_1)
    var_3 = module_0.to_namedtuple(dict_0)
    module_0.to_namedtuple(str_0)
