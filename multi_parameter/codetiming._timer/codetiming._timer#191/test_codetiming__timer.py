# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    str_0 = "9tN3J$N66Xm:n"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()


def test_case_2():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__repr__()
    timer_0.stop()


def test_case_3():
    bool_0 = False
    timer_0 = module_0.Timer(logger=bool_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    timer_0.__exit__()


def test_case_4():
    none_type_0 = None
    bool_0 = False
    str_0 = "F,mjo{NJp\nep8~,E52>o"
    timer_0 = module_0.Timer(none_type_0, none_type_0, bool_0, str_0)
    timer_1 = timer_0.__enter__()


def test_case_5():
    none_type_0 = None
    bool_0 = True
    str_0 = "F,mjo{NJp\nep8~,E52>o"
    timer_0 = module_0.Timer(none_type_0, none_type_0, bool_0, str_0)
    timer_0.__enter__()


def test_case_6():
    str_0 = "9tN3J$N66Xm:n"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__repr__()
    timer_1.__enter__()


def test_case_7():
    float_0 = -2161.878907
    str_0 = "milliseconds"
    var_0 = module_1.field(default=str_0, compare=str_0)
    var_1 = float_0.__eq__(float_0)
    bool_0 = True
    str_1 = "F,mjo{NJp\nep8~,E52>o"
    timer_0 = module_0.Timer(var_0, var_0, bool_0, str_1)
    timer_0.__enter__()


def test_case_8():
    str_0 = "9tN3J$N66Xm:n"
    timer_0 = module_0.Timer(str_0)
    none_type_0 = None
    var_0 = module_1.dataclass(eq=str_0, unsafe_hash=none_type_0, frozen=none_type_0)
    timer_1 = timer_0.__enter__()
    none_type_1 = timer_0.__exit__()
    var_0.get(timer_1)


def test_case_9():
    str_0 = "9tN3J$N66Xm:n"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = module_0.Timer(text=timer_0)
    timer_2 = timer_1.__enter__()
    none_type_0 = timer_2.__exit__()
