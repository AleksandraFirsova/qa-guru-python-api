club_list_response_schema = {
    "type": "object",
    "properties": {
        "count": {
            "type": "integer",
            "minimum": 0
        },
        "next": {
            "type": ["string", "null"]
        },
        "previous": {
            "type": ["string", "null"]
        },
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "bookTitle": {"type": "string"},
                    "bookAuthors": {"type": "string"},
                    "publicationYear": {"type": "integer"},
                    "description": {"type": ["string", "null"]},
                    "telegramChatLink": {"type": ["string", "null"]},
                    "owner": {"type": "integer"},
                    "members": {
                        "type": "array",
                        "items": {"type": "integer"}
                    },
                    "reviews": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "integer"},
                                "club": {"type": "integer"},
                                "user": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "integer"},
                                        "username": {"type": "string"}
                                    },
                                    "required": ["id", "username"]
                                },
                                "review": {"type": ["string", "null"]},
                                "assessment": {
                                    "type": "integer",
                                    "minimum": 1,
                                    "maximum": 10
                                },
                                "readPages": {
                                    "type": "integer",
                                    "minimum": 0
                                },
                                "created": {"type": "string"},
                                "modified": {"type": ["string", "null"]}
                            },
                            "required": [
                                "id",
                                "club",
                                "user",
                                "review",
                                "assessment",
                                "readPages",
                                "created"
                            ]
                        }
                    },
                    "created": {"type": "string"},
                    "modified": {"type": ["string", "null"]}
                },
                "required": [
                    "id",
                    "bookTitle",
                    "bookAuthors",
                    "publicationYear",
                    "owner",
                    "members",
                    "reviews",
                    "created",
                    "modified"
                ]
            }
        }
    },
    "required": ["count", "next", "previous", "results"]
}