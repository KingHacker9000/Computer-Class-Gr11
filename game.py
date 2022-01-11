from random import randint

print('Welcome to 21!\n')

rules = input("Would you like to knoe the rules? [y/n]:\t") == "y"

if rules:
    # Print Rules
    # TODO
    pass

noPlayers = int(input("How many Players? [min: 2]:\t"))
limitInput = input("Limit (default-21):\t")
limit = int(limitInput) if limitInput != "" else 21
playersFinished = 0

players = []
for i in range(noPlayers):
    players.append({
        "score": 0,
        "end": False
    })

while playersFinished < noPlayers:

    for i in range(len(players)):
        player = players[i]
        if not player["end"]:
            print(f"Player {i+1}'s Turn")
            score = player["score"]
            print(f"Current Score: {score} ")
            play = input("Would you like to roll again?\t") == 'y'

            if play:
                num = randint(1,6)
                players[i]["score"] += num
                print(f"Player Rolled.....{num}")
                print(f"Total Score is....{players[i]['score']}")

                if players[i]["score"] == limit:

                    for j in players:
                        j["end"] = True
                        playersFinished += 1
                
                if players[i]["score"] > limit:
                    players[i]["end"] = True 
                    playersFinished += 1

            else:
                players[i]["end"] = True
                playersFinished += 1
        
highscore = {"player": 0, "score": 0}

for i in range(len(players)):
    player = players[i]
    if player["score"] > limit:
        continue
    elif player["score"] == limit:
        highscore = {"player": i+1, "score": limit}
        break
    else:
        if player["score"] > highscore["score"]:
            highscore = {"player": i+1, "score": player["score"]}

print(f"Winner is..................\n{highscore['player']} \nwith a score of ...........\n{highscore['score']}")
