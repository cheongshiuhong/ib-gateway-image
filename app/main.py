import os
import re
from flask import Flask
from utils.ibgw.clients import IBGWMain

app = Flask(__name__)

# Prepare IBC config
with open(os.environ.get('TWS_INSTALL_LOG'), 'r') as fp:
    INSTALL_LOG = fp.read()

IBC_CONFIG = {
    # Provided on Docker build
    'twsVersion'     : re.search('IB Gateway ([0-9]{3})', INSTALL_LOG).group(1),
    'gateway'        : True,
    'ibcIni'         : os.environ.get('ibcIni'),
    'ibcPath'        : os.environ.get('ibcPath'),
    'javaPath'       : os.environ.get('javaPath') + f'/{os.listdir(os.environ.get("javaPath"))[0]}/bin',
    'twsPath'        : os.environ.get('twsPath'),
    'twsSettingsPath': os.environ.get('twsSettingsPath'),
    
    # Provided by Cloud Run
    'tradingMode'    : os.environ.get('TRADING_MODE'),
    'userid'         : os.environ.get('TWSUSERID'),
    'password'       : os.environ.get('TWSPASSWORD')
}

@app.route('/')
def home():
    data = {}
    return {'Test': 'It works!', 'data': data}

@app.route('/test')
def test():
    # Initialize
    ibgw = IBGWMain(IBC_CONFIG)

    return ibgw.pipe([
        lambda x: {'Success': 'Connected to IB Gateway.', **x}
    ])
