import os

from setuptools import setup, find_packages

requires = [
    ]

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

setup(name='pygitversion',
      version='0.1',  # <grin> the irony is that the script itself need the manual way to store the versioning string...
      description='Extract Git information into a file',
      long_description=README + '\n\n' + CHANGES,
      author='',
      author_email='',
      url='https://github.com/axd1967/pygit-version.git',
      keywords='git',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points={
          'console_scripts': ['update_version_info=pygitversion.update:main'],
      }
      )
