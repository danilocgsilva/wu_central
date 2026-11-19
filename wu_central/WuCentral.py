from wu_central.interfaces.WuCentralInterface import WuCentralInterface
from programatic_x.factory.ButtonStartFactory import ButtonStartFactory
from programatic_x.LongType import LongType

class WuCentral(WuCentralInterface):
    def openWhatsUp(self):
        button_start_factory = ButtonStartFactory()
        long_type = LongType()

        button_start = button_start_factory.create_button_start()
        button_start.click()
        long_type.type("whatsapp")
        
        