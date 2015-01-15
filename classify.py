import glob
from document import Document

# first, set up training data
training_files = glob.glob('./documents/*/train/*.txt')
documents = [Document(file) for file in training_files]

print(documents[0].get_vocabulary())