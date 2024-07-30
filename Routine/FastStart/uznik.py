'''
def brick_helper(lst):
    brick = [lst[0], lst[1], lst[2]]
    hole = [lst[3], lst[4]]

    p_m = hole[0] * hole[1]
    brick_s1 = lst[0] * lst[1]
    brick_s2 = lst[0] * lst[2]
    brick_s3 = lst[1] * lst[2]

    if brick_s1 <= p_m or brick_s2 <= p_m or brick_s3 <= p_m:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    lst = [a, b, c, d, e]
    print(brick_helper(lst))
'''
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if (A <= D and B <= E) or (A <= E and B <= D) or \
   (A <= D and C <= E) or (A <= E and C <= D) or \
   (B <= D and C <= E) or (B <= E and C <= D):
    print("YES")
else:
    print("NO")
