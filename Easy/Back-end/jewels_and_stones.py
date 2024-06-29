import sys


def jewels_and_stones(jevels, stones):
    counter = 0
    for stone in stones:
        if stone in jewels:
            counter += 1
    print(counter)
    
jewels = input()
stones = input()

if __name__ == '__main__':
    jewels_and_stones(jewels, stones)
