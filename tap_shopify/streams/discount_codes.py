import shopify

from tap_shopify.streams.base import Stream
from tap_shopify.context import Context


class DiscountCodes(Stream):
    name = 'discount_codes'
    replication_object = shopify.DiscountCode

Context.stream_objects['discount_codes'] = DiscountCodes