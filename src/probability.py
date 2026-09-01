def bernoulli_expected_cost(probability, benefit):
    if not 0 <= probability <= 1:
        raise ValueError("probability must be between 0 and 1")
    if benefit < 0:
        raise ValueError("benefit must be nonnegative")
    return probability * benefit