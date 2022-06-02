from getmatrix import cs_matrix
from getmatrix import data2

datanames = data2['name'].apply(lambda x: x.lower())

class GetSongs:
    def __init__(self,name):
        self.name = str(name) 
        self.songdataidx = datanames[datanames==self.name.lower()].index[0]
        self.songdata = data2.iloc[self.songdataidx]
        print(self.songdata)
        self.allsongs = {"Artist":[],"Song":[],"Details":[]}


    def getRecom(self):
        cs_data = list(enumerate(cs_matrix[self.songdataidx]))
        cs_data.sort(key=lambda x:x[1],reverse=True)
    
        num = 1
        for i in cs_data[0:25]:  
            self.allsongs["Song"].append(data2["name"][i[0]])
            self.allsongs["Artist"].append(data2["artist"][i[0]])
            num +=1
        self.allsongs["Details"].append(data2.iloc[cs_data[0][0]].to_dict())

        return self.allsongs

# Testing
# test = GetSongs("traitor")
# result = test.getRecom()
# print(result)