#!/usr/bin/env python3
""" lists all documents """


def list_all(mongo_collection):
    """ list_all function """
    return list(mongo_collection.find())
