class BaseException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class AssociateCreationError(BaseException):
    pass


class AgendaCreationError(BaseException):
    pass


class AgendaNotFoundError(BaseException):
    pass


class VoteRegistrationError(BaseException):
    pass


class AgendaSessionClosedError(BaseException):
    pass


class AssociateNotFoundError(BaseException):
    pass


class AssociateAlreadyVotedError(Exception):
    pass
