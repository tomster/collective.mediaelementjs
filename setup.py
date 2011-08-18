from setuptools import setup, find_packages
import os

version = '0.1'

tests_require = ['collective.testcaselayer', 'interlude']

setup(name='collective.mediaelementjs',
    version=version,
    description="A simple integration of the `MediaElementJS <http://mediaelementjs.com/>`_ video player for Plone.",
    long_description=open("README.rst").read() + "\n" +
    open(os.path.join("docs", "HISTORY.rst")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
    "Framework :: Plone",
    "Programming Language :: Python",
    ],
    keywords='video plone mp4 html5',
    author='Tom Lazzr',
    author_email='tom@tomster.org',
    url='http://svn.plone.org/svn/collective/',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'setuptools',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
