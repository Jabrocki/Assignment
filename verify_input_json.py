from re import search
import json


class InvalidDataFormat(Exception):
    """
    Class for invalid data error in verify_input_json method.
    """

    pass


def verify_input_json(json_path: str) -> bool:
    """
    It returns bool if file and data format (AWS::IAM::Role Policy) is correct. Else it returns None and prints out error type.

    Parameters
    -----
    json_path: str
        path to json file
    """
    try:
        with open(json_path, "r") as file:
            data = json.load(file)

        if "PolicyName" in data and "PolicyDocument" in data:
            policy_name = data["PolicyName"]
            policy_document = data["PolicyDocument"]
            if type(policy_name) is str:
                if not search(r"[\w+=,.@-]+", policy_name):
                    raise InvalidDataFormat
                if len(policy_name) < 1 or len(policy_name) > 128:
                    raise InvalidDataFormat
            else:
                raise InvalidDataFormat
            if type(policy_document) is not dict:
                raise InvalidDataFormat
        else:
            raise InvalidDataFormat

        if "Statement" in policy_document:
            statement = policy_document["Statement"]
            if type(statement) is list:
                for i in statement:
                    if "Resource" in i and i["Resource"] == "*":
                        return False
        return True
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except InvalidDataFormat:
        print("Invalid data format.")
