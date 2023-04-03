
class Validator(object):
    @staticmethod
    def validate(config: dict) -> bool:
        if not config:
            return False

        for k, v in config.items():
            if not isinstance(v, dict):
                return False

            if "url" not in v:
                return False

        return True