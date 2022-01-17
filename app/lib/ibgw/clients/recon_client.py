import logging
from ib_insync.contract import Stock
from ib_insync.order import MarketOrder
from .base import IBGWBase

class ReconClient(IBGWBase):
    TAGS = [
        'NetLiquidationByCurrency',
        'CashBalance',
        'StockMarketValue',
        'RealizedPnL',
        'UnrealizedPnL'
    ]

    def __init__(self, ibc_config, ib_config={}, connection_timeout=90, per_sleep=2):
        super().__init__(ibc_config, ib_config, connection_timeout, per_sleep)

    def get_account_stats(self, state):
        stats = {}
        stats['positions'] = self.positions()
        stats['accountValues'] = {
            self.TAGS[i]: v.value for i, v in \
                enumerate(
                    filter(
                        lambda x: x.tag in self.TAGS and x.currency == self.CURR,
                        self.accountValues()
                    )
                )
        }

        logging.info('Stats:', stats)
        return { **state, 'stats': stats }
