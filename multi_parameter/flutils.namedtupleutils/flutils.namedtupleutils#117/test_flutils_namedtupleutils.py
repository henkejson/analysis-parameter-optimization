# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1
import builtins as module_2


def test_case_0():
    bool_0 = False
    module_0.to_namedtuple(bool_0)


def test_case_1():
    str_0 = "a"
    set_0 = {str_0}
    int_0 = -2581
    dict_0 = {str_0: set_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_2():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_3():
    bytes_0 = b"<\xce"
    module_0.to_namedtuple(bytes_0)


def test_case_4():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_5():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_6():
    str_0 = "a"
    set_0 = {str_0}
    tuple_0 = (str_0, str_0, set_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    int_0 = -2581
    dict_0 = {str_0: set_0, int_0: int_0, int_0: int_0}
    var_1 = module_0.to_namedtuple(dict_0)
    var_2 = module_0.to_namedtuple(var_1)
    var_3 = module_0.to_namedtuple(var_0)


def test_case_7():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    str_0 = "FvEJL`M2w,r1F7="
    none_type_0 = None
    str_1 = "!\\OB"
    dict_0 = {
        str_0: none_type_0,
        str_1: none_type_0,
        str_1: none_type_0,
        str_0: none_type_0,
    }
    ordered_dict_0 = module_1.OrderedDict(**dict_0)
    var_0 = module_0.to_namedtuple(ordered_dict_0)
    int_0 = -1392
    module_0.to_namedtuple(int_0)


def test_case_9():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_10():
    bytes_0 = b"\x05\xe7\xeaV{"
    dict_0 = {bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_11():
    bytes_0 = b"\xff\xa7QVE\x87\x1eB]\xb7\x18\xa7\xb4\xfb\x15\xeeD!-2"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(list_0)
    bool_0 = True
    tuple_0 = (list_0, ordered_dict_0, list_0, bool_0)
    var_1 = module_0.to_namedtuple(tuple_0)
    str_0 = "\ta"
    set_0 = {str_0}
    tuple_1 = (str_0, str_0, set_0)
    var_2 = module_0.to_namedtuple(tuple_1)
    int_0 = -2567
    dict_0 = {str_0: set_0, int_0: int_0}
    var_3 = module_0.to_namedtuple(dict_0)
    var_4 = module_0.to_namedtuple(var_3)
    ordered_dict_1 = module_1.OrderedDict(*var_3)
    module_2.object(*ordered_dict_1, **var_3)
