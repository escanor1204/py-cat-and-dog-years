from app.main import get_human_age


def test_get_cat_and_dog_0_years() -> None:
    cat = 14
    dog = 14
    assert get_human_age(cat, dog) == [0, 0]


def test_get_cat_and_dog_1_year() -> None:
    cat = 15
    dog = 15
    assert get_human_age(cat, dog) == [1, 1]


def test_get_cat_and_dog_2_years() -> None:
    cat = 27
    dog = 28
    assert get_human_age(cat, dog) == [2, 2]


def test_get_cat_and_dog_3_years() -> None:
    cat = 28
    dog = 29
    assert get_human_age(cat, dog) == [3, 3]


def test_get_cat_4_years_and_dog_3_years() -> None:
    cat = 32
    dog = 29
    assert get_human_age(cat, dog) == [4, 3]
