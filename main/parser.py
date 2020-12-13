import os
import sys
import re

class Bucket(object):
    def __init__(self):
        self.selected_columns = None
        self.source_table = None
        self.query_type = None # select

class Search(object):
    def __init__(self, query):
        self.tree = None
        self.query = query

    def __call__(self):
        self.get_query()

    def parse(self):
        pass

    def get_query(self):
        return self.query

    def tokenize(self, strg, splt_str="\s+|\t+"):
        return re.split(splt_str, strg)


query = "select * from table_1"
obj = Search(query)
print(obj.get_query())
print(obj.tokenize(query))
