# objects/list_object.py
# ListObject encapsulate key usually retrieved from the API or WEB and json_list_object
class ListObject:
    def __init__(self, key,json_list_object):
        self.key = key
        self.json_list_object = json_list_object

    def __str__(self):
        return f"List(key={self.key}, json_list_object={self.json_list_object} )"  
