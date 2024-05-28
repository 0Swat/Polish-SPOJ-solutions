import math

class Field:
    def __init__(self, n):
        self.triangles = []

        for i in range(1, n+1):
            vertex = []
            x, y = map(int, input().split())
            vertex.append(i)
            vertex.append(x)
            vertex.append(y)
            self.triangles.append(vertex)
        
        while self.triangles:
            self.Graham()
        

    def Graham(self):
        self.triangles.sort(key=lambda x: x[1])

        triangle = []
        triangle.append(self.triangles[0])
        maks = [False, 0]
        min = [False, 0]
        for i in range(1, len(self.triangles)):
            vector = (self.triangles[i][1] - self.triangles[0][1], self.triangles[i][2] - self.triangles[0][2])
            angle = math.atan2(vector[1], vector[0])

            if maks[0] == False:
                maks[0] = self.triangles[1]
                maks[1] = angle
            else:
                if maks[1] < angle:
                    maks[0] = self.triangles[i]
                    maks[1] = angle

            if min[0] == False:
                min[0] = self.triangles[1]
                min[1] = angle
            else:
                if min[1] > angle:
                    min[0] = self.triangles[i]
                    min[1] = angle

        triangle.append(min[0])
        triangle.append(maks[0])
        triangle.sort(key=lambda x: x[0])

        print(str(triangle[0][0]) + " " + str(triangle[1][0]) + " " + str(triangle[2][0]))

        self.triangles.pop(0)
        self.triangles.remove(min[0])
        self.triangles.remove(maks[0])


def main():
    d= int(input())
    while d:
        n = int(input())
        Field(n)
        d-=1

if __name__ == '__main__':
    main()