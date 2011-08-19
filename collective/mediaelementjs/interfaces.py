from zope.interface import Interface
from zope import schema

from collective.mediaelementjs import MessageFactory as _

class IMediaElementJSPlayable(Interface):
    """A file playable with mediaelementjs
    """

class IVideo(IMediaElementJSPlayable):
    """Marker interface for files that contain mp4 content
    """

class IMediaInfo(Interface):
    """Information about a video object
    """
    width = schema.Int(title=_(u"Width"), required=False)
    height = schema.Int(title=_(u"Height"), required=False)
    duration = schema.Timedelta(title=_(u"Duration"), required=False)
