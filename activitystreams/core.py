import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Union, Optional, Mapping, Collection as CollectionType


LD_NAMESPACE = 'https://www.w3.org/ns/activitystreams'

LangString = Mapping[str, str]  # todo - limit keys to IETF language tags
String = Union[str, LangString]

ActivityStreamsImageEntity = Union['ActivityStreamsImage', 'ActivityStreamsLink']

ActivityStreamsCollectionEntity = Union['ActivityStreamsCollection', 'ActivityStreamsLink']
ActivityStreamsCollectionPageEntity = Union['ActivityStreamsCollectionPage', 'ActivityStreamsLink']
ActivityStreamsOrderedCollectionEntity = Union['ActivityStreamsOrderedCollection', 'ActivityStreamsLink']
ActivityStreamsOrderedCollectionPageEntity = Union['ActivityStreamsOrderedCollectionPage', 'ActivityStreamsLink']


class ActivityStreamsEntity:
    def __repr__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        raise NotImplementedError


@dataclass
class Object(ActivityStreamsEntity):
    name: String = None
    content: String = None
    summary: Optional[String] = None
    published: Optional[datetime] = None
    attachment: Optional[ActivityStreamsEntity] = None
    updated: Optional[datetime] = None
    attributedTo: Optional[ActivityStreamsEntity] = None
    audience: CollectionType[ActivityStreamsEntity] = None
    context: Optional[ActivityStreamsEntity] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    duration: Optional[timedelta] = None
    generator: Optional[ActivityStreamsEntity] = None
    mediaType: Optional[str] = None
    icon: Optional[ActivityStreamsImageEntity] = None
    image: Optional[ActivityStreamsImageEntity] = None
    url: Optional['Link'] = None
    inReplyTo: CollectionType[ActivityStreamsEntity] = None
    replies: Optional['Collection'] = None
    location: CollectionType[ActivityStreamsEntity] = None
    preview: CollectionType[ActivityStreamsEntity] = None
    tag: CollectionType[ActivityStreamsEntity] = None
    to: CollectionType[ActivityStreamsEntity] = None
    bto: CollectionType[ActivityStreamsEntity] = None
    cc: CollectionType[ActivityStreamsEntity] = None
    bcc: CollectionType[ActivityStreamsEntity] = None

    @property
    def type(self):
        return f'{LD_NAMESPACE}#{self.__class__.__name__}'

    def to_dict(self):
        return {
            '@context': LD_NAMESPACE,
            'type': self.type,
            # data
            'nameMap': self.nameMap,
            'contentMap': self.contentMap,
            'attachment': self.attachment,
            'attributedTo': self.attributedTo,
            'audience': self.audience,
            'context': self.context,
            'endTime': self.endTime,
            'generator': self.generator,
            'icon': self.icon,
            'image': self.image,
            'inReplyTo': self.inReplyTo,
            'location': self.location,
            'preview': self.preview,
            'published': self.published,
            'replies': self.replies,
            'startTime': self.startTime,
            'summaryMap': self.summaryMap,
            'tag': self.tag,
            'updated': self.updated,
            'url': self.url,
            'to': self.to,
            'bto': self.bto,
            'cc': self.cc,
            'bcc': self.bcc,
            'mediaType': self.mediaType,
            'duration': self.duration,
        }


@dataclass
class Link(ActivityStreamsEntity):
    href: str
    rel: Optional[str] = None
    mediaType: Optional[str] = None
    name: Optional[String] = None
    hreflang: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None
    preview: Optional[ActivityStreamsEntity] = None

    @property
    def type(self):
        return f'{LD_NAMESPACE}#{self.__class__.__name__}'

    def to_dict(self):
        return {
            '@context': LD_NAMESPACE,
            'type': self.type,
            'href': self.href,
            'rel': self.rel,
            'mediaType': self.mediaType,
            'name': self.name,
            'hreflang': self.hreflang,
            'height': self.height,
            'width': self.width,
            'preview': self.preview,
        }


@dataclass
class Activity(Object):
    actor: ActivityStreamsEntity = None
    object: Object = None
    target: CollectionType[ActivityStreamsEntity] = None
    result: Optional[ActivityStreamsEntity] = None
    origin: Optional[ActivityStreamsEntity] = None
    instrument: Optional[ActivityStreamsEntity] = None

    def to_dict(self):
        d = super().to_dict()
        d.update({
            'actor': self.actor,
            'object': self.object,
            'target': self.target,
            'result': self.result,
            'origin': self.origin,
            'instrument': self.instrument,
        })
        return d


@dataclass
class IntransitiveActivity(Object):
    actor: ActivityStreamsEntity = None
    target: CollectionType[ActivityStreamsEntity] = None
    result: Optional[ActivityStreamsEntity] = None
    origin: Optional[ActivityStreamsEntity] = None
    instrument: Optional[ActivityStreamsEntity] = None

    def to_dict(self):
        d = super().to_dict()
        d.update({
            'actor': self.actor,
            'target': self.target,
            'result': self.result,
            'origin': self.origin,
            'instrument': self.instrument,
        })
        return d


@dataclass
class Collection(Object):
    totalItems: Optional[int] = None
    current: Optional[ActivityStreamsCollectionPageEntity] = None
    first: Optional[ActivityStreamsCollectionPageEntity] = None
    last: Optional[ActivityStreamsCollectionPageEntity] = None
    items: CollectionType[ActivityStreamsEntity] = None

    def __post_init__(self):
        assert self.items or (self.current or self.first or self.last), \
            "Collection must have either 'items' or first/current/last CollectionPages"

    def to_dict(self):
        d = super().to_dict()
        d.update({
            'totalItems': self.totalItems,
            'current': self.current,
            'first': self.first,
            'last': self.last,
            'items': self.items,
        })
        return d


@dataclass
class OrderedCollection(Collection):
    current: Optional[ActivityStreamsOrderedCollectionPageEntity] = None
    first: Optional[ActivityStreamsOrderedCollectionPageEntity] = None
    last: Optional[ActivityStreamsOrderedCollectionPageEntity] = None


@dataclass
class CollectionPage(Collection):
    partOf: Optional[ActivityStreamsCollectionEntity] = None
    next: Optional[ActivityStreamsCollectionPageEntity] = None
    prev: Optional[ActivityStreamsCollectionPageEntity] = None

    def to_dict(self):
        d = super().to_dict()
        d.update({
            'partOf': self.partOf,
            'next': self.next,
            'prev': self.prev,
        })
        return d


@dataclass
class OrderedCollectionPage(OrderedCollection):
    partOf: Optional[ActivityStreamsOrderedCollectionEntity] = None
    next: Optional[ActivityStreamsOrderedCollectionPageEntity] = None
    prev: Optional[ActivityStreamsOrderedCollectionPageEntity] = None

    def to_dict(self):
        d = super().to_dict()
        d.update({
            'partOf': self.partOf,
            'next': self.next,
            'prev': self.prev,
        })
        return d
