A simple integration of the `MediaElementJS <http://mediaelementjs.com/>`_ video player for Plone.

Large portions of this package have been blatantly copied from the `collective.flowplayer <http://pypi.python.org/pypi/collective.flowplayer>`_ product by Martin Aspeli.

What it does
============

Once installed, you can upload **h.264 baseline encoded .mp4 files** and they will automatically use a default view that renders the video using the MediaElementJS player.

MediaElementJS uses a HTML5 ``<video>`` tag, so any browser that can render .mp4 natively will do so (particularly any Safari browser, including iPhone and iPad). All others (i.e. those that cannot display ``<video>`` at all, such as older versions of IE or those which *can* but don't support the .h264 codec, such as Firefox or Opera) get the same video served via a Flash player. See the `MediaElementJS homepage <http://mediaelementjs.com/>`_ for more details.

Installation
============

Either use easy_install/pip or add it to your buildout. In either case, the name of the egg is ``collective.mediaelementjs``.

Then, simply install it from the ``prefs_install_products_form`` in Plone, as you would with any other Plone product.

