def calculator():
    players_count = int(input())
    players = []

    for _ in range(players_count):
        name = input()
        players.append(name)

    goals_dict = {name: 0 for name in players}
    goals_counter = int(input())

    prewious_score_home = 0
    prewious_score_away = 0

    for _ in range(goals_counter):
        score, name = input().split()
        score_home, score_away = map(int, score.split(':'))
        if name in goals_dict:
            if prewious_score_home < score_home:
                goals_dict[name] += (score_home - prewious_score_home)
                prewious_score_home = score_home
            elif prewious_score_away < score_away:
                goals_dict[name] += (score_away - prewious_score_away)
                prewious_score_away = score_away

    max_goals = -1
    best_player = ''

    for player, goals in goals_dict.items():
        if (goals > max_goals) or (goals == max_goals and player > best_player):
            max_goals = goals
            best_player = player

    print(best_player, max_goals)

if __name__ == '__main__':
    calculator()
