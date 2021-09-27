import dbcreds
import mariadb

conn = mariadb.connect(user=dbcreds.user,
                    password=dbcreds.password,
                    host=dbcreds.host,
                    port=dbcreds.port,
                    database=dbcreds.database
                    )
cursor = conn.cursor()

print('Username:')
username = input()
print('Post:')
content = input()

cursor.execute("INSERT INTO command_line_blog(username, content) VALUES(?,?)",[username, content])
conn.commit()

cursor.execute("SELECT content from command_line_blog")

print("**************List of posts**************")
posts = cursor.fetchall()
for list in posts:
    print(list)