# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.packages as module_0


def test_case_0():
    module_0._VersionInfo()


def test_case_1():
    str_0 = "1604.5826682219338"
    str_1 = module_0.bump_version(str_0)


def test_case_2():
    str_0 = "1604.58266821338"
    module_0.bump_version(str_0, pre_release=str_0)


def test_case_3():
    str_0 = "1604.5826682219338.2"
    str_1 = module_0.bump_version(str_0)


def test_case_4():
    str_0 = "1604.5826682219338"
    int_0 = 163
    module_0.bump_version(str_0, int_0)


def test_case_5():
    str_0 = "1604.5826682219338"
    str_1 = module_0.bump_version(str_0)
    int_0 = -1573
    module_0.bump_version(str_0, int_0)


def test_case_6():
    str_0 = "1.586a82193"
    str_1 = module_0.bump_version(str_0)


def test_case_7():
    bool_0 = True
    str_0 = "1625.2946168973915"
    str_1 = module_0.bump_version(str_0, bool_0)


def test_case_8():
    bool_0 = False
    str_0 = "1625.2946168973915"
    str_1 = module_0.bump_version(str_0, bool_0)


def test_case_9():
    str_0 = "1.8a82193"
    bool_0 = True
    str_1 = module_0.bump_version(str_0, bool_0)
    module_0.bump_version(str_0, pre_release=str_0)
