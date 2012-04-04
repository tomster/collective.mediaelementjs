from setuptools import setup, find_packages
import os

version = '0.1.4'

tests_require = ['collective.testcaselayer', 'interlude']

setup(name='collective.mediaelementjs',
    version=version,
    description="A simple integration of the MediaElementJS video player for Plone.",
    long_description=open("README.rst").read() + "\n" +
    open(os.path.join("docs", "HISTORY.rst")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
    "Framework :: Plone",
    "Programming Language :: Python",
    "Development Status :: 3 - Alpha",
    "Topic :: Multimedia :: Video :: Display",
    ],
    keywords='video plone mp4 html5',
    authors='Tom Lazar, Unweb.me',
    author_email='tom@tomster.org, we@unweb.me',
    url='https://github.com/collective/collective.mediaelementjs',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'setuptools',
      'hachoir_core',
      'hachoir_metadata',
      'hachoir_parser',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
