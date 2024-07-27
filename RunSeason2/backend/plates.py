def find_room_plates(B, W):
    for n in range(3, 2001):
        for k in range(1, n + 1):
            black_tiles = 2 * n + 2 * k - 4
            if black_tiles == B and n * k - black_tiles == W:
                print(n, k)
    return None

if __name__ == '__main__':
    B, W = map(int, input().split())
    find_room_plates(B, W)
