# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1
import builtins as module_2


def test_case_0():
    bool_0 = True
    module_0.to_namedtuple(bool_0)


def test_case_1():
    str_0 = "g6\tYQc\\fhk(2"
    set_0 = {str_0, str_0}
    list_0 = [set_0, str_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_2():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_3():
    bytes_0 = b"\x05\x08\x13>\x86"
    module_0.to_namedtuple(bytes_0)


def test_case_4():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_5():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_6():
    str_0 = "get_os_user"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_7():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_8():
    int_0 = -338
    dict_0 = {int_0: int_0, int_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_9():
    bytes_0 = b"_\x87\xd8*r\x0e\x93$\xc4\x7fv\xc3\xad\x85'+\xcb"
    bool_0 = True
    dict_0 = {
        bool_0: bytes_0,
        bool_0: bool_0,
        bytes_0: bool_0,
        bool_0: bool_0,
        bytes_0: bool_0,
    }
    tuple_0 = (dict_0,)
    object_0 = module_2.object()
    module_0.to_namedtuple(tuple_0)


def test_case_10():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_11():
    str_0 = "get_os_user"
    str_1 = "!Gq}~hB"
    dict_0 = {str_0: str_0, str_0: str_1, str_1: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_12():
    str_0 = "get_os_user"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_13():
    dict_0 = {}
    object_0 = module_0.to_namedtuple(dict_0)
    list_0 = [object_0, object_0, dict_0, dict_0]
    var_0 = module_0.to_namedtuple(list_0)
    str_0 = " et_os_user"
    bytes_0 = b"\xd6\xe5\xb9\x83\x92\x97\x80\xf6\x08\x8f\x03EG\xf19\xafE6"
    str_1 = "!Gq}~hB"
    dict_1 = {str_1: str_0, str_1: str_0, str_0: bytes_0, str_1: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_1)
    ordered_dict_1 = module_1.OrderedDict(**ordered_dict_0)
    var_1 = module_0.to_namedtuple(ordered_dict_1)
    ordered_dict_2 = module_1.OrderedDict()
    var_2 = module_0.to_namedtuple(var_1)
    var_3 = module_0.to_namedtuple(var_0)
