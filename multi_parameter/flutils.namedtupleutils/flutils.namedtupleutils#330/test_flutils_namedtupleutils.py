# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    bool_0 = True
    module_0.to_namedtuple(bool_0)


def test_case_1():
    int_0 = -1256
    str_0 = "directory_present"
    tuple_0 = (int_0, str_0, int_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    str_0 = "\ry/`x/<U"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_4():
    str_0 = "%s.%s"
    module_0.to_namedtuple(str_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    str_0 = "NamedTuple"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_7():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_8():
    bytes_0 = b"u("
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_9():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_10():
    str_0 = "NamedTu:le"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    none_type_0 = None
    var_0 = module_0.to_namedtuple(dict_0)
    str_1 = "is_loaded"
    dict_1 = {str_0: dict_0, str_0: var_0, str_1: str_0, str_1: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_1)
    list_0 = [ordered_dict_0, none_type_0, var_0, dict_1]
    var_1 = module_0.to_namedtuple(list_0)


def test_case_11():
    str_0 = "NamedTuple"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    str_1 = "is_loaded"
    dict_1 = {str_0: dict_0, str_0: var_0, var_0: str_0, str_1: str_0}
    var_1 = module_0.to_namedtuple(dict_1)
    var_2 = module_0.to_namedtuple(var_1)


def test_case_12():
    str_0 = " k4"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    none_type_0 = None
    var_0 = module_0.to_namedtuple(dict_0)
    str_1 = "__attr_map__ contains an invalid item of: "
    str_2 = "is_loaded"
    dict_1 = {str_0: dict_0, str_0: var_0, str_1: str_0, str_2: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_1)
    list_0 = [ordered_dict_0, none_type_0, var_0, dict_1]
    var_1 = module_0.to_namedtuple(list_0)
    var_2 = module_0.to_namedtuple(var_1)
