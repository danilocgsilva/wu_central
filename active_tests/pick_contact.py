from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from wu_central.WuCentral import WuCentral
from wu_central.PickLastContactedContacts import PickLastContactedContacts
from time import sleep
import pyautogui

wucentral = WuCentral()
wucentral.openWhatsUp(3, 1, 1, 100)
sleep(3)
pick_last_contacted_contacts = PickLastContactedContacts()
# x, y = pick_last_contacted_contacts.pick("still_not")
pick_last_contacted_contacts.pick("still_not")
# pyautogui.moveTo(x, y, 3)
