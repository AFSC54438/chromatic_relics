# 1) (a) (i)
class EventItem():
    def __init__(self, event_name, event_type, event_difficultry):
        self.__EventName = event_name  # String
        self.__Type = event_type  # String
        self.__Difficulty = event_difficultry  # Integer

# ---------------------------------------------------------------------------------------------------
#   1) (a) (ii)
    def GetName(self):
        return self.__EventName

    def GetDifficulty(self):
        return self.__Difficulty

    def GetEventType(self):
        return self.__Type


# ---------------------------------------------------------------------------------------------------
# 1) (c)
class Character():
    def __init__(self, name, jump, swim, run, drive):
        self.__CharacterName = name  # String
        self.__Jump = jump  # Integer
        self.__Swim = swim  # Integer
        self.__Run = run  # Integer
        self.__Drive = drive  # Integer

    def GetName(self):
        self.__CharacterName

# ---------------------------------------------------------------------------------------------------
    # 1) (d)
    def CalculateScore(self, event, difficulty):
        event = event.title()

        if event == "Jump":
            char_skill = self.__Jump
        elif event == "Run":
            char_skill = self.__Run
        elif event == "Swim":
            char_skill = self.__Swim
        elif event == "Drive":
            char_skill = self.__Drive
        else:
            raise ValueError("Invalid Event Name")

        if difficulty not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid Difficultry Score")

        skill_gap = difficulty - char_skill

        if skill_gap <= 0:
            return 100
        elif skill_gap == 1:
            return 80
        elif skill_gap == 2:
            return 60
        elif skill_gap == 3:
            return 40
        elif skill_gap == 4:
            return 20


# ---------------------------------------------------------------------------------------------------
# 1) (b) (i)
Group = []

# ---------------------------------------------------------------------------------------------------
# 1) (b) (ii)
Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mile run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on wall", "jump", 4))

# ---------------------------------------------------------------------------------------------------
# 1) (e) (i)
Tarz = Character("Tarz", 5, 3, 5, 1)
Geni = Character("Geni", 2, 2, 3, 4)

# ---------------------------------------------------------------------------------------------------
# 1) (e) (ii)
tarz_score = 0
geni_score = 0

for count, event in enumerate(Group):
    tarz_win_rate = Tarz.CalculateScore(event.GetEventType(), event.GetDifficulty())
    geni_win_rate = Geni.CalculateScore(event.GetEventType(), event.GetDifficulty())

    print(f"Event {count+1}:")
    if tarz_win_rate > geni_win_rate:
        print(f"-> Tarz wins")
        tarz_score += 1
    elif tarz_win_rate < geni_win_rate:
        print(f"-> Geni wins")
        geni_score += 1
    else:
        print(f"-> Draw")

    print()

print("Final Group Results:")
print(f"-> Tarz: {tarz_score}")
print(f"-> Geni: {geni_score}")

if tarz_score > geni_score:
    print("-> Winner: Tarz")
elif tarz_score < geni_score:
    print("-> Winner: Geni")
else:
    print("-> Draw")
# -------------------------------------------------------------------------------
