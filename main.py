# Season simulator

import random

def run_match(team1, team2):
    score1 = random.randint(0,team1[0])
    score2 = random.randint(0,team2[0])
    team1[4] = ((team1[4] * (team1[1] + team1[2] + team1[3])) + score1) / ((team1[1] + team1[2] + team1[3]) + 1)
    team2[4] = ((team2[4] * (team2[1] + team2[2] + team2[3])) + score2) / ((team2[1] + team2[2] + team2[3]) + 1)

    if score1 < score2:
        team1[2]+=1
        team2[1]+=1
    elif score1 > score2:
        team1[1]+=1
        team2[2]+=1
    else:
        team1[3]+=1
        team2[3]+=1
    print("Team #" + str(team1[0]) + ": " + str(score1) + "Team #" + str(team2[0]) + ": " + str(score2))

def run_season(teams):
    n = len(teams)
    for i in range(10,31):
        for j in range(i+1,31):
            run_match(teams[i],teams[j])


if __name__ == '__main__':
    # Declare 20 teams
    measure = {x: [x,0,0,0,0] for x in range(10,31)}
    # Print teams
    for x in measure:
        print(measure[x][0])

    run_season(measure)

    for x in measure:
        measure[x][4] = round(measure[x][4],1)
        print(measure[x])

    for elem in sorted(measure.items(), key=lambda x: x[1][1]+.5*x[1][3]):
        # print(str(elem[0]) + ":: " + str(elem[1]) + "-" + str(elem[2]) + "-" +str(elem[3]))
        print(elem)

