from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from wu_central.WuCentral import WuCentral
from wu_central.PickLastContactedContacts import PickLastContactedContacts
from time import sleep
import pyautogui

pick_last_contacted_contacts = PickLastContactedContacts()
pick_last_contacted_contacts.pick("still_not")
