import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'DX\r\x9ea\r>\xd8\xda\xb0\x81\xb4ar\x03\xbb'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment'
                         }