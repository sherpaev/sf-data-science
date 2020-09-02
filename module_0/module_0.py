import numpy as np

MAX_NUMBER = 100
COUNT_OF_RUNS = 1000


def game_core_binary(number_to_guess):
    """Binary search approach.
    Set the first predict value as the middle of interval, i.e. 50.
    Then decrease or increase the predict number by step.
    The step is calculated using the check interval divided by 2,
    i.e. 25, 13 ... 1
    The minimum step is always 1.
    The function return count of guesses"""
    count_guesses = 1
    predict = step = round(MAX_NUMBER / 2)

    while number_to_guess != predict:
        count_guesses += 1
        step = round(step / 2) if step > 1 else 1

        if number_to_guess > predict:
            predict += step
        elif number_to_guess < predict:
            predict -= step
    return count_guesses


def score_game(game_core):
    """Run game COUNT_OF_RUNS times, to know, how quickly the game guesses number"""
    scores = []
    random_numbers = np.random.randint(1, MAX_NUMBER + 1, size=COUNT_OF_RUNS)
    for number in random_numbers:
        scores.append(game_core(number))
    score = int(np.mean(scores))
    print(f"Your algorithm guesses the average number of {score} attempts")
    return score


score_game(game_core_binary)
