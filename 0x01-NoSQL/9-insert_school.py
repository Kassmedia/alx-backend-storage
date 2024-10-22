#!/usr/bin/env python3
""" MongbDB Operations with Python using pmongo ""


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs """
    return mongo_collection.insert(kwargs)
