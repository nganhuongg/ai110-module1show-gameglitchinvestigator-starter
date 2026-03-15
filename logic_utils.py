def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # AI helped spot that the range needed to match each difficulty, and I verified the values in the app flow.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "Correct!"

    try:
        # The AI pointed out the hint logic was reversed, and I confirmed it by tracing real guesses against the secret.
        if guess < secret:
            return "Too Low", "Go HIGHER!"
        return "Too High", "Go LOWER!"
    except TypeError:
        # We noticed together that string comparison broke numeric hints, so both values are normalized to ints here.
        g = int(guess)
        s = int(secret)
        if g == s:
            return "Win", "Correct!"
        if g < s:
            return "Too Low", "Go HIGHER!"
        return "Too High", "Go LOWER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        # The AI helped compare both wrong-guess branches, and I used that to make the scoring rule consistent.
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        # I matched this branch with the "Too High" branch after reviewing the inconsistency with AI support.
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    return current_score
