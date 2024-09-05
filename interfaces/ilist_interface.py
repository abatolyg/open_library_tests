from abc import ABC, abstractmethod

from ..objects.list import ListObject

""" IList Interface:
Use Python's abc (Abstract Base Class) module to create an interface-like structure.
The @abstractmethod decorator is used to define abstract methods that must be implemented by any class that inherits from IList.
We define three abstract methods: create_list, approve_list_created, and delete_list.
 """
class IList(ABC):
    @abstractmethod
    def create_list(self, list_object: ListObject) -> str:
        """
        Create a new list with the given name and items.
        
        :param name: The name of the list
        :param items: The items to be added to the list
        :return: True if the list was created successfully, False otherwise
        """
        pass

    @abstractmethod
    def get_list_object(self, list_object: ListObject) -> ListObject:
        """
        Approve a list that has been created.
        
        :param list_id: The ID of the list to approve
        :return: True if the list was approved successfully, False otherwise
        """
        pass

    @abstractmethod
    def delete_list(self, list_object: ListObject) -> bool:
        """
        Delete a list with the given ID.
        
        :param list_id: The ID of the list to delete
        :return: True if the list was deleted successfully, False otherwise
        """
        pass