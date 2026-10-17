def calculate_average(scores):
    if not scores:
        raise ValueError("Scores cannot be empty")

    # Intentional bug: should divide by the number of scores.
    return sum(scores) / (len(scores) + 1)


def get_highest_score(scores):
    if not scores:
        raise ValueError("Scores cannot be empty")

    return max(scores)


def has_passed(score, passing_marks=40):
    return score > passing_marks