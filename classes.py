from collections import defaultdict

class Classes():
    def __init__(self):
        self.classes = defaultdict(list)
        self.total_doc_count = 0

    def add_doc(self, doc):
        self.total_doc_count += 1

        if doc.type in self.classes:
            self.classes[doc.type].append(doc)
        else:
            self.classes[doc.type] = []
            self.classes[doc.type].append(doc)

    def get_doc_count(self, class_name):
        return len(self.classes[class_name])

    def get_docs(self, class_name):
        return self.classes[class_name]

    def get_class_names(self):
        return self.classes.keys()

    def get_all_text(self, class_name):
        all_text = ""

        # TODO: use token instead of text?
        for doc in self.classes[class_name]:
            all_text += doc.get_text()

        return all_text

    def count_token_in_class(self, token_name, class_name):
        count = 0

        for doc in self.classes[class_name]:
            for token in doc.get_tokens():
                if token == token_name:
                    count += 1

        return count

    def count_token_total(self, token_name):
        total_count = 0
        for doc_class in self.classes:
            total_count += self.count_token_in_class(token_name, doc_class)

        return total_count


    """ Get unique list of all words in all classes """
    def get_vocabulary(self):
        vocabulary = []

        # go through all tokens from every document
        for doc_class in self.classes:
            for doc in self.classes[doc_class]:
                for token in doc.get_tokens():
                    # append to vocabulary if not already added
                    if token not in vocabulary:
                        vocabulary.append(token)

        return vocabulary
