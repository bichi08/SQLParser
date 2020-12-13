import os
import sys
import re


class Bucket(object):
    def __init__(self):
        self.selected_columns = None
        self.source_table = None
        self.query_type = None  # select or create or merge or update


class Search(object):
    def __init__(self, query):
        self.tree = None
        self.query = query.lower()
        self.source_system = None
        self.target_system = "bigquery"

    def __call__(self):
        tokens = self.tokenize(self.query)
        self.parse(tokens)

        print(self.tree.selected_columns)
        print(self.tree.source_table)
        print(self.tree.query_type)

    def parse(self, tokens):
        bucket = Bucket()
        last = None
        for idx, token in enumerate(tokens):
            if idx == 0:
                bucket.query_type = token

            if last == "select" and tokens[idx + 1] == "from":
                bucket.selected_columns = token

            if last == "from":
                bucket.source_table = token

            last = token
        self.tree = bucket

    def get_query(self):
        return self.query

    def tokenize(self, strg, splt_str="\s+|\t+"):
        return re.split(splt_str, strg)


query = "select * from table_1"
obj = Search(query)
obj()
