# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    set_0 = set()
    module_0.to_namedtuple(set_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_2():
    str_0 = "k"
    bytes_0 = b"\xd3\x05'\x9e\xc0\xec\x82\x16\xf2\xd7\xaa\x1b\xd3\xbcY\x18h"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: bytes_0, str_0: bytes_0}
    var_0 = module_0.to_namedtuple(dict_0)
    ordered_dict_0 = module_1.OrderedDict()
    var_1 = module_0.to_namedtuple(var_0)


def test_case_3():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_4():
    str_0 = "dhG\x0br:wh>1:iweV;"
    module_0.to_namedtuple(str_0)


def test_case_5():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_6():
    bool_0 = True
    str_0 = "k"
    bytes_0 = b"\xd3\x05'\x9e\xc0\xec\x82\x16\xf2\xd7\xaa\x1b\xd3\xbcY\x18h"
    dict_0 = {bool_0: bool_0, str_0: bool_0, str_0: bytes_0, str_0: bytes_0}
    var_0 = module_0.to_namedtuple(dict_0)
    ordered_dict_0 = module_1.OrderedDict()
    var_1 = module_0.to_namedtuple(var_0)


def test_case_7():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_8():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_9():
    bool_0 = True
    str_0 = "]a3Oh'(co(+/pL"
    bytes_0 = b"\xd3\x05'\x9e\xc0\xec\x82\x16\xf2\xd7\xaa\x1b\xd3\xbcY\x18h"
    dict_0 = {bool_0: bool_0, str_0: bool_0, str_0: bytes_0, str_0: bytes_0}
    tuple_0 = (bytes_0, dict_0, dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    module_0.to_namedtuple(str_0)


def test_case_10():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_11():
    bytes_0 = b"\xa6.116\xe2\xe9^\x06\x13\xd8"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_12():
    bool_0 = True
    str_0 = "\tHM"
    bytes_0 = b"\xd3\x05'\x9e\xc0\xec\x82\x16\xf2\xd7\xaa\x1b\xd3\xbcY\x18h"
    dict_0 = {bool_0: bool_0, str_0: bool_0, str_0: bytes_0, str_0: bytes_0}
    tuple_0 = (bytes_0, dict_0, dict_0)
    var_0 = module_0.to_namedtuple(dict_0)
    tuple_1 = (var_0, bool_0, str_0, var_0)
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_0.to_namedtuple(tuple_0)
    var_3 = module_0.to_namedtuple(tuple_1)
    module_0.to_namedtuple(bool_0)
