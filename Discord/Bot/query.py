import psycopg2
from time import time

host = "localhost"
database = "main"
user = "postgres"


def passw():
    return input("Pass: ")


def conn(user, pw):
    return psycopg2.connect(host=host, database=database, user=user, password=pw).cursor()


def getuser(cursor):
    cur = cursor
    cur.execute("SELECT * FROM users;")

    # data = cur.fetchall()
    return cur.fetchall()


def getsession(cursor):
    cur = cursor
    cur.execute("SELECT * FROM session;")

    # data = cur.fetchall()
    return cur.fetchall()


def ex_query(cursor, query):
    cur = cursor
    cur.execute(query)

    # data = cur.fetchall()
    return cur.fetchall()


"""start = time()
while True:
    if time() - start > 600:
        start = time()
        cur = conn("Kkutu0410!")
        cur.execute("SELECT * FROM session;")
        data = cur.fetchall()

        out = ""
        for l in data:
            out += str(l)

        with open(start, "w", encoding="UTF-8") as f:
            f.write(out)
    else:
        pass
"""

"""
bj= []
for l in data:
    #if l[0] == "108010890119595160271":
    #    for n in range(len(l)):
    #        print(str(n)+"  :  "+str(l[n]))
    if "BDG" in str(l[5]):
        #print(l)
        bj.append(l)

"""
