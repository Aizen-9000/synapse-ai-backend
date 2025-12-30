class UIValidator:
    @staticmethod
    def validate(data: dict, schema):
        for field in schema.required:
            if field not in data:
                raise ValueError(f"Missing UI field: {field}")