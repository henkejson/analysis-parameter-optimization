# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1
import builtins as module_2


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_2():
    str_0 = "b64"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    list_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    bytes_0 = b"/\xab\x1f\n\xae\xa4\xb4T\xec@\x90K"
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_7():
    str_0 = "b64"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    bool_0 = True
    list_0 = [bool_0]
    ordered_dict_0 = module_1.OrderedDict()
    tuple_0 = (list_0, ordered_dict_0, ordered_dict_0, list_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)
    ordered_dict_1 = module_1.OrderedDict()


def test_case_9():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_10():
    bool_0 = True
    list_0 = [bool_0]
    dict_0 = {bool_0: list_0}
    ordered_dict_0 = module_1.OrderedDict()
    tuple_0 = (list_0, dict_0, ordered_dict_0, list_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_1.OrderedDict()


def test_case_11():
    object_0 = module_2.object()
    bytes_0 = b"n\xd1\xc3"
    float_0 = -1549.685796
    dict_0 = {object_0: object_0, bytes_0: float_0, float_0: object_0, float_0: float_0}
    module_0.to_namedtuple(dict_0)


def test_case_12():
    str_0 = "b&4"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    bool_0 = True
    var_0 = module_0.to_namedtuple(dict_0)
    list_0 = [dict_0]
    tuple_0 = (ordered_dict_0, bool_0, list_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    module_0.to_namedtuple(str_0)


def test_case_13():
    str_0 = "b64\n"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    bool_0 = True
    list_0 = [dict_0]
    tuple_0 = (ordered_dict_0, bool_0, list_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)
