from wu_central.interfaces.WuCentralInterface import WuCentralInterface
from programatic_x.factory.ButtonStartFactory import ButtonStartFactory
from programatic_x.LongType import LongType
from time import sleep
import pyautogui

class WuCentral(WuCentralInterface):
    def openWhatsUp(
        self, 
        smooth_time: int = 0, 
        await_time: int = 0,
        await_start_type: int = 0,
        character_interval_typing_ms: int = 1,
        await_accept: int = 1
    ):
        button_start_factory = ButtonStartFactory()
        long_type = LongType()

        button_start = button_start_factory.create_button_start()
        button_start.click(smooth_time, await_time)
        if not await_start_type == 0:
            sleep(await_start_type)
        long_type.type("whatsapp", character_interval_typing_ms)
        sleep(await_accept)
        pyautogui.press("enter")

    def openWhatsUpAuto(self):
        self.openWhatsUp(3, 1, 1, 100)
        
        