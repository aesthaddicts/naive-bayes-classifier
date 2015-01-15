import glob
from collections import defaultdict

from document import Document

# first, set up training data
training_files = glob.glob('./documents/*/train/*.txt')
training_docs = []

for file_path in training_files:
    # the class is encoded into the file_path (first * in patttern above)
    document_class = file_path.split("/")[2]
    training_docs.append(Document(file_path, document_class))

# cache this for later use
docs_in_class = defaultdict(list)
for doc in training_docs:
    docs_in_class[doc.type].append(doc)
