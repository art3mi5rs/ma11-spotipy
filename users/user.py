class User:
    def __init__(self, username, status, logger):
        self.username = username
        self.status = status
        self.logger = logger

    def _update_log(self):
        self.logger.info(f"A new {self.status} user was created")


class Status:
    def __init__(self):
        self.free = "Free"
        self.premium = "Premium"
