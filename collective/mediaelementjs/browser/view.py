from Acquisition import aq_inner
import os

from Products.Five.browser import BrowserView


class File(BrowserView):

    def __init__(self, context, request):
        super(File, self).__init__(context, request)

    def videos(self):
        return[dict(url=self.href(),
                    title=self.context.Title(),
                    description=self.context.Description(),
                    )]

    def getFilename(self):
        context = aq_inner(self.context)
        return context.getFilename()

    def href(self):
        context = aq_inner(self.context)
        ext = ''
        url = self.context.absolute_url()
        filename = self.getFilename()
        if filename:
            extension = os.path.splitext(filename)[1]
            if not url.endswith(extension):
                ext = "?e=%s" % extension
        return self.context.absolute_url()+ext

