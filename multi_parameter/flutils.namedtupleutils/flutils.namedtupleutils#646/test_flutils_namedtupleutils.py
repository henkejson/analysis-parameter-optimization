# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    bool_0 = True
    module_0.to_namedtuple(bool_0)


def test_case_1():
    int_0 = 867
    list_0 = [int_0, int_0]
    var_0 = module_0.to_namedtuple(list_0)
    set_0 = set()
    module_0.to_namedtuple(set_0)


def test_case_2():
    complex_0 = -4256 - 128.4j
    dict_0 = {complex_0: complex_0, complex_0: complex_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = "Check if given ``obj`` has all the given ``*attrs``.\n\n    Args:\n        obj (:obj:`Any <typing.Any>`): The object to check.\n        *attrs (:obj:`str`): The names of the attributes to check.\n\n    :rtype:\n        :obj:`bool`\n\n        * :obj:`True` if all the given ``*attrs`` exist on the given ``obj``;\n        * :obj:`False` otherwise.\n\n    Example:\n        >>> from flutils.objutils import has_attrs\n        >>> has_attrs(dict(),'get','keys','items','values')\n        True\n    "
    module_0.to_namedtuple(str_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    str_0 = "m"
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: str_0, bool_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    bytes_0 = b"D\x8f\x0e\x8e\xb8"
    tuple_0 = (bytes_0,)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_9():
    str_0 = "|hN<yL"
    bool_0 = False
    int_0 = -2221
    dict_0 = {bool_0: bool_0, int_0: str_0, bool_0: str_0, str_0: str_0}
    tuple_0 = module_0.to_namedtuple(dict_0)
    module_0.to_namedtuple(bool_0)


def test_case_10():
    str_0 = "1#Q\nXWX\\\nUW6>A"
    bytes_0 = b"B\xceA`\x94\x85\x19"
    int_0 = -702
    dict_0 = {str_0: str_0, bytes_0: str_0, bytes_0: str_0, bytes_0: int_0}
    tuple_0 = (str_0, bytes_0, dict_0)
    module_0.to_namedtuple(tuple_0)


def test_case_11():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_12():
    complex_0 = -4256 - 128.4j
    dict_0 = {complex_0: complex_0, complex_0: complex_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_13():
    str_0 = "m"
    int_0 = -2229
    dict_0 = {str_0: str_0, int_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_14():
    str_0 = "SdO\n"
    bool_0 = False
    int_0 = -2266
    dict_0 = {bool_0: bool_0, int_0: str_0, bool_0: str_0, str_0: str_0}
    bool_1 = False
    tuple_0 = (str_0, bool_0, dict_0, bool_1)
    var_0 = module_0.to_namedtuple(tuple_0)
    list_0 = [str_0, str_0, tuple_0, bool_1]
    var_1 = module_0.to_namedtuple(list_0)
    var_2 = module_0.to_namedtuple(var_1)
