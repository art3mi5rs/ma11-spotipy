from users.user import User, Status


class Artist(User):
    def __init__(self, name, logger):
        super().__init__(name, Status.premium, logger)
        self.name = name
        self.status = Status.premium

