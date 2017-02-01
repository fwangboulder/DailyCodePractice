##Add a post to the database

def AddPost(content):
    DB=psycopg2.connect("dbname")
    c=DB.cursor()
    c.execute("INSERT INTO posts")
