# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.mkd') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='maasapi',
    version='0.1.0',
    description='MAAS API',
    long_description=readme,
    author='Nathan Victor',
    author_email='howdy@nathanvictor.com',
    url='https://github.com/ingenology/mars_weather_api',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)