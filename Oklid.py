import random
import math

def euclideanDistance(point1: tuple, point2: tuple) -> float:
    distance = math.sqrt(math.pow(abs(point1[0]-point2[0]) ,2)+math.pow(abs(point1[1]-point2[1]) ,2))
    return distance

def main() -> None:
    points = list(tuple())
    distances = list()
    for i in range(10):
        point1 :int = random.randint(0, 50)
        point2 :int = random.randint(0, 50)
        points.append( (point1, point2) )

    for i in points:
        for j in points:
            if i == j:
                continue
            else:
                distance = euclideanDistance(i,j)
                distances.append(distance)
    for i in distances:
        print(i)
    print("min distances = ",min(distances))


if __name__ == "__main__":
    main()
