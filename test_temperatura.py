from temperatura import fahrenheit_para_celsius, celsius_para_fahrenheit

def test_f_para_c():
    # 32°F deve ser 0°C
    assert round(fahrenheit_para_celsius(32), 2) == 0.0

def test_c_para_f():
    # 0°C deve ser 32°F
    assert round(celsius_para_fahrenheit(0), 2) == 32.0
