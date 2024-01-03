import cfbd
import os

def configure_cfbd():
    configuration = cfbd.Configuration()
    configuration.api_key['Authorization'] = os.getenv("CFBD_API_KEY")
    configuration.api_key_prefix['Authorization'] = 'Bearer'
    return configuration
