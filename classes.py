from collections import defaultdict

class Classes():
    def __init__(self):
        self.classes = defaultdict(list)
        self.total_doc_count = 0
        self.vocabulary = defaultdict(list)

    def add_doc(self, doc):
        self.total_doc_count += 1

        # add document to class or create new one if not yet existent
        if doc.type in self.classes:
            self.classes[doc.type].append(doc)
        else:
            self.classes[doc.type] = []
            self.classes[doc.type].append(doc)

        # append to vocabulary if not already added and store frequency
        for token in doc.get_tokens():
            if token not in self.vocabulary:
                self.vocabulary[token] = 1
            else:
                self.vocabulary[token] += 1

    def get_doc_count(self, class_name):
        return len(self.classes[class_name])

    def get_docs(self, class_name):
        return self.classes[class_name]

    def get_class_names(self):
        return self.classes.keys()

    def count_token_in_class(self, token_name, class_name):
        count = 0

        for doc in self.classes[class_name]:
            for token in doc.get_tokens():
                if token == token_name:
                    count += 1

        return count

    def count_token_total(self, token_name):
        if token_name in self.vocabulary:
            return self.vocabulary[token_name]
        else:
            return 0


    """ Get non-duplicate list of all words in all classes """
    def get_vocabulary(self):
        return self.vocabulary.keys()
