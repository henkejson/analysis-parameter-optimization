# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    float_0 = 1758.05334
    module_0.to_namedtuple(float_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    tuple_0 = (list_0, bool_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_2():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_3():
    bytes_0 = b"\xc8\x14S+\xa1\xec\xdc\n\x1dv\x16CL"
    module_0.to_namedtuple(bytes_0)


def test_case_4():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_5():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_6():
    bytes_0 = b"\xda\x8c\xc8\xfd\xf8"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_7():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_9():
    bool_0 = False
    str_0 = "stderr"
    tuple_0 = (bool_0, bool_0, str_0, bool_0)
    dict_0 = {
        bool_0: bool_0,
        bool_0: bool_0,
        bool_0: bool_0,
        bool_0: tuple_0,
        str_0: tuple_0,
    }
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_10():
    float_0 = 1679.303989
    bool_0 = True
    str_0 = "&d"
    tuple_0 = (bool_0, bool_0, str_0, float_0)
    dict_0 = {
        bool_0: bool_0,
        bool_0: bool_0,
        bool_0: bool_0,
        float_0: tuple_0,
        str_0: tuple_0,
    }
    var_0 = module_0.to_namedtuple(dict_0)
    module_1.namedtuple(str_0, tuple_0)


def test_case_11():
    float_0 = 1679.303989
    bool_0 = False
    str_0 = "stderr"
    tuple_0 = (bool_0, bool_0, str_0, float_0)
    dict_0 = {
        bool_0: bool_0,
        bool_0: bool_0,
        bool_0: bool_0,
        float_0: tuple_0,
        str_0: tuple_0,
    }
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_0.to_namedtuple(var_0)
    var_3 = module_0.to_namedtuple(var_2)
    bytes_0 = b"f\x1a!r\xf9?\xc4\xb8\xbe"
    dict_1 = {bytes_0: var_1}
    module_0.to_namedtuple(dict_1)


def test_case_12():
    float_0 = 1679.303989
    bool_0 = False
    str_0 = "stder\x0c"
    tuple_0 = (bool_0, bool_0, str_0, float_0)
    dict_0 = {
        bool_0: bool_0,
        bool_0: bool_0,
        bool_0: bool_0,
        float_0: tuple_0,
        str_0: tuple_0,
    }
    var_0 = module_0.to_namedtuple(dict_0)
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    module_0.to_namedtuple(float_0)
