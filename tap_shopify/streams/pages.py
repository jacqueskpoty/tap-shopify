import shopify

from tap_shopify.streams.base import Stream
from tap_shopify.context import Context


class Pages(Stream):
    name = 'pages'
    replication_object = shopify.Page

Context.stream_objects['pages'] = Pages