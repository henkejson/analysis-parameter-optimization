# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.namedtupleutils as module_0
import collections as module_1


def test_case_0():
    none_type_0 = None
    module_0.to_namedtuple(none_type_0)


def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    tuple_0 = (list_0,)
    var_0 = module_0.to_namedtuple(tuple_0)
    set_0 = set()
    module_0.to_namedtuple(set_0)


def test_case_2():
    ordered_dict_0 = module_1.OrderedDict()
    var_0 = module_0.to_namedtuple(ordered_dict_0)


def test_case_3():
    bytes_0 = b"W\x0c\xdb5\xc6v\xfc\xf1\xbc\xec\x1c~%\xc9\x06\xfdZ\x11"
    module_0.to_namedtuple(bytes_0)


def test_case_4():
    list_0 = []
    var_0 = module_0.to_namedtuple(list_0)


def test_case_5():
    dict_0 = {}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_6():
    str_0 = "dirctorpresent"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)


def test_case_7():
    str_0 = "drctor_presn"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)


def test_case_8():
    ordered_dict_0 = module_1.OrderedDict()
    list_0 = [ordered_dict_0]
    var_0 = module_0.to_namedtuple(list_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(var_0)


def test_case_9():
    tuple_0 = ()
    var_0 = module_0.to_namedtuple(tuple_0)


def test_case_10():
    ordered_dict_0 = module_1.OrderedDict()
    list_0 = [ordered_dict_0]
    var_0 = module_0.to_namedtuple(list_0)


def test_case_11():
    str_0 = "Run the given command and return the result.\n\n        Args:\n             cmd (:obj:`Sequence <typing.Sequence>`): The command\n             **kwargs: Any default_kwargs to pass to :obj:`subprocess.run`.\n                These default_kwargs will override any ``default_kwargs``\n                set in the constructor.\n\n        Raises:\n            FileNotFoundError: If the given ``cmd`` cannot be found.\n            ChildProcessError: If ``raise_error=True`` was set in this\n                class' constructor; and, the process (from running the\n                given ``cmd``) returns a non-zero value.\n            ValueError: If the given ``**kwargs`` has invalid arguments.\n\n        Example:\n\n            >>> from flutils.cmdutils import RunCmd\n            >>> from subprocess import PIPE\n            >>> import os\n            >>> run_command = RunCmd(stdout=PIPE, stderr=PIPE)\n            >>> result = run_command('ls -flap %s' % os.getcwd())\n           >>> result.return_code\n            0\n            >>> result.stdout\n            ...\n            >>> result = run_command('ls -flap %s' % os.path.expanduser('~'))\n        "
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    module_0.to_namedtuple(str_0)


def test_case_12():
    str_0 = "directory_present"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(var_0)
    var_2 = module_0.to_namedtuple(dict_0)
    dict_1 = {var_0: var_0, var_0: var_2}
    var_3 = module_0.to_namedtuple(dict_1)
    var_4 = module_0.to_namedtuple(dict_0)
    var_5 = module_0.to_namedtuple(var_0)
    module_1.namedtuple(var_2, var_2, rename=var_2, defaults=var_2, module=var_2)


def test_case_13():
    bytes_0 = b"\x14"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.to_namedtuple(dict_0)


def test_case_14():
    str_0 = " I8c"
    dict_0 = {str_0: str_0}
    var_0 = module_0.to_namedtuple(dict_0)
    var_1 = module_0.to_namedtuple(dict_0)
    module_1.namedtuple(var_1, dict_0, rename=var_1)
