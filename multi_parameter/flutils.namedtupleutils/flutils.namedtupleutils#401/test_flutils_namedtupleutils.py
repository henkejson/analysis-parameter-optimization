# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    set_0 = set()
    tuple_0 = (set_0,)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    str_0 = "R"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    bytes_0 = b'@"\x0f\xe5\xdf|\x80\x90R.q\xaa'
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    int_0 = 2465
    dict_0 = {int_0: int_0}
    bool_0 = False
    tuple_0 = (int_0, dict_0, bool_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    var_2 = module_0.to_namedtuple(var_1)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    var_0 = module_1.OrderedDict()
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_1)


def test_case_9():
    str_0 = "h2{D,|W!9,3#"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_10():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_11():
    str_0 = "Xw"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_12():
    str_0 = "\tg"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_0.to_namedtuple(var_1)
    module_1.OrderedDict(**var_0)


def test_case_13():
    bytes_0 = b"\xc8\xa1\x9a"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    float_0 = 623.0
    bytes_1 = b""
    tuple_0 = (bytes_0, dict_0, float_0, bytes_1)
    module_0.to_namedtuple(tuple_0)
