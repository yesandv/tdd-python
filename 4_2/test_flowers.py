from flowers import list_to_list_of_tuples, sort_list_of_tuples, list_of_tuples_to_list_of_flowers, find_frequent_flowers


def test_list_to_list_of_tuples():
    list_of_tuples = list_to_list_of_tuples([4, "Тюльпаны", 10, "Нарциссы", 5, "Крокусы", 11, "Примулы", 55])
    assert list_of_tuples == [("Тюльпаны", 10), ("Нарциссы", 5), ("Крокусы", 11), ("Примулы", 55)]


def test_sort_list_of_tuples():
    sorted_list_of_tuples = sort_list_of_tuples([("Тюльпаны", 10), ("Нарциссы", 5), ("Крокусы", 11), ("Примулы", 55)])
    assert sorted_list_of_tuples == [("Примулы", 55), ("Крокусы", 11), ("Тюльпаны", 10), ("Нарциссы", 5)]


def test_list_of_tuples_to_list_of_flowers():
    list_of_flowers = list_of_tuples_to_list_of_flowers([("Примулы", 55), ("Крокусы", 11), ("Тюльпаны", 10), ("Нарциссы", 5)])
    assert list_of_flowers == ["Примулы", "Крокусы", "Тюльпаны", "Нарциссы"]


def test_find_frequent_flowers():
    flowers = find_frequent_flowers([("Тюльпаны", 10), ("Нарциссы", 5), ("Крокусы", 11), ("Примулы", 55)])
    assert flowers == ["Примулы", "Крокусы", "Тюльпаны"]
