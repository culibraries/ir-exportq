from setuptools import setup, find_packages

setup(name='ir-exportq',
      version='1.0',
      packages=find_packages(),
      install_requires=[
          'requests',
          'boto3'
      ],
      )
