from src.wordle import check_word


def test_check_word():
    assert check_word("speed", "abide") == (0, 0, 1, 0, 1)
    assert check_word("speed", "erase") == (1, 0, 1, 1, 0)
    assert check_word("speed", "steal") == (2, 0, 2, 0, 0)
    assert check_word("speed", "crepe") == (0, 1, 2, 1, 0)
    assert check_word("speed", "speed") == (2, 2, 2, 2, 2)
    assert check_word("crane", "shard") == (0, 1, 2, 0, 0)
    assert check_word("shtik", "shard") == (2, 2, 0, 0, 0)
    assert check_word("shard", "shard") == (2, 2, 2, 2, 2)
