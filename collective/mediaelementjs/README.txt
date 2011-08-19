.. -*-doctest-*-


=========================
collective.mediaelementjs
=========================

Open a browser and log in as a normal user.

    >>> from Products.Five.testbrowser import Browser
    >>> from Products.PloneTestCase import ptc
    >>> browser = Browser()
    >>> browser.handleErrors = False
    >>> browser.open(portal.absolute_url())
    >>> browser.getLink('Log in').click()
    >>> browser.getControl('Login Name').value = ptc.default_user
    >>> browser.getControl(
    ...     'Password').value = ptc.default_password
    >>> browser.getControl('Log in').click()


Add an mp4 file to a folder.

    >>> import os
    >>> from collective.mediaelementjs import tests
    >>> browser.open(folder.absolute_url())
    >>> browser.getLink('File').click()
    >>> ctrl = browser.getControl(name="file_file")
    >>> opened = open(
    ...     os.path.join(os.path.dirname(tests.__file__), 'barsandtone.mp4'))
    >>> ctrl.add_file(opened, 'video/x-mp4', 'barsandtone.mp4')
    >>> browser.getControl('Save').click()
    >>> opened.close()
    >>> print browser.contents
    <...
    ...Changes saved...

The file now provides IVideo and the display layout has automatically
been set to the mediaelementjs view.

    >>> from collective.mediaelementjs import interfaces
    >>> interfaces.IVideo.providedBy(folder['barsandtone.mp4'])
    True
    >>> folder['barsandtone.mp4'].getLayout()
    'mediaelementjs'
    >>> contents = browser.contents
    >>> '++resource++collective.mediaelementjs/mediaelement-and-player.min.js">' in contents
    True
    >>> '++resource++collective.mediaelementjs/mediaelementplayer.min.css)' in contents
    True
    >>> 'href="http://nohost/plone/Members/test_user_1_/barsandtone.mp4"' in contents
    True

The width and height of the movie are set in the video tag::

  >>> '<video width="360" height="288"' in contents
  True

As well as the duration::

  >>> '0:00:06.014000' in contents
  True

