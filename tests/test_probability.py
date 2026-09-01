from src.probability import bernoulli_expected_cost


def test_expected_cost():
    assert bernoulli_expected_cost(0.004, 500_000) == 2_000


def test_zero_probability():
    assert bernoulli_expected_cost(0.0, 500_000) == 0.0