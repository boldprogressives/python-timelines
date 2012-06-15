from setuptools import setup, find_packages
import sys, os

version = '0.2'

try:
    long_description = open("timelines/timelines.txt").read()
except:
    long_description = ""
try:
    long_description = "%s\n%s" % (long_description, open("NEWS.txt").read())
except:
    pass

setup(name='timelines',
      version=version,
      description="timespan and scheduling helpers for Python",
      long_description=long_description,
      classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
      ],
      keywords='',
      author='Ethan Jucovy',
      author_email='ethan@boldprogressives.org',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ],
      entry_points="""
      """,
      )
