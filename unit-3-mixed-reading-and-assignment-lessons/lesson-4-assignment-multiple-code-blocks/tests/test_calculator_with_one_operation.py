def test_calculator_with_one_operation():
    calc = Calculator(
        operations={
            'add': AddOperation
        }
    )
    res = calc.calculate(1, 5, 13, 2, 'add')
    assert res == 21
