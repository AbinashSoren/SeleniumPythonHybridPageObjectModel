from datetime import datetime

import pytest


@pytest.mark.usefixtures('setup_and_teardown')
class BaseTest:

    def generate_email_time_stamp(self):
        timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timestamp=timestamp.replace('-',"_").replace(' ','').replace(':','_')
        return 'abinash'+timestamp+'soren@gmail.com'