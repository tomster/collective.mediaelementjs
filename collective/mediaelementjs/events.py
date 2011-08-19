from zope.cachedescriptors import property
from zope.interface import alsoProvides, noLongerProvides

from collective.mediaelementjs.interfaces import IVideo, IMediaInfo
from collective.mediaelementjs.metadata_extraction import parse_raw
from collective.mediaelementjs.metadata_extraction import defensive_get

from Products.ATContentTypes import interface
from Products.Archetypes.interfaces import IObjectInitializedEvent

from StringIO import StringIO

VIDEO_EXTENSIONS = ['.mp4', '.m4v',]

def remove_marker(object):
    changed = False
    if IVideo.providedBy(object):
        noLongerProvides(object, IVideo)
        changed = True
    if changed:
        object.reindexObject(idxs=['object_provides'])


class ChangeView(object):

    interface = None
    value = None
    file_handle = None

    def __init__(self, object, event):
        self.object = object
        # TODO: do we really need this different from object?
        self.content = content = event.object
        if not self.interface.providedBy(content): return
        if self.value is None:
            remove_marker(content)
            return

        ext = self.check_extension()
        if ext is None:
            remove_marker(content)
            return

        # set the view to mediaelementjs view
        if IObjectInitializedEvent.providedBy(event):
            content.setLayout('mediaelementjs')

        if ext in VIDEO_EXTENSIONS:
            self.handleVideo()

    def check_extension(self):
        for ext in VIDEO_EXTENSIONS:
            if self.filename.endswith(ext):
                return ext
        return None

    def handleVideo(self):
        handle = self.file_handle
        metadata = parse_raw(handle)
        handle.close()
        
        if not IVideo.providedBy(self.content):
            alsoProvides(self.content, IVideo)
            self.object.reindexObject(idxs=['object_provides'])

        info = IMediaInfo(self.content)
        info.height = defensive_get(metadata, 'height')
        info.width = defensive_get(metadata, 'width')
        info.duration = defensive_get(metadata, 'duration')


class ChangeFileView(ChangeView):

    interface = interface.IFileContent

    @property.Lazy
    def value(self):
        return self.content.getField('file').getRaw(self.content)

    @property.Lazy
    def filename(self):
        filename = self.value.filename
        if isinstance(filename, basestring):
            filename = filename.lower()
        return filename

    @property.Lazy
    def file_handle(self):
        file_object = self.value
        try:
            # For blobs
            file_handle = file_object.getIterator()
        except AttributeError:
            file_handle = StringIO(str(file_object.data))
        return file_handle

