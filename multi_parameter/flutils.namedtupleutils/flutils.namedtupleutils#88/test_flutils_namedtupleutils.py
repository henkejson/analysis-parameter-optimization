# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    int_0 = 107
    module_0.to_namedtuple(int_0)


def test_case_1():
    int_0 = -511
    ordered_dict_0 = module_1.OrderedDict()
    tuple_0 = (int_0, ordered_dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    dict_0 = {}
    var_1 = module_0.to_namedtuple(dict_0)
    module_1.namedtuple(dict_0, int_0, module=int_0)


def test_case_2():
    str_0 = "subsequent_indent_len"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_3():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_4():
    bytes_0 = b"R\xec\t\x837\xf5S\xe0c\xe6m\xfe\xdbvq\x08\x86\xca"
    module_0.to_namedtuple(bytes_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    int_0 = -518
    dict_0 = {int_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_7():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_8():
    bytes_0 = b"\xb9\xbe\xebo\xe4Y1W\xc8\xe1\xe5\xb1\xf2\xa6dy2"
    list_0 = [bytes_0]
    var_0 = module_0.to_namedtuple(list_0)
    bytes_1 = b"\x1bx$Q\xe0\xf0\xb5\xb4"
    module_0.to_namedtuple(bytes_1)


def test_case_9():
    ordered_dict_0 = module_1.OrderedDict()
    dict_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_10():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_11():
    str_0 = "Item %r of the given 'cmd' is not of type 'str'.  Got: %r"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_0)


def test_case_12():
    str_0 = "subsequent_indent_len"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_13():
    bytes_0 = b"V!8m\x134\xa0U\xc8"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)
