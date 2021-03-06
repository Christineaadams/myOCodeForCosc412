import json
import requests
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity # For calculating similarity matrix
from sklearn.neighbors import NearestNeighbors


os.chdir('C:\Python27')
DIR_PATH = os.getcwd() #Get currect directory
​
lfm = pd.read_csv(DIR_PATH + "//LastFM_Matrix.csv") #Load dataset
lfm.head()

songs = pd.DataFrame(lfm.columns)
songs.head(30)

lfm_songs = lfm.drop("user",axis =1) #drop user column
lfm_songs.head() # Show Head

lfm_songs.shape #gives out total rows and columns|

data_similarity = cosine_similarity(lfm_songs.T) #
data_similarity

type(data_similarity)

data_similarity_df = pd.DataFrame(data_similarity, columns=(lfm_songs.columns), index=(lfm_songs.columns))

data_similarity_df.head()# similarity Matrix

data_similarity_df.index.is_unique # check if there is no repeated songs

neigh = NearestNeighbors(n_neighbors=10)

neigh.fit(data_similarity_df) # Fit the data

#Copy the predicted data to a new DataFrame
model = pd.DataFrame(neigh.kneighbors(data_similarity_df, return_distance=False))
model.head() #gives you integer values instead of song names

final_model = pd.DataFrame(data_similarity_df.columns[model], index=data_similarity_df.index)#gives names with respect to songs

final_model.head() #preview final Model

top10 = final_model[list(final_model.columns[:11])]

top10.head()

top10.to_csv("top10.csv",index_label = "Index") # store data in csv file

f=open("search.txt","r")
value=f.read()
print(value)

##look up like how to run a script in a command line where we can directly run jupyter notebook and get a result
##value="abba"
for j in range(0, 8):
  if final_model[0][j]== value:
    print (j)
    break
row_1=final_model.iloc[j]
print(row_1)

##return to file
a=final_model.iloc[j]
a.tolist()
ithinkjson=a.to_json()
print(ithinkjson)
with open('dataithink.json', 'w') as json_file: ##a+ is used to append if I wanted to overwrite we use w maybe .txt
    json.dump(ithinkjson, json_file)

with open('collectionofallsearches.json', 'a+') as json_file: ##a+ is used to append if I wanted to overwrite we use w maybe .txt
    json.dump(ithinkjson, json_file)