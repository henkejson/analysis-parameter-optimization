# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1
import builtins as module_2


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    int_0 = 2279
    list_0 = [int_0, int_0]
    tuple_0 = (int_0, list_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    str_0 = 'K{"jrEh3;'
    module_0.to_namedtuple(str_0)


def test_case_4():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_5():
    str_0 = "name"
    ordered_dict_0 = module_1.OrderedDict()
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(ordered_dict_0)


def test_case_6():
    str_0 = "name"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    tuple_0 = (dict_0, dict_0, dict_0, dict_0)
    var_2 = module_0.to_namedtuple(tuple_0)


def test_case_8():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_9():
    dict_0 = {}
    tuple_0 = (dict_0, dict_0, dict_0, dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_10():
    bytes_0 = b"\xc2\x9e"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_11():
    int_0 = -2679
    dict_0 = {int_0: int_0, int_0: int_0}
    float_0 = 643.84281
    set_0 = {int_0}
    tuple_0 = (int_0, set_0)
    bool_0 = True
    tuple_1 = (dict_0, float_0, tuple_0, bool_0)
    var_0 = module_0.to_namedtuple(tuple_1)
    bool_1 = True
    list_0 = [bool_1]
    var_1 = module_0.to_namedtuple(list_0)


def test_case_12():
    bool_0 = True
    str_0 = "\nwj3Zzboy}1E~"
    tuple_0 = (bool_0, str_0)
    ordered_dict_0 = module_1.OrderedDict()
    bytes_0 = b"\x8c\x8cT\xf2\x18f\xce\x14\xceUI\x07\x94\xef\xf5"
    tuple_1 = (bool_0, tuple_0, ordered_dict_0, bytes_0)
    var_0 = module_0.to_namedtuple(tuple_1)
    var_1 = module_0.to_namedtuple(tuple_1)
    list_0 = [bytes_0, bool_0]
    var_2 = module_0.to_namedtuple(list_0)
    var_3 = module_0.to_namedtuple(var_2)
    object_0 = module_2.object()
    dict_0 = {str_0: str_0, str_0: str_0}
    var_4 = module_0.to_namedtuple(dict_0)
    var_5 = module_0.to_namedtuple(var_2)
    module_0.to_namedtuple(bytes_0)


def test_case_13():
    bool_0 = False
    str_0 = "\name"
    ordered_dict_0 = module_1.OrderedDict()
    bytes_0 = b"\x8c\x8cT\xf2\x18f\xce\x14]UI\x07\x94\xef\xf5"
    tuple_0 = (ordered_dict_0, ordered_dict_0, ordered_dict_0, bytes_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    var_2 = module_0.to_namedtuple(var_0)
    list_0 = [bytes_0, bool_0]
    ordered_dict_1 = module_1.OrderedDict()
    list_1 = [bool_0, list_0, list_0]
    var_3 = module_0.to_namedtuple(list_1)
    var_4 = module_0.to_namedtuple(var_1)
    dict_0 = {var_4: var_4, str_0: var_4}
    var_5 = module_0.to_namedtuple(dict_0)
    var_6 = module_0.to_namedtuple(ordered_dict_0)
    var_7 = module_0.to_namedtuple(tuple_0)
    var_8 = module_0.to_namedtuple(var_6)
    var_9 = module_0.to_namedtuple(var_7)
