"""Module creating abstract object (base Framework)"""
import json
from abc import ABC


class Model(ABC):
    """Base abstract class"""

    @classmethod
    def get_data(cls):
        """Function returned objects in database"""
        file = open('database/' + cls.file, 'r', encoding="utf-8")
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    def generate_dict(self):
        """Function create empty dictionary"""
        return self.__dict__

    @classmethod
    def get_all(cls):
        """Function returning all objects in database"""
        data = cls.get_data()
        if len(data) > 0:
            fields = data[0].keys()
            for el in data:
                for field in fields:
                    if field == "id":
                        continue
                    print(el[field])

    @classmethod
    def print_object(cls, objects: list):
        """Function printiong objects"""
        if len(objects) > 0:
            fields = objects[0].keys()
            for el in objects:
                for field in fields:
                    if field == "id":
                        continue
                    print(el[field])

    @classmethod
    def get_by_id(cls, id: int):
        """Function returning object by id"""
        data = cls.get_data()
        counter = 0
        if len(data) > 0:
            for el in data:
                if el["id"] == id:
                    return el
                counter += 1
                if counter == len(el):
                    print("Not found element with this id")

    @staticmethod
    def save_to_file(path_to_file, data):
        """Function saving object to the file"""
        file = open(path_to_file, 'w', encoding="utf-8")
        data_in_json = json.dumps(data)
        file.write(data_in_json)

    @classmethod
    def delete(cls, id: int):
        """Function deleting object by id"""
        elements = cls.get_data()
        for el, element in enumerate(elements):
            if element["id"] == id:
                del elements[el]
                break
        cls.save_to_file('database/' + cls.file, elements)

    def save(self):
        """Function saving object"""
        data = self.get_data()
        new_el = self.generate_dict()
        if len(data) > 0:
            new_el["id"] = data[-1]["id"] + 1
        else:
            new_el["id"] = 1
        data.append(new_el)
        self.save_to_file('database/' + self.file, data)
