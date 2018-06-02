import random  

class Matrix:
    def __init__(self, q, w):
        self.line = q
        self.pillar = w
        r = 0
        self.array = []
        for i in range(self.line):
            self.array.append([])
            for j in range(self.pillar):
                self.array[i].append(random.randint(0,10))
                r += 1  

    def outMat(self):
        i = 0
        while i != self.line:
            print(self.array[i])
            i += 1
        print('')

    def __add__(self, second):
        if (self.line == second.line) and (self.pillar == second.pillar):
            result = Matrix(self.line, self.pillar)
            for i in range(self.line):
                for j in range(self.pillar):
                    result.array[i][j] = self.array[i][j] + second.array[i][j]
            return result
        else:
            return 1

    def __sub__(self, second):
        if (self.line == second.line) and (self.pillar == second.pillar):
            result = Matrix(self.line, self.pillar)
            for i in range(self.line):
                for j in range(self.pillar):
                    result.array[i][j] = self.array[i][j] - second.array[i][j]
            return result
        else:
            return 1

    def __mul__(self, other):
        if type(other).__name__ == 'int':
            result = Matrix(self.line, self.pillar)
            for i in range(self.line):
                for j in range(self.pillar):
                    result.array[i][j] = self.array[i][j]*other
            return result
        elif self.pillar == other.line:
            result = Matrix(self.line, other.pillar)
            for i in range(self.line):
                for j in range(other.pillar):
                    element = 0
                    for k in range(self.pillar):
                        element += self.array[i][k]*other.array[k][j]
                    result.array[i][j] = element
            return result
        else:
            return 1

    def transporate(self):
        result = Matrix(self.line, self.pillar)
        for j in range(self.pillar):
            for i in range(self.line):
                result.array[j][i] = self.array[i][j]
        self.array = result.array

    def determinant(self):
        result = 0
        if self.line == self.pillar:
            if self.line == 2:
                result = self.array[0][0] * self.array[1][1] - self.array[0][1] * self.array[1][0]
                print(result)
            elif self.line == 3:
                result = self.array[0][0]*self.array[1][1]*self.array[2][2] + self.array[2][0]*self.array[0][1]*self.array[1][2] + self.array[1][0]*self.array[2][1]*self.array[0][2] - self.array[2][0]*self.array[1][1]*self.array[0][2] - self.array[0][0]*self.array[2][1]*self.array[1][2] - self.array[1][0]*self.array[0][1]*self.array[2][2]
                print(result)
        else:
            return 1