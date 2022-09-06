import json
from jsonschema import validate


class Validate:
    def create_new_json(self, response):
        new_response = json.dumps(response)
        return json.loads(new_response)

    def empty_friend_list_current_user(self, response):
        schema = {
            "type": "object",
            "properties": {
                "kind": {"type": "string", "enum": ["UserList"]},
                "data": {
                    "type": "object",
                    "properties": {
                        "children": {"type": "array"}
                    }
                }
            }
        }
        _json = self.create_new_json(response)
        validate(instance=_json, schema=schema)

    def karma_current_user(self, response):
        schema = {
            "type": "object",
            "properties": {
                "kind": {"type": "string", "enum": ["KarmaList"]},
                "data": {"type": "array"}
            }
        }
        _json = self.create_new_json(response)
        validate(instance=_json, schema=schema)
