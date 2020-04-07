#%%
import mysql.connector
import pandas as pd
import sqlalchemy
import time


#datat = pd.read_csv('books.csv', error_bad_lines=False)

# %%
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="booksnormal"
)

mycursor = mydb.cursor()

#%%
mycursor.execute("SELECT books.bookID, title, name, num_pages FROM author_book_rel INNER JOIN books ON author_book_rel.bookID = books.bookID INNER JOIN authors ON author_book_rel.AuthorID = authors.AuthorID")
myresult = mycursor.fetchall()

#for x in myresult:
#  print(x)

len(myresult)
#%% SELECT WRITER WHERE ORDER
mycursor = mydb.cursor()
start = time.clock()
mycursor.execute("SELECT * FROM author_book_rel INNER JOIN books ON author_book_rel.bookID = books.bookID INNER JOIN authors ON author_book_rel.AuthorID = authors.AuthorID WHERE name='Garth Nix' ORDER BY title")
myresult = mycursor.fetchall()
print(time.clock()-start)
len(myresult)
mycursor.close()

# %% SELECT WHERE PAGES BIGGER THAN
mycursor = mydb.cursor(buffered=True)
start = time.clock()
mycursor.execute("SELECT * FROM author_book_rel INNER JOIN books ON author_book_rel.bookID = books.bookID INNER JOIN authors ON author_book_rel.AuthorID = authors.AuthorID WHERE num_pages > 500 ORDER BY title")
mycursor.fetchall()
print(time.clock()-start)
mycursor.close()

#%% SELECT UNIQUE VALUES
mycursor = mydb.cursor()
start = time.clock()
mycursor.execute("SELECT DISTINCT name FROM authors")
myresult = mycursor.fetchall()
print(time.clock()-start)
len(myresult)
#%% INSERT ONE ROW
start = time.clock()
sql = "INSERT INTO books (bookID, title, average_rating, isbn, isbn13, num_pages, ratings_count, text_reviews_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
val = (564654615, 'Abhorsen (Abhorsen  #3)', 4.27, '0007137354', 9780007137350, 396, 1830, 156)
mycursor.execute(sql, val)
print(time.clock()-start)

#%% INSERT 100000 ROWS
val = [(564654615, 'Abhorsen (Abhorsen  #3)', 4.27, '0007137354', 9780007137350, 396, 1830, 156)]*100000
start = time.clock()
sql = "INSERT INTO books (bookID, title, average_rating, isbn, isbn13, num_pages, ratings_count, text_reviews_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
mycursor.executemany(sql, val)
print(time.clock()-start)
# %% CHANGE NAMES STARTING WITH C
start = time.clock()
sql = "UPDATE books SET title = REGEXP_REPLACE (title, '^C', 'Changed book title')"
mycursor.execute(sql)
mydb.commit()
print(time.clock()-start)
print(mycursor.rowcount, "record(s) affected")

# %% DELETE ROWS WHERE NUM PAGES BELOW
start = time.clock()
sql = "DELETE FROM books WHERE num_pages < 150"
mycursor.execute(sql)
mydb.commit()
print(time.clock()-start)
print(mycursor.rowcount, "record(s) deleted")

#%%
data = pd.read_csv('books.csv', error_bad_lines=False)
#%%
datalanbook = data[['bookID', 'language_code']]

#%%
datalan = datalanbook[['language_code']].drop_duplicates().reset_index(drop=True)
datalan['LanID'] = datalan.index
datalan = datalan.reindex(columns=['LanID', 'language_code'])
datalanbook['language_code'] = datalanbook['language_code'].map(datalan.set_index('language_code')['LanID'])
datalanbook = datalanbook.rename(columns={'language_code': "LanID"})



# %%
dataauthorbook = data[['bookID', 'authors']]
dataauthorbook = dataauthorbook.join(dataauthorbook['authors'].str.split('-', expand=True).add_prefix('author'))
dataauthorbook = dataauthorbook.drop(['authors'], axis=1)
dataauthorbook.set_index('bookID', inplace=True)
dataauthorbook = pd.concat([dataauthorbook[col] for col in dataauthorbook])

# %%
dataauthorbook = dataauthorbook.dropna()
dataauthorbook = dataauthorbook.to_frame()
dataauthorbook = dataauthorbook.rename(columns={0: "authors"})

#%%
#dataauthorbook = dataauthorbook.to_frame()
dataauthorbook['bookID'] = dataauthorbook.index
dataauthorbook = dataauthorbook.reindex(columns=['bookID', 'authors'])
#%%
dataAuthor = dataauthorbook[['authors']].drop_duplicates().reset_index(drop=True)
dataAuthor['AuthorID'] = dataAuthor.index
dataAuthor = dataAuthor.reindex(columns=['AuthorID', 'authors'])
dataAuthor = dataAuthor.rename(columns={'authors': "name"})
#%%
dataauthorbook['authors'] = dataauthorbook['authors'].map(dataAuthor.set_index('name')['AuthorID'])
dataauthorbook = dataauthorbook.rename(columns={'authors': "AuthorID"})
# %%
data = data.drop(['language_code', 'authors'], axis=1)

# %%
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

# %%
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE booksnormal")

# %%
database_username = 'root'
database_password = ''
database_ip       = 'localhost'
database_name     = 'booksnormal'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))
# %% 
start = time.clock()
data.to_sql(con=database_connection, name='books', if_exists='replace', index=False)
dataAuthor.to_sql(con=database_connection, name='authors', if_exists='replace', index=False)
datalan.to_sql(con=database_connection, name='languages', if_exists='replace', index=False)
dataauthorbook.to_sql(con=database_connection, name='author_book_rel', if_exists='replace', index=False)
datalanbook.to_sql(con=database_connection, name='language_book_rel', if_exists='replace', index=False)
print(time.clock()-start)

# %%
start = time.clock()
data.to_sql(con=database_connection, name='books', if_exists='append', index=False)
print(time.clock()-start)

# %%
