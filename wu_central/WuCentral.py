from wu_central.interfaces.WuCentralInterface import WuCentralInterface
from programatic_x.factory.ButtonStartFactory import ButtonStartFactory

class WuCentral(WuCentralInterface):
    def openWhatsUp(self):
        button_start_factory = ButtonStartFactory()
        button_start = button_start_factory.create_button_start()
        button_start.click()
        
        