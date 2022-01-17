import logging
from ib_insync.contract import Stock
from ib_insync.order import MarketOrder
from .base import IBGWBase

class TradeClient(IBGWBase):

    def __init__(self, ibc_config, ib_config={}, connection_timeout=90, per_sleep=2):
        super().__init__(ibc_config, ib_config, connection_timeout, per_sleep)

    def execute_stock_market_order(self, state):
        """
        Executes a market order

        :param state.ticker: ticker of the stock to trade
        :param state.exchange: exchange to trade on
        :param state.action: whether to BUY or SELL
        :param state.qty: number of stocks to trade
        """

        contract = Stock(state['ticker'], state['exchange'], self.CURR)
        order = MarketOrder(state['action'], state['qty'])
        self.placeOrder(contract, order)

        return state
