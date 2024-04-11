import unittest
import json
import os
from verify_input_json import verify_input_json


class TestVerifyInputJSON(unittest.TestCase):
    """
    Class created for unit tests.
    """
    def test_valid_input(self):
        """
        Test for valid input.
        """
        json_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": ["iam:ListRoles", "iam:ListUsers"],
                        "Resource": "example",
                    }
                ],
            },
        }
        with open("file.json", "w") as file:
            json.dump(json_data, file)
        self.assertTrue(verify_input_json("file.json"))

    def test_single_asteriks(self):
        """
        Test for single asterisk for resource.
        """
        json_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": ["iam:ListRoles", "iam:ListUsers"],
                        "Resource": "*",
                    }
                ],
            },
        }
        with open("file.json", "w") as file:
            json.dump(json_data, file)
        self.assertFalse(verify_input_json("file.json"))

    def test_file_not_found(self):
        """
        Test for no file. 
        """
        self.assertIsNone(verify_input_json("test_file_not_found.json"))
    
    def invalid_file(self, json_data: dict):
        """
        Function creates invalid file for tests.
        """
        with open("file.json", "w") as file:
            json.dump(json_data,file)
        self.assertIsNone(verify_input_json("file.json"))
        

    def test_invalid_json_format(self):
        """
        Test for invalid json format.
        """
        json_data = '{"test": "arn:aws:s3:::example-bucket/*"'
        with open("file.json", "w") as file:
            file.write(json_data)
        self.assertIsNone(verify_input_json("file.json"))    
        
    
    def test_invalid_data_format_no_policy_document(self):
        """
        Test for no policy document.
        """
        json_data = {"PolicyName": "root"}
        self.invalid_file(json_data)

    def test_invalid_data_format_policy_document_wrong_type(self):
        """
        Test for no wrong policy document data type.
        """
        json_data = {"PolicyName": "root", "PolicyDocument": 1}
        self.invalid_file(json_data)

    def test_invalid_data_format_no_policy_name(self):
        """
        Test for no policy name.
        """
        json_data = {
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": ["iam:ListRoles", "iam:ListUsers"],
                        "Resource": "example",
                    }
                ],
            }
        }
        self.invalid_file(json_data)
    def test_invalid_data_format_policy_name_wrong_type(self):
        """
        Test for wrong policy name data type.
        """
        json_data = {
            "PolicyName": 1,
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": ["iam:ListRoles", "iam:ListUsers"],
                        "Resource": "*",
                    }
                ],
            },
        }
        self.invalid_file(json_data)

    def test_invalid_data_format_policy_name_not_enough_characters(self):
        """
        Test for not enough characters in policy name.
        """
        json_data = {
            "PolicyName": "",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": ["iam:ListRoles", "iam:ListUsers"],
                        "Resource": "*",
                    }
                ],
            },
        }
        self.invalid_file(json_data)
    
    def test_invalid_data_format_policy_name_too_many_characters(self):
        """
        Test for to many characters in policy name.
        """
        json_data = {
            "PolicyName": "t"*200,
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": ["iam:ListRoles", "iam:ListUsers"],
                        "Resource": "*",
                    }
                ],
            },
        }
        self.invalid_file(json_data)
    def test_invalid_data_format_policy_name_wrong_re(self):
        """
        Test for wrong re in policy name.
        """
        json_data = {
            "PolicyName": "*",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": ["iam:ListRoles", "iam:ListUsers"],
                        "Resource": "*",
                    }
                ],
            },
        }
        self.invalid_file(json_data)




if __name__ == "__main__":
    unittest.main()
   





