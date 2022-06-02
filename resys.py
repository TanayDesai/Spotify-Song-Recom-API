from getmatrix import cs_matrix
from getmatrix import data2

datanames = data2['name'].apply(lambda x: x.lower())

class GetSongs:
    def __init__(self,name):
        self.name = str(name) 
        self.songdataidx = datanames[datanames==self.name.lower()].index[0]
        self.songdata = data2.iloc[self.songdataidx]
        print(self.songdata)
        self.allsongs = []


    def getRecom(self):
        cs_data = list(enumerate(cs_matrix[self.songdataidx]))
        cs_data.sort(key=lambda x:x[1],reverse=True)
    
        num = 1
        for i in cs_data[0:25]:
            namesong = data2["name"][i[0]] 
            artist = data2["artist"][i[0]]
            self.allsongs.append(f"{num} {namesong} by {artist}")
            num +=1

        return self.allsongs


# test = GetSongs("bLINDING lIgHTS")
# result = test.getRecom()
# print(result)