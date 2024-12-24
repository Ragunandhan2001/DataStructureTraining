print("Hash Map")
class HashMap:

    def __init__(self,size):
        self.size = size
        self.hashlist = [None]*self.size

    def GetIndex(self,key):
        index=hash(key) % self.size
        return index

    def __setitem__(self, key, value):
        Index = self.GetIndex(key)

        if self.hashlist[Index] is None:
            self.hashlist[Index] = [[key,value]]
        else:
            # if self.hashlist[Index]  is not None:
            self.hashlist.append([key,value])

    def __getitem__(self, key):
        Index=self.GetIndex(key)
        if self.hashlist[Index] is not None:
            sublist = self.hashlist[Index]
            for pair in sublist:
                if pair[0] == key:
                    return pair[1]

    def __delitem__(self, key):
        Index = self.GetIndex(key)

        if self.hashlist[Index] is not None:
            sublist = self.hashlist[Index]
            for i,pair in enumerate(sublist):
                if pair[i] == key:
                    del sublist[i]
hm=HashMap(10)
hm['name'] = "mani"
hm["age"] =100
del hm["name"]
print(hm.hashlist)

