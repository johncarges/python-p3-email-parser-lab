# your code goes here!
import re

class EmailAddressParser:

    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        split_pattern = re.compile(r'[\s,]{1,}')
        split_array = split_pattern.split(self.addresses)

        regex = re.compile(r"[A-z]([A-z0-9]+[\.]{0,1})[A-z0-9]+@[A-z0-9]+[.][a-z]{2,}")
        validated_array = [address for address in split_array if regex.match(address)]


        return sorted(validated_array)

    