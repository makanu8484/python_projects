def try_again():
    vote = input("\nDo you want to try again? (T/t/Y/y - Yes; N/n - No): ")
    votes_map = {
        "T": True,
        "t": True,
        "Y": True,
        "y": True,
        "N": False,
        "n": False
    }

    return votes_map[vote]
