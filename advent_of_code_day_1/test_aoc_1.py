from aoc_1 import findMostCals

def test_worksWithOneElfWithOneValue():
    assert findMostCals(['1', '']) == 1

def test_worksWithArrayWithoutEndingEmptyLine():
    assert findMostCals(['1']) == 1

def test_worksWithOneElfWithMultipleValues():
    assert findMostCals(['1', '3']) == 4

def test_worksWithTwoElfsWithOneValue():
    assert findMostCals(['1', '', '3']) == 3

def test_worksWithExampleTest():
    inputArray = ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']
    assert findMostCals(inputArray) == 24000