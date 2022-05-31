from getmatrix import cs_matrix
from getmatrix import data2


class GetSongs:
    def __init__(self,name):
        self.name = str(name) 
        self.songdata = data2[data2.name==self.name]
        print(self.songdata)
        self.songdataidx = data2[data2.name==self.name].index[0]
        self.songdatascaled = datascaledarr[self.songdataidx]
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
