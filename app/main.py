import os
import re
from flask import Flask
from utils.ibgw import IBGW

app = Flask(__name__)

@app.route('/')
def home():
    print('DB USER:', os.environ.get('DB_USER'))
    print('DB PASS:', os.environ.get('DB_PASS'))
    print('DB NAME:', os.environ.get('DB_NAME'))
    print('DB SOCKET DIR:'. os.environ.get('DB_SOCKET_DIR', '/cloudsql'))
    print('CLOUD SQL CONNECTION NAME:'. os.environ.get('CLOUD_SQL_CONNECTION_NAME'))
    return {'Test': 'It works!'}

@app.route('/run')
def run():
    # Prepare IBC config
    with open(os.environ.get('TWS_INSTALL_LOG'), 'r') as fp:
        install_log = fp.read()

    ibc_config = {
        # Provided on Docker build
        'twsVersion': re.search('IB Gateway ([0-9]{3})', install_log).group(1),
        'gateway': True,
        'ibcIni': os.environ.get('ibcIni'),
        'ibcPath': os.environ.get('ibcPath'),
        'javaPath': os.environ.get('javaPath') + f'/{os.listdir(os.environ.get("javaPath"))[0]}/bin',
        'twsPath': os.environ.get('twsPath'),
        'twsSettingsPath': os.environ.get('twsSettingsPath'),
        # Provided by Cloud Run
        'tradingMode': os.environ.get('TRADING_MODE'),
        'userid': os.environ.get('TWSUSERID'),
        'password': os.environ.get('TWSPASSWORD')
    }

    # Initialize
    ibgw = IBGW(ibc_config)
    
    # Connect
    try:
        ibgw.start_and_connect()
        ibgw.stop_and_terminate()
        return {'Success': 'Connected to IB Gateway.'}
    except TimeoutError:
        return {'Timeout Error': 'Could not connect to IB Gateway.'}
