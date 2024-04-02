def get_reward(times):
    if times <= 10:
        print("Congratulations, you won a car!")
    elif 10 < times <= 25:
        print("Congratulations, you won a trip!")
    elif 25 < times <= 50:
        print("Congratulations, you've won a consolation prize!")
    else:
        print("Unfortunately, maybe you will be lucky next time...")