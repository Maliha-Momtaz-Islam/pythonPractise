#c = "IoT"
#for item in c:
#    print(item)
class Rev:

    def __init__(self,data): #duita underscore ache , careful
        self.data = data
        self.length = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.length == 0:
            raise StopIteration
        self.length = self.length - 1
        return self.data[self.length]

rev = Rev('DataSoft')
for item in rev:
    print(item)