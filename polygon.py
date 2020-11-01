inf = 10000


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def onseg(a, b, c):
    if min(a.x, c.x) <= b.x <= max(a.x, c.x) and min(a.y, c.y) <= b.y <= max(c.y, a.y):
        return True
    return False


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def dointersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and onseg(p1, p2, q1):
        return True
    if o2 == 0 and onseg(p1, q2, q1):
        return True
    if o3 == 0 and onseg(p2, p1, q2):
        return True
    if o4 == 0 and onseg(p2, q1, q2):
        return True

    return False


def isInside(polygon, p):
    if len(polygon) < 3:
        return False
    last = Point(inf, p.y)

    count = i = 0
    while True:
        next = (i + 1) % len(polygon)
        if dointersect(polygon[i], polygon[next], p, last):
            if orientation(polygon[i], p, polygon[next]) == 0:
                return onseg(polygon[i], p, polygon[next])

            count += 1
        i = next
        if i == 0:
            break
    return count % 2 == 1


# Change this line for polygon entries
polygon = [Point(0,0), Point(0,5), Point(5, 5), Point(5,0)]

# change this line for point entries
p = Point(2.5, 2.5)

print("Inside") if isInside(polygon, p) else print("Outside")
