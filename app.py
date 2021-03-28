import os
import re
from flask import Flask
from py.ibgw import IBGW

app = Flask(__name__)

@app.route('/')
def home():
    return {'Test': 'It works!'}

@app.route('/run')
def run():
    # Prepare IBC config
    with open(os.environ.get('TWS_INSTALL_LOG'), 'r') as fp:
        install_log = fp.read()

    ibc_config = {
        'twsVersion': re.search('IB Gateway ([0-9]{3})', install_log).group(1),
        'gateway': True,
        'tradingMode': 'paper',
        'ibcIni': os.environ.get('ibcIni'),
        'ibcPath': os.environ.get('ibcPath'),
        'javaPath': os.environ.get('javaPath') + f'/{os.listdir(os.environ.get("javaPath"))[0]}/bin',
        'twsPath': os.environ.get('twsPath'),
        'twsSettingsPath': os.environ.get('twsSettingsPath'),
        'userid': os.environ.get('TWSUSERID'),
        'password': os.environ.get('TWSPASSWORD')
    }

    # Initialize
    ibgw = IBGW(ibc_config)
    
    # Connect
    try:
        ibgw.start_and_connect()
        return {'Success': 'Connected to IB Gateway.'}
    except TimeoutError:
        return {'Timeout Error': 'Could not connect to IB Gateway.'}
