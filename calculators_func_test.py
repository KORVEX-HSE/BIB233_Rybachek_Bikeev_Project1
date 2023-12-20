import pytest
from calculators_funk import *

def test_calculator_1():
    assert calculator_1(25, 170, 70, 'middle', 'man') == 2546
    assert calculator_1(30, 160, 60, 'low', 'woman') == 1772
    assert calculator_1(35, 180, 80, 'hard', 'man') == 3027
    assert calculator_1(40, 165, 55, 'very_low', 'woman') == 1464

def test_calculate_macros():
    assert calculate_macros(25, 170, 60, 'low', 'man', 'gain') ==  [189, 56, 315, 2521]
    assert calculate_macros(30, 160, 55, 'middle', 'woman', 'loss') == [209, 28, 146, 1670]
    assert calculate_macros(35, 180, 70, 'hard', 'man', 'balance') == [214, 95, 286, 2855]
    assert calculate_macros(40, 165, 65, 'very_low', 'woman', 'gain') == [138, 41, 229, 1834]

def test_difference():
    vals_r = [160, 31, 267, 2532]
    vals_f = [150, 25, 280, 2400]
    assert difference(vals_r, vals_f) == [['ниже на', 10], ['ниже на', 6], ['больше на', 13], ['ниже на', 132]]
    
    vals_r = [112, 14, 224, 1304]
    vals_f = [120, 18, 210, 1400]
    assert difference(vals_r, vals_f) == [['больше на', 8], ['больше на', 4], ['ниже на', 14], ['больше на', 96]]
    
    vals_r = [240, 71, 320, 3200]
    vals_f = [240, 70, 320, 3200]
    assert difference(vals_r, vals_f) == [['столько же,сколько ожидалось', 0], ['ниже на', 1], ['столько же,сколько ожидалось', 0], ['столько же,сколько ожидалось', 0]]
    
    vals_r = [91, 10, 182, 1440]
    vals_f = [95, 12, 180, 1500]
    assert difference(vals_r, vals_f) == [['больше на', 4], ['больше на', 2], ['ниже на', 2], ['больше на', 60]]


def test_consumed_now():
    assert consumed_now(55,1,0,13,100) == [55, 1, 0, 13]
    assert consumed_now(275,11.9,012.4,29,350) == [962, 38, 42, 102]
    assert consumed_now(113,23.6,2,0,250) == [282, 58, 5, 0]
    assert consumed_now(346,12,3,75,150) == [519, 18, 4, 112]