#%%
import mysql.connector
import pandas as pd
import sqlalchemy
import time

# %%
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="books"
)

mycursor = mydb.cursor()
#%%
mycursor.execute("SELECT bookID, title, authors, num_pages FROM books.books WHERE authors LIKE '%Edward P. Jones%'")
myresult = mycursor.fetchall()

#%% SELECT WRITER WHERE ORDER
start = time.clock()
mycursor.execute("SELECT * FROM books.books WHERE authors LIKE '%Garth Nix%' ORDER BY title")
myresult = mycursor.fetchall()
print(time.clock()-start)

# %% SELECT WHERE PAGES BIGGER THAN
mycursor = mydb.cursor()
start = time.clock()
mycursor.execute("SELECT * FROM books.books WHERE num_pages > 500 ORDER BY title")
myresult = mycursor.fetchall()
print(time.clock()-start)
mycursor.close()
#%% SELECT UNIQUE VALUES
mycursor = mydb.cursor()
start = time.clock()
mycursor.execute("SELECT DISTINCT authors FROM books.books")
myresult = mycursor.fetchall()
print(time.clock()-start)
len(myresult)

#%% INSERT ONE ROW
start = time.clock()
sql = "INSERT INTO books.books (bookID, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (564654615, 'Abhorsen (Abhorsen  #3)', 'Garth Nix', 4.27, '0007137354', 9780007137350, 'en-GB', 396, 1830, 156)
mycursor.execute(sql, val)
print(time.clock()-start)

#%% INSERT 100000 ROWS
val = [(564654615, 'Abhorsen (Abhorsen  #3)', 'Garth Nix', 4.27, '0007137354', 9780007137350, 'en-GB', 396, 1830, 156)]*100000
start = time.clock()
sql = "INSERT INTO books.books (bookID, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
mycursor.executemany(sql, val)
print(time.clock()-start)
# %% CHANGE NAMES STARTING WITH C
start = time.clock()
sql = "UPDATE books.books SET title = REGEXP_REPLACE (title, '^C', 'Changed book title')"
mycursor.execute(sql)
#mydb.commit()
print(time.clock()-start)
print(mycursor.rowcount, "record(s) affected")


# %% DELETE ROWS WHERE NUM PAGES BELOW
start = time.clock()
sql = "DELETE FROM books.books WHERE num_pages < 150"
mycursor.execute(sql)
mydb.commit()
print(time.clock()-start)
print(mycursor.rowcount, "record(s) deleted")
# %%

data = pd.read_csv('books.csv', error_bad_lines=False)

#%%
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

# %%
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE books")


# %%
database_username = 'root'
database_password = ''
database_ip       = 'localhost'
database_name     = 'books'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))

start = time.clock()
data.to_sql(con=database_connection, name='books', if_exists='append', index=False)
print(time.clock()-start)

#%%
data=None
#%% To duplicate the data
data = pd.concat([data,data])
#%%
data.to_csv('books.csv', index=False)

