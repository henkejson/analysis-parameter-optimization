# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    int_0 = 2108
    module_0.to_namedtuple(int_0)


def test_case_1():
    float_0 = 25.0
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
    tuple_0 = (float_0, dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_3():
    str_0 = "wk"
    module_0.to_namedtuple(str_0)


def test_case_4():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_5():
    str_0 = "SRv"
    dict_0 = {str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_6():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_7():
    float_0 = 25.0
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
    tuple_0 = (float_0, dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    bytes_0 = b"\xcd\x9f \x02\x90\x14\xe7d*\tJ\x8e\xfdX\xe8\x82"
    dict_0 = {bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_9():
    str_0 = "\nSg\x0c"
    dict_0 = {str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    float_0 = -762.96807
    dict_1 = {
        float_0: float_0,
        float_0: float_0,
        float_0: float_0,
        float_0: float_0,
        float_0: float_0,
        float_0: float_0,
    }
    tuple_0 = (float_0, dict_1)
    var_0 = module_0.to_namedtuple(tuple_0)
    ordered_dict_1 = module_1.OrderedDict()
    list_0 = [dict_1, ordered_dict_1, var_0]
    var_1 = module_0.to_namedtuple(list_0)
    bytes_0 = b"\xf9\xcc\x9f\x05\xae&\xea9\x89\x83p<\x13H\x8c}\x90\xa97\xda"
    var_2 = module_0.to_namedtuple(ordered_dict_0)
    var_3 = module_0.to_namedtuple(tuple_0)
    module_0.to_namedtuple(bytes_0)


def test_case_10():
    str_0 = "\nS g\x0c"
    dict_0 = {str_0: str_0, str_0: str_0}
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    tuple_0 = (ordered_dict_0, ordered_dict_0, str_0, ordered_dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    float_0 = -762.96807
    dict_1 = {
        float_0: float_0,
        float_0: float_0,
        float_0: float_0,
        float_0: float_0,
        float_0: float_0,
        float_0: float_0,
    }
    tuple_1 = (float_0, dict_1)
    var_1 = module_0.to_namedtuple(tuple_1)
    ordered_dict_1 = module_1.OrderedDict()
    list_0 = [dict_1, ordered_dict_1, var_1]
    var_2 = module_0.to_namedtuple(list_0)
    var_3 = module_0.to_namedtuple(ordered_dict_0)
    var_4 = module_0.to_namedtuple(tuple_0)
    var_5 = module_0.to_namedtuple(var_0)
