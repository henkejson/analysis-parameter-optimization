# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    str_0 = "utf8"
    int_0 = 1
    dict_0 = {int_0: str_0, str_0: str_0, str_0: str_0, str_0: int_0, str_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_2():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = "-4]H\rn6"
    module_0.to_namedtuple(str_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    bytes_0 = b"\xa0\x88\xa2u\xf4}\x94t{\xb5\xb1\xd0$\xb4"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    str_0 = "ut)8"
    int_0 = 1
    dict_0 = {str_0: str_0, str_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    module_0.to_namedtuple(str_0)


def test_case_9():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_10():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    list_0 = [dict_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_11():
    str_0 = "utf8"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_12():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    list_0 = module_0.to_namedtuple(dict_0)
    var_0 = module_0.to_namedtuple(list_0)


def test_case_13():
    str_0 = "ut\x0b"
    int_0 = 1
    dict_0 = {int_0: str_0, str_0: str_0, str_0: str_0, str_0: int_0, str_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    tuple_0 = (int_0,)
    var_2 = module_0.to_namedtuple(tuple_0)
    var_3 = module_0.to_namedtuple(var_1)
