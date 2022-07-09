from enum import Enum


class UserTypes(Enum):
    Owner = 'Owner'
    District_Manager = 'District Manager'
    Manager = 'Manager'
    Assistant_Manager = 'Assistant_Manager'
    Employee = 'Employee'

    @classmethod
    def all(cls):
        return [UserTypes.Owner, UserTypes.District_Manager, UserTypes.Manager,
        UserTypes.Assistant_Manager, UserTypes.Employee]