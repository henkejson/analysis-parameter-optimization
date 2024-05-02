# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1
import builtins as module_2


def test_case_0():
    float_0 = 2883.3742
    module_0.to_namedtuple(float_0)


def test_case_1():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)
    tuple_0 = (bool_0, bool_0, dict_0)
    var_1 = module_0.to_namedtuple(tuple_0)


def test_case_2():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_3():
    bytes_0 = b"\xcb"
    module_0.to_namedtuple(bytes_0)


def test_case_4():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_5():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_6():
    str_0 = "|4)s6\tS~:7O.F?s2!"
    list_0 = [str_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_7():
    str_0 = "CompletedProcess"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    str_0 = "Ensure the state of the given :obj:`path` is present and a directory.\n\n    This function processes the given ``path`` with\n    :obj:`~flutils.normalize_path`.\n\n    If the given ``path`` does **NOT** exist, it will be created as a\n    directory.\n\n    If the parent paths of the given ``path`` do not exist, they will also be\n    created with the ``mode``, ``user`` and ``group``.\n\n    If the given ``path`` does exist as a directory, the ``mode``, ``user``,\n    and :``group`` will be applied.\n\n    Args:\n        path (:obj:`str`, :obj:`bytes` or :obj:`Path <pathlib.Path>`):\n            The path of the directory.\n        mode (:obj:`int`, optional): The mode applied to the ``path``.\n            Defaults to ``0o700``.\n        user (:obj:`str` or :obj:`int`, optional): The \"login name\" used to\n            set the owner of the given ``path``.  A value of ``'-1'`` will\n            leave the owner unchanged.  Defaults to the \"login name\" of the\n            current user.\n        group (:obj:`str` or :obj:`int`, optional): The group name used to set\n            the group of the given ``path``.  A value of ``'-1'`` will leave\n            the group unchanged.  Defaults to the current user's group.\n\n    Raises:\n        ValueError: if the given ``path`` contains a glob pattern.\n        ValueError: if the given ``path`` is not an absolute path.\n        FileExistsError: if the given ``path`` exists and is not a directory.\n        FileExistsError: if a parent of the given ``path`` exists and is\n            not a directory.\n\n    :rtype: :obj:`Path <pathlib.Path>`\n\n        * :obj:`PosixPath <pathlib.PosixPath>` or\n          :obj:`WindowsPath <pathlib.WindowsPath>` depending on the system.\n\n        .. Note:: :obj:`Path <pathlib.Path>` objects are immutable. Therefore,\n           any given ``path`` of type :obj:`Path <pathlib.Path>` will not be\n           the same object returned.\n\n    Example:\n        >>> from flutils.pathutils import directory_present\n        >>> directory_present('~/tmp/test_path')\n        PosixPath('/Users/len/tmp/test_path')\n\n    "
    ordered_dict_0 = module_1.OrderedDict()
    tuple_0 = (str_0, ordered_dict_0)
    var_0 = module_0.to_namedtuple(tuple_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_0)


def test_case_9():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_10():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_11():
    str_0 = "\\*SL0<p/AIaNjxc"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    bool_0 = True
    list_0 = [dict_0]
    tuple_0 = (bool_0, bool_0)
    tuple_1 = (list_0,)
    var_1 = module_0.to_namedtuple(tuple_1)
    var_2 = module_0.to_namedtuple(tuple_0)
    str_1 = "B+`4hs0[W]7B`5pK!"
    var_3 = module_0.to_namedtuple(var_2)
    module_0.to_namedtuple(str_1)


def test_case_12():
    bytes_0 = b"\x11;\xc0\xb0\xf8'=I+\xaa\xc3\xe2X\xe8\xfbWq\xff"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    list_0 = [dict_0, bytes_0, bytes_0, dict_0]
    module_0.to_namedtuple(list_0)


def test_case_13():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)
    str_0 = " t"
    ordered_dict_0 = module_1.OrderedDict()
    tuple_1 = (ordered_dict_0, str_0)
    var_1 = module_0.to_namedtuple(tuple_1)
    object_0 = module_2.object()
    dict_0 = {tuple_0: tuple_1, str_0: ordered_dict_0}
    var_2 = module_0.to_namedtuple(dict_0)
    var_3 = module_0.to_namedtuple(var_2)
    tuple_2 = (var_3,)
    var_4 = module_0.to_namedtuple(ordered_dict_0)
    var_5 = module_0.to_namedtuple(tuple_2)
    str_1 = "B+`4hs0[W]7B`5pK!"
    object_1 = module_2.object(**ordered_dict_0)
    module_0.to_namedtuple(str_1)
