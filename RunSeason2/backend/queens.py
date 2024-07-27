'''
def lie_detector(a, b, c, d):
    total_queens = a + b + c + d
    cards = [a, b, c, d]
    max_queens = 4
    liars = 0

    players_list = {}
    for i in range(4):
        player_number = i + 1
        players_list[player_number] = cards[i]

    for count in cards:
        if count > 4:
            liars += 1

    queens_needed = max_queens - total_queens
    if queens_needed > 0:
        liars += queens_needed

    return liars

if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    print(lie_detector(a, b, c, d))
'''

def lie_detector(a, b, c, d):
    cards = [a, b, c, d]
    total_queens = sum(cards)
    max_queens = 4

    if total_queens <= max_queens:
        return 0

    cards.sort(reverse=True)

    liars = 0
    excess = total_queens - max_queens

    for count in cards:
        if excess > 0:
            excess -= min(count, 4)
            liars += 1

    return liars

if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    print(lie_detector(a, b, c, d))
