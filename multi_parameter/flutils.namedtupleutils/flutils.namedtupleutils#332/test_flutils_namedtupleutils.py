# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    int_0 = -595
    module_0.to_namedtuple(int_0)


def test_case_1():
    bool_0 = True
    tuple_0 = (bool_0, bool_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    dict_0 = {}
    tuple_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    bytes_0 = b"\x90\x0b\xbe\xafX\tI\xb9"
    module_0.to_namedtuple(bytes_0)


def test_case_4():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_5():
    bytes_0 = b"\x06\x98)\x91\xe4\xb4\xfd\xa3^\x13\x9bh\x97\xcd'"
    tuple_0 = (bytes_0,)
    var_0 = module_0.to_namedtuple(tuple_0)
    int_0 = 50855936
    module_0.to_namedtuple(int_0)


def test_case_6():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_9():
    bool_0 = True
    str_0 = "b"
    dict_0 = {
        str_0: str_0,
        bool_0: bool_0,
        bool_0: bool_0,
        bool_0: bool_0,
        str_0: bool_0,
    }
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_10():
    bool_0 = True
    str_0 = "The given 'setup_dir' of %r is NOT a directory."
    bool_1 = True
    str_1 = ".(8'VP'e!IG>=k8Y"
    dict_0 = {str_0: str_0, str_0: bool_0, str_0: bool_1, str_1: bool_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    list_0 = [bool_0, ordered_dict_0, ordered_dict_0]
    var_0 = module_0.to_namedtuple(list_0)
    module_0.to_namedtuple(bool_0)


def test_case_11():
    bytes_0 = b"\xc4e\x9ab\x9b\x10\x8aM,Oy\xf5\x8c\x95\xcb\xc5\xd2\xee\xf4"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    bytes_1 = b"k=SZ\xaen\xe2\x1b\x99>\xcc\xdf\x05C\xe5.\xbcB\xd3"
    int_0 = -76
    tuple_0 = (dict_0, bytes_1, int_0)
    module_0.to_namedtuple(tuple_0)


def test_case_12():
    list_0 = []
    str_0 = "n\x0c"
    dict_0 = {str_0: list_0}
    var_0 = module_0.to_namedtuple(dict_0)
    tuple_0 = (var_0, var_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    bool_0 = True
    bool_1 = True
    str_1 = "b"
    dict_1 = {
        str_1: str_1,
        bool_1: bool_1,
        bool_1: bool_0,
        bool_1: bool_1,
        str_1: bool_0,
    }
    ordered_dict_0 = module_1.OrderedDict(**dict_1)
    list_1 = [bool_0, ordered_dict_0, ordered_dict_0]
    module_1.namedtuple(list_1, bool_1, module=var_0)
