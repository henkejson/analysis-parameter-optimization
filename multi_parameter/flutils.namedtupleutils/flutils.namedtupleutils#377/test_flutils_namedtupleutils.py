# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    bool_0 = False
    str_0 = "t"
    dict_0 = {str_0: str_0, str_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_2():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_3():
    str_0 = "4p"
    module_0.to_namedtuple(str_0)


def test_case_4():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_5():
    bool_0 = False
    str_0 = "t"
    dict_0 = {str_0: bool_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_6():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_7():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_8():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)
    tuple_0 = (list_0, list_0, list_0, var_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    ordered_dict_0 = module_1.OrderedDict()
    list_1 = [var_1, list_0, var_0, list_0]
    var_2 = module_0.to_namedtuple(list_1)


def test_case_9():
    str_0 = "nJ2~M6l.!x"
    bool_0 = True
    tuple_0 = (str_0, str_0, bool_0)
    dict_0 = {str_0: tuple_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    str_1 = "a^\x0b6S]$;5xaJ|J#dTF\x0c\\"
    module_0.to_namedtuple(str_1)


def test_case_10():
    str_0 = "nJ2~6l.!x"
    bool_0 = False
    tuple_0 = (str_0, str_0, bool_0)
    dict_0 = {str_0: str_0, str_0: bool_0, bool_0: tuple_0, bool_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    dict_1 = {}
    var_2 = module_0.to_namedtuple(dict_1)
    var_3 = module_0.to_namedtuple(var_2)


def test_case_11():
    bytes_0 = b"\x1au_"
    int_0 = 3
    bool_0 = False
    dict_0 = {bytes_0: bytes_0, bytes_0: bool_0, bool_0: int_0, bool_0: bool_0}
    tuple_0 = (bytes_0, int_0, bool_0, dict_0)
    module_0.to_namedtuple(tuple_0)


def test_case_12():
    str_0 = "\x0bTG"
    str_1 = "J2~6l.!x"
    bool_0 = False
    tuple_0 = (str_1, str_0, bool_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    dict_0 = {str_0: str_0, str_0: var_0, var_0: tuple_0, var_0: str_0}
    var_1 = module_0.to_namedtuple(dict_0)
    module_1.namedtuple(var_0, bool_0, rename=var_1, defaults=bool_0, module=var_0)
