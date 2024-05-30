class System_WIZUT_2009:
    def __init__(self, n, r):
        self.cluster_size = r
        self.cluster = r * n
        self.files = []

    def PokazClustery(self):
        return int(self.cluster / self.cluster_size)

    def file_exists(self, filename):
        return any(file[0] == filename for file in self.files)
    
    def Komenda(self, data_in):
        command_parts = data_in.split()
        command = command_parts[0]
        if command == "CREATE":
            self.Create(command_parts[1])
        elif command == "WRITE":
            self.Write(command_parts[1], int(command_parts[2]))
        elif command == "TRUNCATE":
            self.Truncate(command_parts[1], int(command_parts[2]))
        elif command == "DELETE":
            self.Delete(command_parts[1])

    def Create(self, name):
        if self.file_exists(name):
            #print("Istnieje już taki plik")
            return
        else:
            file = [name, 0]
            self.files.append(file)
    
    def Write(self, name, size):
        if not self.file_exists(name):
            #print("Taki plik nie istnieje")
            return
        elif size > self.cluster:
            #print("Brak miejsca")
            return
        else:
            for file in self.files:
                if file[0] == name:
                    file[1] += size
                    self.cluster -= size
                    break

    def Truncate(self, name, size):
        if not self.file_exists(name):
            #print("Taki plik nie istnieje")
            return
        else:
            for file in self.files:
                if file[0] == name:
                    if file[1] < size:
                        #print("Za mały rozmiar pliku")
                        return
                    else:
                        file[1] -= size
                        self.cluster += size
                        break

    def Delete(self, name):
        if not self.file_exists(name):
            #print("Taki plik nie istnieje")
            return
        else:
           for file in self.files:
                if file[0] == name:
                    self.cluster += file[1]
                    self.files.remove(file)


                


def main():
    n = int(input())
    r = int(input())
    system1 = System_WIZUT_2009(n, r)
    x = int(input())
    while x:
        data = str(input())
        system1.Komenda(data)
        x-=1
    while True:
        try:
            data = str(input())
            system1.Komenda(data)
            x-=1
        except EOFError:
            break
    print(system1.PokazClustery())

if __name__ == '__main__':
    main()