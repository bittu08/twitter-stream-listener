# pylint: disable=W0401,W0614
import os
from settings import *

PROJECT_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
BASE_DIR = os.path.join(PROJECT_DIR, os.pardir)
STATIC_DIR = os.path.join(BASE_DIR, "src/static")
TEMPLATE_DIR = os.path.join(BASE_DIR, "src/templates")
OUT_DIR = os.path.join(BASE_DIR, "out")


DEBUG = True
TEMPLATE_DEBUG = DEBUG

BROKER_URL= 'redis://localhost:6379'
REDIS_URL = 'redis://localhost:6379'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    STATIC_DIR,
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_DIR,
)

TWITTER_CONFIG = {
	consumer_key="IN6zHMLbiYeWTRAG41IzEw",
	consumer_secret="gtT8Wdz3wW5fhkL1VNHi8IXiVOj4Z6JUyxIk6jyMTU",
	access_token="2416222890-QpC6kPa1fsbiADLxP0sPCf4wVF9zEa9wy5OTCbt",
	access_token_secret="bDWTVW5FB0DvSdsQA22ryfFXQdAdGyap2utBDQyqN1XJ2",
	index="twitter",
	doc_type="tweet"
}