import re
import string

# for removing punctuation
regex = re.compile("[%s]" % re.escape(string.punctuation))

class Document():
    """Represents a document on the filesystem"""

    def __init__(self, file_path, type=None, encoding="utf-8"):
        file = open(file_path, encoding=encoding)
        self.type = type
        self.content = file.read()
        file.close()

    def get_tokens(self):
        return re.sub(regex, "", self.content.lower()).split()

    # def get_text(self):
    #     return self.content.lower()
