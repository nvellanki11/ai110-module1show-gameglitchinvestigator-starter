from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


# ---------------------------------------------------------------------------
# check_guess — base cases
# ---------------------------------------------------------------------------
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# check_guess — edge cases (regression for the string-comparison glitch)
def test_check_guess_no_lexicographic_comparison():
    # "9" > "100" lexicographically, but 9 < 100 numerically -> must be Too Low
    assert check_guess(9, 100) == "Too Low"
    # 100 vs 9: must be Too High
    assert check_guess(100, 9) == "Too High"


def test_check_guess_boundaries():
    assert check_guess(1, 1) == "Win"
    assert check_guess(2, 1) == "Too High"
    assert check_guess(0, 1) == "Too Low"


# ---------------------------------------------------------------------------
# get_range_for_difficulty
# ---------------------------------------------------------------------------
def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_range_unknown_defaults_to_normal():
    assert get_range_for_difficulty("???") == (1, 100)


# ---------------------------------------------------------------------------
# parse_guess
# ---------------------------------------------------------------------------
def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert err == "Enter a guess."


def test_parse_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."


def test_parse_float_is_truncated():
    ok, value, err = parse_guess("3.9")
    assert ok is True
    assert value == 3


def test_parse_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5


# ---------------------------------------------------------------------------
# update_score — regression for the "Too High" parity glitch (issue 5)
# ---------------------------------------------------------------------------
def test_too_high_always_penalizes():
    # Must subtract regardless of attempt parity (used to add on even attempts)
    assert update_score(100, "Too High", attempt_number=2) == 95
    assert update_score(100, "Too High", attempt_number=3) == 95


def test_too_low_penalizes():
    assert update_score(100, "Too Low", attempt_number=1) == 95


def test_too_high_and_too_low_match():
    # Both wrong outcomes should change the score identically
    assert update_score(50, "Too High", 4) == update_score(50, "Too Low", 4)


def test_win_adds_points():
    # Winning increases the score
    assert update_score(0, "Win", attempt_number=1) > 0


def test_win_points_have_floor():
    # Points never drop below the 10-point floor, even on a late win
    assert update_score(0, "Win", attempt_number=20) == 10


def test_unknown_outcome_leaves_score_unchanged():
    assert update_score(77, "Mystery", attempt_number=1) == 77
