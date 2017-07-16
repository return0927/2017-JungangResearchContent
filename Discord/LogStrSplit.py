import codecs

class LogSplit():
    def __init__(self):
        pass

    def split(string):
        """if "Message Deleted" in string: authorSplitter = "Author : "; messageSplitter = " | Content : "
        elif "Message Editted" in string: authorSplitter = " / Author : "; messageSplitter = " | Before : "; afterMessageSplitter = " | After : "
        elif "]" in string and "Author" in string and "Message" in string: authorSplitter = "Author: "; messageSplitter = " | Message: "
        else:
            return "Splitted Line", string
        date = string.split(" ]   ")[0]
        author = string.split(authorSplitter)[1].split(messageSplitter)[0]
        message = string.split(messageSplitter)[1] if not "afterMessageSplitter" in locals() else string.split(afterMessageSplitter)[1]
        return date, author, message"""
        return None