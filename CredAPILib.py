##################################
# Project: CredAPI
# File:    CredAPILib.py
# Author:  Yash Bharatula
# Date:    08/03/2019
##################################

class credential:
    def __init__(self, name, username=None, password=None, client_id=None, client_secret=None, user_agent=None):
        self.name = name.strip().lower()

        if self.name == "reddit":
            self.username = username
            if username is None:
                raise ValueError("Class credential: username is required")
            self.password = password
            if password is None:
                raise ValueError("Class credential: password is required")
            self.client_id = client_id
            if client_id is None:
                raise ValueError("Class credential: client_id is required")
            self.client_secret = client_secret
            if client_secret is None:
                raise ValueError("Class credential: client_secret is required")
            self.user_agent = user_agent
            if user_agent is None:
                raise ValueError("Class credential: user_agent is required")
        else:
            raise NameError("Class credential: " + self.name + " is not defined yet")

    def get_cred_dict(self):
        cred_dict = {}
        if self.name == "reddit":
            cred_dict["username"] = self.username
            cred_dict["password"] = self.password
            cred_dict["client_id"] = self.client_id
            cred_dict["client_secret"] = self.client_secret
            cred_dict["user_agent"] = self.user_agent

        return cred_dict
