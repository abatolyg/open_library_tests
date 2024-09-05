""" 
LoginJsonData is just wrapper for json.
additional_params allows to add more parameters in the future to json 
"""
class LoginJsonData:
    def __init__(self, email=None, password=None,additional_params=None):
        self.email = email
        self.password = password

    def set(self, key, value):
        if key in {"name", "description", "tags", "seeds"}:
            setattr(self, key, value)
        else:
            self.additional_params[key] = value

    def to_json(self):
        data = {
            "email": self.email,
            "password": self.password
        }
        data.update(self.additional_params)
        return data