""" 
ListJsonData is just wrapper for json.
additional_params allows to add more parameters in the future to json 
"""
class ListJsonData:
    def __init__(self, name=None, description=None, tags=None, seeds=None, additional_params=None):
        self.name = name
        self.description = description
        self.tags = tags or []
        self.seeds = seeds or []
        self.additional_params = additional_params if additional_params else {}

    def set(self, key, value):
        if key in {"name", "description", "tags", "seeds"}:
            setattr(self, key, value)
        else:
            self.additional_params[key] = value

    def to_json(self):
        data = {
            "name": self.name,
            "description": self.description,
            "tags": self.tags,
            "seeds": self.seeds,
        }
        data.update(self.additional_params)
        return data