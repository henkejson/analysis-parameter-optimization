# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import builtins as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(logger=timer_error_0)
    var_0 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_3():
    str_0 = "Zqc\r8WM_U^e"
    list_0 = [str_0, str_0]
    timer_0 = module_0.Timer(text=list_0)
    timer_0.stop()


def test_case_4():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(logger=timer_error_0)
    var_0 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=var_0, initial_text=timer_1)
    var_0.copy()


def test_case_5():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    float_arg_0 = module_0.FloatArg()
    none_type_0 = timer_0.start()
    object_0 = module_1.object()
    timer_error_1 = module_0.TimerError()
    var_0 = object_0.__eq__(timer_error_1)
    module_0.FloatArg(*object_0)


def test_case_6():
    str_0 = "k7xm"
    bool_0 = True
    timer_0 = module_0.Timer(str_0, initial_text=str_0, logger=bool_0)
    timer_0.__enter__()


def test_case_7():
    timer_error_0 = module_0.TimerError()
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=timer_error_0, logger=none_type_0)
    var_0 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    timer_0.__enter__()


def test_case_8():
    int_0 = 10
    timer_error_0 = module_0.TimerError()
    int_1 = -762
    var_0 = timer_error_0.__eq__(int_1)
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, var_0, timer_error_0)
    float_arg_0 = module_0.FloatArg()
    timer_1 = module_0.Timer(int_0, int_0, logger=int_0)
    none_type_1 = timer_0.start()
    timer_2 = timer_1.__enter__()
    object_0 = module_1.object()
    timer_error_1 = module_0.TimerError()
    timer_1.stop()


def test_case_9():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    var_0 = timer_0.__eq__(timer_0)
    timer_1 = timer_0.__enter__()
    object_0 = module_1.object()
    timer_error_1 = module_0.TimerError()
    float_0 = timer_1.stop()
    none_type_0 = timer_0.start()
    var_1 = object_0.__eq__(timer_error_1)
    var_0.stop()


def test_case_10():
    int_0 = 0
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    float_arg_0 = module_0.FloatArg()
    timer_1 = module_0.Timer(int_0, int_0, logger=int_0)
    none_type_0 = timer_0.start()
    timer_2 = timer_1.__enter__()
    object_0 = timer_2.__eq__(float_arg_0)
    timer_error_1 = timer_1.__eq__(float_arg_0)
    float_0 = timer_1.stop()
    timer_3 = timer_1.__enter__()
    timer_3.start()


def test_case_11():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    float_arg_0 = module_0.FloatArg()
    timer_1 = module_0.Timer(timer_0, timer_0, logger=timer_0)
    none_type_0 = timer_0.start()
    timer_2 = timer_1.__enter__()
    object_0 = module_1.object()
    timer_error_1 = module_0.TimerError()
    timer_1.stop()
