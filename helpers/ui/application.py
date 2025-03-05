from helpers.ui.common_steps import CommonHelper
from helpers.ui.info_steps import InfoHelper
from helpers.ui.category_steps import CategoryHelper


class Application:

    def __init__(self):
        self.common = CommonHelper()
        self.info = InfoHelper()
        self.category = CategoryHelper()
