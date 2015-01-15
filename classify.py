import glob
from document import Document

# first, set up training data
training_files = glob.glob('./documents/*/train/*.txt')
training_docs = []

for file_path in training_files:
    # the class is encoded into the file_path (first * in patttern above)
    file_class = file_path.split("/")[2]
    training_docs.append(Document(file_path, file_class))