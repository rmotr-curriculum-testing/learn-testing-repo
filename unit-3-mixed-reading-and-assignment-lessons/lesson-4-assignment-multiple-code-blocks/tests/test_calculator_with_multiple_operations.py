def test_calculator_with_multiple_operations():
    calc = Calculator(
        operations={
            'add': AddOperation,
            'subtract': SubtractOperation
        }
    )
    res = calc.calculate(1, 5, 13, 2, 'add')
    assert res == 21

    res = calc.calculate(13, 3, 7, 'subtract')
    assert res == 3
