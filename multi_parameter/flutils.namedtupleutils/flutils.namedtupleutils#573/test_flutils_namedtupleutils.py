# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    int_0 = 1621
    module_0.to_namedtuple(int_0)


def test_case_1():
    int_0 = 1166
    ordered_dict_0 = module_1.OrderedDict()
    tuple_0 = (int_0, int_0, ordered_dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    bool_0 = True
    list_0 = [int_0, var_0, bool_0]
    var_1 = module_0.to_namedtuple(list_0)


def test_case_2():
    str_0 = "pE'qdi\x0c"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = "`A]P~gSMO-xu"
    module_0.to_namedtuple(str_0)


def test_case_5():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_6():
    int_0 = 4108
    str_0 = "camel_to_underscore"
    dict_0 = {int_0: int_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    str_0 = "WkCqV"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_9():
    str_0 = "WkCqV"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_10():
    str_0 = "pE'qdi\x0c"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    ordered_dict_0 = module_1.OrderedDict(*var_1)


def test_case_11():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_12():
    ordered_dict_0 = module_1.OrderedDict()
    tuple_0 = (ordered_dict_0, ordered_dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_13():
    bytes_0 = b"\xf0\xc7\xf5\xc1\x9f\xcdh\xb8"
    dict_0 = {bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_14():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)
    str_0 = "Eqdi\x0c"
    dict_0 = {str_0: str_0}
    var_1 = module_0.to_namedtuple(dict_0)
