# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_2():
    str_0 = "placeholder_len"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    bytes_0 = b"\xd2\xe1\xd1\x04\xfe\x15\x11\x07KSv\xa2\xc4"
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    str_0 = "{`78>"
    str_1 = "capitalize"
    float_0 = 542.6
    str_2 = "The name of the cherry-picking module attribute."
    dict_0 = {str_0: str_0, str_1: str_0, str_1: float_0, str_2: float_0}
    var_0 = module_0.to_namedtuple(dict_0)
    bool_0 = False
    module_0.to_namedtuple(bool_0)


def test_case_7():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(ordered_dict_0)
    var_2 = module_0.to_namedtuple(ordered_dict_0)
    var_3 = module_0.to_namedtuple(var_0)
    var_4 = module_0.to_namedtuple(var_1)


def test_case_8():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_9():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_10():
    int_0 = 1
    int_1 = -1684
    bool_0 = False
    tuple_0 = ()
    int_2 = -664
    tuple_1 = (bool_0, tuple_0, tuple_0, int_2)
    bool_1 = True
    bytes_0 = b"\xd6Pw\xf7\xc8K\x88\xab\x92^\x0fB"
    tuple_2 = (tuple_1, bool_1, bytes_0)
    dict_0 = {int_1: int_0, int_1: tuple_2, bool_1: int_0, bytes_0: bytes_0}
    list_0 = [int_0, int_1, dict_0]
    str_0 = "D@ZGU;"
    tuple_3 = (list_0, list_0, bool_0, str_0)
    module_0.to_namedtuple(tuple_3)


def test_case_11():
    str_0 = "{`78>"
    str_1 = "a\x0c"
    float_0 = -601.4649
    str_2 = "The name of the cherry-picking module attribute."
    dict_0 = {str_0: str_0, str_1: str_0, str_1: float_0, str_2: float_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(ordered_dict_0)
    tuple_0 = (var_0,)
    var_2 = module_0.to_namedtuple(tuple_0)
    bytes_0 = b"\xe0\\\xd8\xcf\xaf\xf9\x10Rv\xa4\xe4\xa74W\xc5P\x08=\x92"
    module_0.to_namedtuple(bytes_0)
