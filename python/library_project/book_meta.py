from abc import ABCMeta


class BookMeta(ABCMeta):

    def __new__(mcs, name, bases, namespace):

        if "get_details" not in namespace:
            print(f"Warning: Class {name} does not contain get_details() method.")

        return super().__new__(mcs, name, bases, namespace)
