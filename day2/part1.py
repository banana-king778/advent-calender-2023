# day 2
# sum of game ids that would have been possible if the bag contained 12 red, 13 green, and 14 blue cubes

games = open("day2/input.txt").read()

rules = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# listify input
inputgames = list(games.split("\n"))

# setup and such - working games is not used, kinda of a placeholder
workinggames = []
failinggames = []

# go through each color of cube and their respective rule to determine games that do not work
for key, value in rules.items():
    i = 0
    # go through each game and remove "Game #:" and split each set into list items
    for games in inputgames:
        ig = inputgames[i].replace(f"Game {i+1}:", "")
        ig = list(ig.split(";"))
        ii = 0
        cubecolor = []
        # find respective color's amount in each set and add to a list
        for games in ig:
            colorindex = ig[ii].find(key)
            ig3 = ig[ii][colorindex - 3:colorindex - 1]
            if colorindex == -1:
                cubecolor += "0"
            else:
                cubecolor += [ig3.replace(" ", "")]
            ii += 1
        # check if the max of the game is possible according to the rules and adding it to list if condition not met
        if int(max(list(map(int, cubecolor)))) > value:
            failinggames += [f"{i+1}"]
        i += 1

# setup more for loops, more for loops, more for loops
sumtotal = 0
i = 0

# find sum of all game #'s that "failed" the predefined conditions of 12 red, 13 green, and 14 blue
for games in list(set(failinggames)):
    sumtotal += int(list(set(failinggames))[i])
    i += 1

# find total of all game #'s assuming all passed the conditions, so the failed ones can be subtracted leaving only the working games #'s
sumofallgames = int((len(inputgames) * (len(inputgames) + 1)) / 2)

print(f"Total Working Games: {sumofallgames - sumtotal}")