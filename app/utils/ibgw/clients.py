from .base import IBGWBase

class IBGWMain(IBGWBase):
    
    def __init__(self, ibc_config, ib_config={}, connection_timeout=60, per_sleep=2):
        super().__init__(ibc_config, ib_config, connection_timeout, per_sleep)
