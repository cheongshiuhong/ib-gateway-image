import logging
from flask import Flask
from lib.ibgw.config import IBC_CONFIG
from lib.ibgw.clients import TradeClient, ReconClient
from lib.db import DbClient

app = Flask(__name__)

@app.route('/')
def home():
    data = {}
    return {'Test': 'It works!', 'data': data}

# ----------------------------------------------------
# Test route to test if IB Gateway setup is working
# ----------------------------------------------------
@app.route('/test-ib')
def test_ib():
    # Initialize
    client = TradeClient(IBC_CONFIG)

    return client.pipe(
        initial_state={},
        funcs=[
            lambda x: { 'Success': 'Connected to IB Gateway.', **x }
        ]
    )

# ----------------------------------------------------
# Test route to test if DB setup is working
# ----------------------------------------------------
@app.route('/test-db')
def test_db():
    # Initialize
    client = DbClient()

    return { 'Success': 'Client initalized' }

# ----------------------------------------------------
# Screen route to screen for stocks to inlcude
# ----------------------------------------------------
@app.route('/screen')
def screen():
    return {'screen': 'screen'}

# ----------------------------------------------------
# HMMW route to trade with Hidden Markov Model
# ----------------------------------------------------
@app.route('/trade-hmmw')
def trade_hmmw():
    # Initialize
    client = TradeClient(IBC_CONFIG)
    client.start_and_connect()
    client.stop_and_terminate()

    return { 'trade': 'hmmwtrade' }

# ----------------------------------------------------
# Reconcilate route to reconciliate account stats
# ----------------------------------------------------
@app.route('/reconciliate')
def reconciliate():
    client = ReconClient(IBC_CONFIG)
    
    return client.pipe(
        initial_state={},
        funcs=[
            client.get_account_stats
        ] 
    )
