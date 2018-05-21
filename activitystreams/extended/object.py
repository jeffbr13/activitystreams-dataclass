from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from activitystreams.core import Object, ActivityStreamsEntity


@dataclass
class Relationship(Object):
    """Describes a relationship between two individuals.

    The subject and object properties are used to identify the connected individuals.
    See 5.2 Representing Relationships Between Entities for additional information.
    """
    subject: ActivityStreamsEntity = None
    object: ActivityStreamsEntity = None
    relationship: str = None


@dataclass
class Place(Object):
    """Represents a logical or physical location.

    If units is not specified, the default is assumed to be "m" indicating meters.
    """
    accuracy: Optional[float] = None
    altitude: Optional[float] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    radius: Optional[float] = None
    units: Optional[str] = None


class Article(Object):
    """Represents any kind of multi-paragraph written work."""
    pass


class Note(Object):
    """Represents a short written work typically less than a single paragraph in length.
    """
    pass


class Document(Object):
    """Represents a document of any kind."""
    pass


class Audio(Document):
    """Represents an audio document of any kind."""
    pass


class Image(Document):
    """An image document of any kind."""
    pass


class Video(Document):
    """A video document of any kind."""
    pass


class Page(Document):
    """Represents a Web Page."""
    pass


class Event(Object):
    """Represents any kind of event."""
    pass


@dataclass
class Profile(Object):
    """A Profile is a content object that describes another Object.

    Typically used to describe Actor Type objects.
    The describes property is used to reference the object being described by the profile.
    """
    describes: Object = None


class Tombstone(Object):
    """A Tombstone represents a content object that has been deleted.

    It can be used in Collections to signify that there used to be an object at this position,
    but it has been deleted.
    """
    formerType: Optional[str] = None
    deleted: Optional[datetime] = None
