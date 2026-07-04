class cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"cricket - player: {self.__player}, score:{self.__score}")

    def play(self):
        print(f"{self.__player} hits a six!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"score updated to {self.__score}")
        else:
            print("score cannot be negative.")

class football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"football - player: {self.__player}, score:{self.__score}")

    def play(self):
        print(f"{self.__player} score a goal!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"score updated to {self.__score}")
        else:
            print("score cannot be negative.")   

cricket = cricket("rohit",85)
football = football("arjun",2)

print("=== sports scoreboad ===\n")
for sport in (cricket, football):
    sport.info()
    sport.play()
    print()

print("--- direct change attempt ---")
cricket.__score = 999
print(f"get_score still shows: {cricket.get_score()}")

print("\n --- Updating score ---")
cricket.set_score(100)
football.set_score(3)