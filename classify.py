import glob
from collections import defaultdict

from document import Document
from classes import Classes

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

# [print(doc.type, doc.get_tokens()) for doc in training_docs]

classes = Classes()
for doc in training_docs:
    classes.add_doc(doc)
    # print(doc.get_tokens())

print(classes.total_doc_count)
print(classes.get_doc_count("wirtschaft"))
[print(name) for name in classes.get_class_names()]

for doc_class in classes.get_class_names():
    prior = classes.get_doc_count(doc_class) / classes.total_doc_count
    text = classes.get_all_text(doc_class)
    print(prior)

    for word in classes.get_vocabulary():
        print(doc_class, word, classes.count_token_in_class(word, doc_class))

# print(classes.get_vocabulary())
