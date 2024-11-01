import bmi #Lab2.bmi as bmi
def test_bmi_under_weight():
    result = bmi.calculate_bmi(height=1.60,weight=40)
    test_result=-1
    assert(result == test_result)
def test_bmi_normal_weight():
    result = bmi.calculate_bmi(height=1.60,weight=60)
    test_result=0
    assert(result == test_result)
def test_bmi_over_weight():
    result = bmi.calculate_bmi(height=1.60,weight=80)
    test_result=1
    assert(result == test_result)