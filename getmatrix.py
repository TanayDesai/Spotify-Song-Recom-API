import pandas as pd
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler


data = pd.read_csv("Spotify-Songs-Data.csv")
columns = ["release_date","popularity","danceability","acousticness","energy","instrumentalness","liveness","loudness","speechiness"]

scaler = MinMaxScaler()
for i in columns:
  data[i] = scaler.fit_transform(np.array(data[i]).reshape(-1,1))

####################################
datascaled = data[columns][:2200]
datascaledarr = np.array(datascaled)

vsm1 = cosine_similarity(datascaledarr,datascaledarr)
vsm1array = np.array(vsm1)
print(vsm1array.nbytes/1000000000,"GB")

#####################################
# datascaled = data[columns][5000:10000]
# datascaledarr = np.array(datascaled)

# vsm2 = cosine_similarity(datascaledarr,datascaledarr)
# vsm2array = np.array(vsm2)
# print(vsm2array.nbytes/1000000000)

######################################
# datascaled = data[columns][10000:12000]
# datascaledarr = np.array(datascaled)

# vsm3 = cosine_similarity(datascaledarr,datascaledarr)
# vsm3array = np.array(vsm3)
# print(vsm3array.nbytes/1000000000)

######################################

data2 = data[:30000]
cs_matrix = np.vstack((vsm1array))
