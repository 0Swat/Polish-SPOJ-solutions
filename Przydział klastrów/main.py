class System_WIZUT_2009:
    def __init__(self, n, r):
        self.cluster = [r for _ in range(n)]
        self.files = []

    def PokazClustery(self):
        print(self.cluster)

    def PokazPliki(self):
        print(self.files)

    def Komenda(self, data_in):
        print(data_in[0:6])
        #if data_in[0:6] == "CREATE":
        #    a, b = map(str, input().split())
        #if data_in[0:5] == "WRITE":
        #    a, b, c = map(str, input().split())
        #if data_in[0:8] == "TRUNCATE":
        #    a, b, c = map(str, input().split())
        #if data_in[0:6] == "DELETE":
        #    a, b = map(str, input().split())

def main():
    n = int(input())
    r = int(input())
    system1 = System_WIZUT_2009(n, r)
    x = int(input())
    while x:
        data = str(input())
        system1.Komenda(data)
        x-=1
    system1.PokazClustery()
    system1.PokazPliki()
    return

if __name__ == '__main__':
    main()