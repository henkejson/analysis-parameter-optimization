# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    bool_0 = True
    module_0.to_namedtuple(bool_0)


def test_case_1():
    str_0 = "directory_present"
    bool_0 = False
    dict_0 = {bool_0: str_0, str_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_2():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_4():
    str_0 = "eyG[!s8)0v(NnK"
    module_0.to_namedtuple(str_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_0.to_namedtuple(var_1)


def test_case_7():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_8():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    tuple_0 = (dict_0,)
    tuple_1 = (bool_0, bool_0, bool_0, tuple_0)
    var_0 = module_0.to_namedtuple(tuple_1)
    bool_1 = True
    module_0.to_namedtuple(bool_1)


def test_case_9():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_10():
    str_0 = "patch"
    dict_0 = {str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    module_1.namedtuple(dict_0, ordered_dict_0, rename=str_0, defaults=ordered_dict_0)


def test_case_11():
    bytes_0 = b"e@I\xdf;\x8e\xe9M\t\x88{\xfe\xb8\xd6\xab\x8bU\xdbP"
    set_0 = {bytes_0, bytes_0, bytes_0}
    dict_0 = {bytes_0: set_0, bytes_0: bytes_0}
    tuple_0 = (bytes_0, set_0, dict_0)
    module_0.to_namedtuple(tuple_0)


def test_case_12():
    str_0 = " Cannot be a builtin name."
    bool_0 = True
    dict_0 = {
        bool_0: bool_0,
        bool_0: bool_0,
        bool_0: bool_0,
        str_0: bool_0,
        bool_0: bool_0,
    }
    var_0 = module_0.to_namedtuple(dict_0)
    module_1.namedtuple(var_0, var_0, defaults=dict_0)


def test_case_13():
    str_0 = "\tirectry_pr9get"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_1 = module_0.to_namedtuple(ordered_dict_0)
    var_2 = module_0.to_namedtuple(var_1)
    bool_0 = False
    dict_1 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_3 = module_0.to_namedtuple(dict_1)
    var_4 = module_0.to_namedtuple(dict_1)
    var_5 = module_0.to_namedtuple(dict_0)
    list_0 = [var_4, bool_0]
    var_6 = module_0.to_namedtuple(list_0)
    none_type_0 = None
    module_1.namedtuple(dict_0, none_type_0, defaults=dict_1)
