from setuptools import setup, find_packages

setup(name='ir-exportq',
      version='0.0',
      packages= find_packages(),
      install_requires=[
          'celery==3.1.22',
          'pymongo==3.2.1',
      ],
)