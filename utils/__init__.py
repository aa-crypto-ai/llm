import os
from dotenv import load_dotenv

if not load_dotenv('settings.env'):
    raise Exception('settings.env not found, refer to the format of sample.env for example')

DATA_DIR = os.path.join('/usr/src/app/doc', os.environ['DATA_DIR'])
if not os.path.exists(DATA_DIR):
    raise Exception(f'{DATA_DIR} not found')
