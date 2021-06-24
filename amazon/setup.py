# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name='project',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = amazon.settings']}, install_requires=['pymysql', 'scrapy', 'twisted',
                                                                               'beautifulsoup4', 'requests']
)
