# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    bool_0 = True
    module_0.to_namedtuple(bool_0)


def test_case_1():
    str_0 = "h"
    none_type_0 = None
    dict_0 = {str_0: none_type_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_2():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    bytes_0 = b"\x8d\rq"
    module_0.to_namedtuple(bytes_0)


def test_case_4():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_5():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_6():
    str_0 = "qS"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_7():
    str_0 = "qS"
    dict_0 = {str_0: str_0}
    tuple_0 = module_0.to_namedtuple(dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_8():
    str_0 = 's;@Bz(y.:v"q4.'
    bool_0 = True
    float_0 = -3193.0
    dict_0 = {bool_0: str_0, str_0: bool_0}
    tuple_0 = (str_0, bool_0, float_0, dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_9():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_10():
    str_0 = "qS"
    dict_0 = {str_0: str_0}
    tuple_0 = (str_0, dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_11():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_12():
    bytes_0 = b"\xab{J\t"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)
