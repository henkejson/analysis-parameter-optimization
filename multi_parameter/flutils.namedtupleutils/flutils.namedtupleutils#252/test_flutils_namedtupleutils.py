# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    float_0 = 403.0109
    module_0.to_namedtuple(float_0)


def test_case_1():
    str_0 = "gY*HFEs-5$b&Ua|>"
    int_0 = -1961
    dict_0 = {str_0: int_0, str_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)
    int_1 = -2443
    list_0 = [var_0, int_1]
    var_1 = module_0.to_namedtuple(list_0)


def test_case_2():
    str_0 = "N"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = "The path: %r must NOT contain any glob patterns."
    module_0.to_namedtuple(str_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    str_0 = "Nith"
    list_0 = [str_0, str_0, str_0, str_0]
    tuple_0 = ()
    dict_0 = {str_0: str_0, str_0: str_0, tuple_0: list_0}
    tuple_1 = (list_0, dict_0, str_0)
    var_0 = module_0.to_namedtuple(tuple_1)
    module_1.namedtuple(var_0, var_0, defaults=tuple_1)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    ordered_dict_0 = module_1.OrderedDict()
    tuple_0 = module_0.to_namedtuple(ordered_dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_9():
    str_0 = "gY*HFEs-5$b&Ua|>"
    int_0 = -1961
    dict_0 = {str_0: int_0, str_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_10():
    bytes_0 = b"\n\xaenu`\xa3\xfe\x8dT\xcd\xe3"
    bool_0 = False
    dict_0 = {bytes_0: bytes_0, bool_0: bytes_0}
    tuple_0 = (bytes_0, dict_0, bytes_0, bool_0)
    module_0.to_namedtuple(tuple_0)


def test_case_11():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_12():
    ordered_dict_0 = module_1.OrderedDict()
    tuple_0 = (ordered_dict_0,)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_13():
    str_0 = "Nith\r"
    list_0 = [str_0, str_0, str_0, str_0]
    tuple_0 = ()
    dict_0 = {str_0: str_0, str_0: str_0, tuple_0: list_0}
    tuple_1 = (list_0, dict_0, str_0)
    var_0 = module_0.to_namedtuple(tuple_1)
    str_1 = "gY*HFEs-5$b&Ua|>"
    int_0 = -1961
    dict_1 = {str_1: int_0, str_1: int_0}
    var_1 = module_0.to_namedtuple(dict_1)
    int_1 = -2419
    list_1 = [var_1, int_1]
    var_2 = module_0.to_namedtuple(list_1)
    var_3 = module_0.to_namedtuple(var_2)
    var_4 = module_0.to_namedtuple(var_0)
    module_0.to_namedtuple(str_1)
