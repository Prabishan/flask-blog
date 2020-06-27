import sqlite3

with sqlite3.connect("blog.db") as connection:
    
    #get a cursor object used to execute SQL commands
    c = connection.cursor()

    #creates the table with two fields- tile and post
    c.execute("""CREATE TABLE posts(title TEXT, post TEXT)""")

    c.execute('INSERT INTO posts VALUES("Blog Title Test","Blog Post Test")')
