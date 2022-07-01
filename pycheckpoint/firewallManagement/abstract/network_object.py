from restfly.endpoint import APIEndpoint
from abc import ABC, abstractclassmethod


class NetworkObjectAPI(ABC, APIEndpoint):
    @abstractclassmethod
    def add(self):
        pass

    @abstractclassmethod
    def show(self):
        pass

    @abstractclassmethod
    def set(self):
        pass

    @abstractclassmethod
    def delete(self):
        pass

    @abstractclassmethod
    def show_objects(self):
        pass
