# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    bool_0 = False
    set_0 = set()
    list_0 = []
    tuple_0 = (bool_0, set_0, list_0, bool_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    str_0 = "Yl"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    bytes_0 = b"@\xd2\xa2Z\x13\x9e\xbfa._\x1b\xe4\x9dYOx~"
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    str_0 = "4{T#}\nJ!\\a"
    none_type_0 = None
    dict_0 = {str_0: none_type_0}
    var_0 = module_0.to_namedtuple(dict_0)
    module_0.to_namedtuple(str_0)


def test_case_7():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_8():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_9():
    float_0 = -2437.294224
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(dict_0)
    bytes_0 = b"\xa1\xdb_)\x91\x80\x03\x82\xe1\x130"
    module_0.to_namedtuple(bytes_0)


def test_case_10():
    bytes_0 = b"\xccA\xd2\xca\xf4Z"
    bool_0 = False
    int_0 = 2994
    dict_0 = {int_0: bool_0, bool_0: int_0, bytes_0: int_0}
    tuple_0 = (bool_0, int_0, dict_0)
    tuple_1 = (bytes_0, tuple_0)
    module_0.to_namedtuple(tuple_1)


def test_case_11():
    str_0 = "e\n"
    none_type_0 = None
    dict_0 = {str_0: none_type_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    tuple_0 = (var_1, none_type_0)
    var_2 = module_0.to_namedtuple(tuple_0)
    module_0.to_namedtuple(none_type_0)
