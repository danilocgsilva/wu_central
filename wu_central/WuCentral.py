from wu_central.interfaces.WuCentralInterface import WuCentralInterface
from programatic_x.factory.ButtonStartFactory import ButtonStartFactory
from programatic_x.LongType import LongType

class WuCentral(WuCentralInterface):
    def openWhatsUp(self, smooth_time: int = 0, await_time: int = 0):
        button_start_factory = ButtonStartFactory()
        long_type = LongType()

        button_start = button_start_factory.create_button_start()
        button_start.click(smooth_time, await_time)
        long_type.type("whatsapp")
        
        