import glob
import math

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


classes = Classes()
for doc in training_docs:
    classes.add_doc(doc)

[print(name) for name in classes.get_class_names()]
print(classes.total_doc_count)
print(classes.get_doc_count("wirtschaft"))


# start pseudo code training
# for doc_class in classes.get_class_names():
#     prior = classes.get_doc_count(doc_class) / classes.total_doc_count
#     print(prior)
#
#     for term in classes.get_vocabulary():
#         tct_frequency = classes.count_token_in_class(term, doc_class)
#         cond_prob = tct_frequency + 1 / (classes.count_token_total(term) * (tct_frequency + 1))
#
#         print(doc_class, term, cond_prob)


# now, look at the test files
test_files = glob.glob('./documents/*/test/*.txt')
test_docs = []

for file_path in test_files:
    # the class is encoded into the file_path (first * in patttern above)
    document_class = file_path.split("/")[2]
    test_docs.append(Document(file_path, document_class))

# start pseudo code testing
for doc in test_docs:
    tokens = doc.get_tokens()
    score = defaultdict(list)

    for doc_class in classes.get_class_names():
        score[doc_class] = math.log(classes.get_doc_count(doc_class) / classes.total_doc_count)
        for token in tokens:
            tct_frequency = classes.count_token_in_class(token, doc_class)
            cond_prob = tct_frequency + 1 / ((classes.count_token_total(token) + 1) * (tct_frequency + 1))

            score[doc_class] += cond_prob
    print(doc.type, score)
