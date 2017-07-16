import query, websocket, codecs


class db:
    def getDB(user, pw='Kkutu0410!'):
        return query.conn(user, pw)

    def getUserinfo(cursor, id):
        cursor.execute("SELECT * FROM users where _id='" + str(id) + "'")
        return cursor.fetchall()

    def getWord(cursor, word):
        cursor.execute("SELECT * FROM kkutu_ko where _id='" + str(word) + "'")
        return cursor.fetchall()


first = ""


class web:
    def openSocket(socket):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(socket, on_message=web.procedure, on_close=web.breaker)
        ws.run_forever()

    def procedure(ws, message):
        global first
        if first == "":
            first = message
        print("Incoming Message")
        # print(message)
        with codecs.open("First.txt", "a", encoding="UTF-8") as f:
            f.write(message + "\n")

    def breaker(ws):
        print(" ## Socket Died")

class discord:
    class commandProcedure:
        def personalCommands(self, commandline):
            print(self)
            print(commandline)