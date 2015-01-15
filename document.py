class Document():
    """Represents a document on the filesystem"""
    
    def __init__(self, file_path, type=None, encoding="utf-8"):
        file = open(file_path, encoding=encoding)
        self.type = type
        self.content = file.read()
        file.close()
        
    def get_vocabulary(self):
        return self.content.lower().split()