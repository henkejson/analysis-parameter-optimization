# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    int_0 = 2985
    module_0.to_namedtuple(int_0)


def test_case_1():
    str_0 = "cF0"
    none_type_0 = None
    dict_0 = {str_0: none_type_0, str_0: none_type_0, str_0: none_type_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_2():
    bytes_0 = b""
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    float_0 = -1633.42035
    list_0 = [dict_0, bytes_0, float_0, dict_0]
    module_0.to_namedtuple(list_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    bytes_0 = b'}Z\xe3"^\xac\x8d\xddQ\xd6w\x82\xa5\x01\xfbu'
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_0.to_namedtuple(var_1)
    ordered_dict_0 = module_1.OrderedDict()
    var_3 = module_0.to_namedtuple(var_0)
    var_4 = module_0.to_namedtuple(var_1)
    var_5 = module_0.to_namedtuple(var_3)
    var_6 = module_0.to_namedtuple(var_1)
    var_7 = module_0.to_namedtuple(var_5)


def test_case_7():
    str_0 = "cF0"
    none_type_0 = None
    dict_0 = {str_0: none_type_0, str_0: none_type_0, str_0: none_type_0}
    ordered_dict_0 = module_0.to_namedtuple(dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_8():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    var_2 = module_0.to_namedtuple(tuple_0)
    var_3 = module_0.to_namedtuple(var_0)
    var_4 = module_0.to_namedtuple(tuple_0)
    str_0 = ""
    list_0 = [var_1, var_1, str_0, str_0]
    var_5 = module_0.to_namedtuple(list_0)


def test_case_9():
    ordered_dict_0 = module_1.OrderedDict()
    list_0 = [ordered_dict_0, ordered_dict_0, ordered_dict_0, ordered_dict_0]
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(list_0)
    var_3 = module_0.to_namedtuple(ordered_dict_0)


def test_case_10():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_11():
    ordered_dict_0 = module_1.OrderedDict()
    list_0 = [ordered_dict_0, ordered_dict_0, ordered_dict_0, ordered_dict_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_12():
    str_0 = "cF0"
    none_type_0 = None
    str_1 = 'E\n"R.Pg:gX~'
    dict_0 = {str_0: none_type_0, str_0: none_type_0, str_1: none_type_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_13():
    str_0 = "validate_identifier\t"
    str_1 = "(T\\Y^Uf8.VIm6>Y8"
    dict_0 = {str_0: str_0, str_1: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(ordered_dict_0)
    ordered_dict_1 = module_1.OrderedDict()
    var_2 = module_0.to_namedtuple(var_0)
    list_0 = [var_1]
    var_3 = module_0.to_namedtuple(var_0)
    var_4 = module_0.to_namedtuple(list_0)
    bool_0 = True
    var_5 = module_0.to_namedtuple(list_0)
    module_0.to_namedtuple(bool_0)
