import sys

def main():
    set_data = set()
    lines = [line for line in sys.stdin.read().split()]
    for word in lines:
        set_data.add(word)
    return len(set_data)

if __name__ == '__main__':
    print(main())
