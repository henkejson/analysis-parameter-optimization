# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import builtins as module_1
import dataclasses as module_2


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    none_type_0 = timer_0.start()
    timer_0.start()


def test_case_2():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_3():
    bool_0 = False
    none_type_0 = None
    timer_0 = module_0.Timer(text=bool_0, logger=none_type_0)
    timer_0.__exit__()


def test_case_4():
    float_arg_0 = module_0.FloatArg()
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = timer_0.__enter__()
    timer_0.start()


def test_case_5():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    none_type_0 = timer_0.start()


def test_case_6():
    str_0 = "Definition of Timer.\n\nSee help(codetiming) for quick instructions, and\nhttps://pypi.org/project/codetiming/ for more details.\n"
    timer_0 = module_0.Timer(initial_text=str_0)
    none_type_0 = timer_0.start()
    str_1 = "eUZ]2v5]bz1peD"
    list_0 = [timer_0, str_1, str_0]
    var_0 = timer_0.__repr__()
    exception_0 = module_1.Exception(*list_0)
    list_1 = [exception_0, str_1, str_1, list_0]
    none_type_1 = timer_0.__exit__(*list_1)
    none_type_2 = None
    timer_1 = module_0.Timer(initial_text=none_type_2, logger=none_type_2)
    var_1 = timer_1.__repr__()
    timer_2 = module_0.Timer()
    none_type_3 = timer_2.start()
    none_type_4 = timer_2.__exit__()
    timer_error_0 = module_0.TimerError()
    timer_2.stop()


def test_case_7():
    timer_error_0 = module_0.TimerError()
    bool_0 = True
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=none_type_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    var_0 = timer_1.__call__(bool_0)
    none_type_1 = timer_0.__exit__()
    var_1 = var_0.__repr__()
    module_2.field(hash=timer_1, metadata=bool_0)


def test_case_8():
    bool_0 = True
    str_0 = ";'3p"
    timer_0 = module_0.Timer(str_0, initial_text=bool_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    timer_1.__exit__()


def test_case_9():
    bool_0 = True
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer(initial_text=bool_0)
    timer_2 = module_0.Timer(text=timer_1)
    timer_3 = timer_2.__enter__()
    var_0 = timer_1.__call__(bool_0)
    none_type_0 = timer_2.__exit__()
    var_1 = var_0.__repr__()
    module_2.field(default=none_type_0, compare=var_1, metadata=timer_3)
