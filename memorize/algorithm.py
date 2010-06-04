def interval(repition, rating, easy_factor=2.5):
    ef = easy_factor + (0.1 - (5 - rating) * (0.08 + (5 - rating) * 0.02))
    ef = ef if ef >= 1.3 else 1.3

    if rating < 3:
        return 1, ef
    if repition == 1:
        return 1, ef
    if repition == 2:
        return 6, ef

    i, ef = interval(repition-1, rating, easy_factor)
    i *= easy_factor
    return i, ef
