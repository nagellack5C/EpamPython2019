"""
Написать тесты(pytest) к предыдущим 3 заданиям, запустив которые, я бы смог бы проверить их корректность
"""

import pytest
import unittest
from task1 import PrintableFile, PrintableFolder
from task2 import Graph
from task3 import ShiftDescriptor


@pytest.fixture
def task1_folder_with_contents():
    file1 = PrintableFile("file1")
    file2 = PrintableFile("file2")
    file3 = PrintableFile("file3")
    file4 = PrintableFile("file4")
    file5 = PrintableFile("file5")

    folder1 = PrintableFolder("folder1")
    folder2 = PrintableFolder("folder2", [file1])
    folder3 = PrintableFolder("folder3", [folder1, file3, file2])
    folder4 = PrintableFolder("folder4", [folder2])
    folder5 = PrintableFolder("folder5", [folder4, file4, folder3])
    return folder5


def test_task1_value_types():
    # check initialization with correct params
    assert PrintableFile("test")
    assert PrintableFolder("test")
    test_file = PrintableFile("test_file")
    test_dir1 = PrintableFolder("folder1", test_file)
    test_dir2 = PrintableFolder("folder2", test_dir1)

    # check that __contains__ works ok
    assert test_file in test_dir1
    assert test_dir1 in test_dir2
    assert test_file in test_dir2
    assert test_dir2 not in test_dir1

    # check that exceptions are raised with bad params
    with pytest.raises(TypeError):
        bad_values = [1, ValueError, False, []]
        for i in bad_values:
            assert PrintableFile(i)
            assert PrintableFolder(i)
            assert PrintableFolder("test", i)


def test_task1_printing(task1_folder_with_contents):
    lines = str(task1_folder_with_contents).split("\n")
    assert 0 == lines[0].count("|")
    assert 2 == lines[1].count("|") == lines[4].count("|")\
           == lines[5].count("|")
    assert 3 == lines[2].count("|") == lines[6].count("|")\
           == lines[7].count("|") == lines[8].count("|")
    assert 4 == lines[3].count("|")


@pytest.fixture
def task2_dicts():
    good_dict = {
        'A': ['B', 'C', 'D'],
        'B': ['C'],
        'C': ['E', 'G'],
        'E': ['A'],
        'G': [],
        'D': ['A']
    }
    bad_dict = {
        'A': 'X',
        'B': 'Y'
    }
    not_a_dict = [1, ValueError, False, []]
    test_dict = {
        "good dict": good_dict,
        "bad dict": bad_dict,
        "not a dict": not_a_dict
    }
    return test_dict


def test_task2_values(task2_dicts):
    assert Graph(task2_dicts["good dict"])
    with pytest.raises(TypeError):
        assert Graph(task2_dicts["bad dict"])
        for i in task2_dicts["not a dict"]:
            assert Graph(i)


def test_task2_iterates(task2_dicts):
    assert [vert for vert in Graph(task2_dicts["good dict"])]\
           == list("ABCDEG")
    # test a not-connected graph, should return first node only
    assert "".join([vert for vert in Graph({"A": [], "B": []})]) == "A"


def test_task3():
    class Caesar:
        cypher = ShiftDescriptor(7)
        anticypher = ShiftDescriptor(-7)

    c = Caesar()
    # test that ShiftDescriptor works with negative values and that
    # it shifts correctly
    c.cypher = "cypher"
    assert c.cypher == "jfwoly"
    c.anticypher = c.cypher
    assert c.anticypher == "cypher"

    with pytest.raises(TypeError):
        c.cypher = 123
    with pytest.raises(ValueError):
        c.cypher = "123"
