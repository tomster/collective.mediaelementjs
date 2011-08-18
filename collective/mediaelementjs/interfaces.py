from zope.interface import Interface

class IMediaElementJSPlayable(Interface):
    """A file playable with mediaelementjs
    """

class IVideo(IMediaElementJSPlayable):
    """Marker interface for files that contain mp4 content
    """

