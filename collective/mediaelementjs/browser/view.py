from Acquisition import aq_inner
import os

from Products.Five.browser import BrowserView

from collective.mediaelementjs.interfaces import IMediaInfo

class File(BrowserView):

    def __init__(self, context, request):
        super(File, self).__init__(context, request)

    def video(self):
        info = IMediaInfo(self.context)
        return dict(url=self.href(),
            title=self.context.Title(),
            description=self.context.Description(),
            height=info.height,
            width=info.width,
            duration=info.duration)

    def getFilename(self):
        context = aq_inner(self.context)
        return context.getFilename()

    def href(self):
        context = aq_inner(self.context)
        ext = ''
        url = context.absolute_url()
        filename = self.getFilename()
        if filename:
            extension = os.path.splitext(filename)[1]
            if not url.endswith(extension):
                ext = "?e=%s" % extension
        return self.context.absolute_url()+ext

