# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()


def test_case_2():
    int_0 = 239
    timer_0 = module_0.Timer(initial_text=int_0)
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()
    timer_0.stop()


def test_case_3():
    int_0 = 244
    timer_0 = module_0.Timer(initial_text=int_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_4():
    int_0 = 244
    timer_0 = module_0.Timer(initial_text=int_0)
    none_type_0 = timer_0.start()
    timer_0.start()


def test_case_5():
    int_0 = 244
    timer_0 = module_0.Timer(initial_text=int_0)
    str_0 = "hw@h{()~>..*AE>"
    timer_1 = module_0.Timer(str_0, timer_0)
    none_type_0 = timer_1.start()
    float_0 = timer_1.stop()
    timer_0.__exit__(*timer_0)


def test_case_6():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    list_0 = [none_type_1]
    none_type_2 = timer_0.__exit__(*list_0)
    var_0 = timer_0.__eq__(timer_0)
    var_1 = var_0.__eq__(none_type_2)
    var_0.popitem()


def test_case_7():
    int_0 = 244
    timer_0 = module_0.Timer(initial_text=int_0)
    none_type_0 = timer_0.start()


def test_case_8():
    str_0 = "Rea,"
    timer_0 = module_0.Timer(initial_text=str_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_9():
    int_0 = 244
    timer_error_0 = module_0.TimerError()
    int_1 = 244
    bool_0 = True
    tuple_0 = (int_0, timer_error_0, bool_0)
    list_0 = [int_0, int_1, tuple_0, timer_error_0]
    timer_error_1 = module_0.TimerError(*list_0)
    bool_1 = True
    timer_0 = module_0.Timer(int_1, timer_error_1, bool_1)
    none_type_0 = timer_0.start()
    timer_0.__exit__()
