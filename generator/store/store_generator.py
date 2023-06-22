from store.store_name_generator import NameGenerator
from common.address_generator import AddressGenerator
from models.store import Store

import uuid

class StoreGenerator:
    def __init__(self):
        self.store_id = uuid.uuid4()
        self.store_name = NameGenerator()
        self.address = AddressGenerator()

    def generate_data(self):
        store_name = self.store_name.generate_name()
        address = self.address.generate_address()[0]
        store_info = f'{store_name} {self.address.generate_address()[1]}'

        return Store(self.store_id, store_info, store_name, address)
        