from getmatrix import cs_matrix
from getmatrix import data2, columns

datanames = data2['name'].apply(lambda x: x.lower())

class GetSongs:
    def __init__(self,name):
        self.name = str(name) 
        self.songdataidx = datanames[datanames==self.name.lower()].index[0]
        self.songdata = data2.iloc[self.songdataidx]
        print(self.songdata)
        
    def getRecom(self):
        cs_data = list(enumerate(cs_matrix[self.songdataidx]))
        cs_data.sort(key=lambda x:x[1],reverse=True)
    
        num = 1
        self.final = []
        for i in cs_data[0:25]:
            allsongs = data2.iloc[i[0]].to_dict()
            self.final.append(allsongs)
            num +=1
    
        return self.final

# Testing
# test = GetSongs("traitor")
# result = test.getRecom()
# print(result)