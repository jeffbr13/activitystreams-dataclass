from activitystreams.core import Object


class Actor(Object):
    """Describes a generic actor."""
    pass


class Application(Actor):
    """Describes a software application."""
    pass


class Group(Actor):
    """Represents a formal or informal collective of Actors."""
    pass


class Organization(Actor):
    """Represents an organization."""
    pass


class Person(Actor):
    """Represents an individual person."""
    pass


class Service(Actor):
    """Represents a service of any kind."""
    pass
