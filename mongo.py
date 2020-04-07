#%%
import pymongo
import pandas as pd
import json
import time

#%%
data = pd.read_csv('books.csv', error_bad_lines=False)
# %%
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#%%
col = myclient["books"]['books']

# %%
start = time.clock()
dataD = data.to_dict(orient='records')
col.insert_many(dataD)
print(time.clock()-start)

# %%
data = None
dataD = None
# %%
myquery = { "authors": {"$regex": "Edward P. Jones"} }

mydoc = col.find(myquery, { "_id": 0}).sort("title")

for x in mydoc:
  print(x)

# %%
# %% SELECT WRITER WHERE ORDER
start = time.clock()
myquery = { "authors": {"$regex": "Garth Nix" }}
mydoc = col.find(myquery).sort("title")
x = list(mydoc)
print(time.clock()-start)
mydoc.count()

# %% SELECT WHERE PAGES BIGGER THAN
start = time.clock()
myquery = { "num_pages": {"$gt":500} }
mydoc = col.find(myquery).sort("title")
x = list(mydoc)
print(time.clock()-start)
mydoc.count()
# %% SELECT UNIQUE VALUES
start = time.clock()
myquery = 'authors'
mydoc = col.distinct(myquery)
x = list(mydoc)
print(time.clock()-start)
len(mydoc)

# %% INSERT 1 ROW
val = {"bookID":564654615, "title":'Abhorsen (Abhorsen  #3)', "authors":'Garth Nix', "average_rating":4.27, "isbn":'0007137354', "isbn13":9780007137350, "language_code":'en-GB', "num_pages":396, "ratings_count":1830, "text_reviews_count":156}
start = time.clock()
col.insert_one(val)
print(time.clock()-start)

#%% INSERT 100000 ROWS
start = time.clock()
col.insert_many([{"bookID":56465461, "title":'Abhorsen (Abhorsen  #3)', "authors":'Garth Nix', "average_rating":4.27, "isbn":'0007137354', "isbn13":9780007137350, "language_code":'en-GB', "num_pages":396, "ratings_count":1830, "text_reviews_count":156} for i in range(100000)])
print(time.clock()-start)


# %%
start = time.clock()
myquery = { "title": { "$regex": "^C" } }
newvalues = { "$set": { "title": "Changed book titleeeeeeee" } }
x = col.update_many(myquery, newvalues, upsert=True)
print(time.clock()-start)
print(x.modified_count, "documents updated.")

#%%
start = time.clock()
myquery = { "num_pages": 150 }
x = col.delete_many(myquery)
print(time.clock()-start)
print(x.deleted_count, " documents deleted.")


# %%
col.drop()

# %%
# %%
