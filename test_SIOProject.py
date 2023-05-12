import pandas
import filecmp
import pytest
import SIOProject_Part1


def test_pytest_install():
    assert 3 <= 5


def test_reading_normal_file():
    '''
    Test if read_file() can parse a normally formatted file.
    '''
    test_df = SIOProject.read_file("example.txt")
    real_df = pandas.read_csv("example.txt", sep="\t")
    print(test_df)


def test_reading_empty_file():
    '''
    Test behavior of read_file() if given an empty or non-existent file.
    '''
