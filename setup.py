from setuptools import setup, find_packages

setup(
    name="tweetlistener",
    version="0.0.1",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools', 'Django', 'celery', 'gunicorn', 'django-tastypie', 'requests', 'redis', 'django-celery','parse', 'tweepy', 'elasticsearch', 'redis']
)
