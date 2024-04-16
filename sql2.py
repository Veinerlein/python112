import sqlite3

def dict_factory(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

db = sqlite3.connect("simple_prepared_db.sqlite")
# db.row_factory = dict_factory
cur = db.cursor()
#
#
# cur.execute("SELECT * FROM users")
# res = cur.fetchall()
# print(res)
# for user in res:
#     print(user["name"],user['email'])

# cur.execute("INSERT INTO users (name, email) VALUES ('User 4', 'user4@gmail.com')")
# cur.execute("INSERT INTO users (name, email) VALUES ('User 5', 'user5@gmail.com')")
db.commit()
print(db.total_changes)


db.close()



