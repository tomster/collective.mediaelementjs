from plone.rfc822.interfaces import IPrimaryFieldInfo
from collective.mediaelementjs.browser.view import File as FileViewBase

class MediaElementJSFileView(FileViewBase):
    def getFilename(self):
        info = IPrimaryFieldInfo(self.context)
        return info.value.filename
