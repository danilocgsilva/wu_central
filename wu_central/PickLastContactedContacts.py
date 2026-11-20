from programatic_x.Image import Image
import pyautogui

class PickLastContactedContacts:
    def pick(self, lasting_contact_name: str):
        # Lets see the upper left corner of the desktop window, so we can
        # calculate where to start to pick search for last contacts
        x, y = self._getImageIconWindowCenter()
        print(f"Position x: {x}")
        print(f"Position y: {y}")
        return x, y

    def _getImageIconWindowCenter(self):
        wu_images = [
            "WhatsApp_1.5x_window_icon.png",
            "WhatsApp_1x_window_icon.png"
        ]

        confidence = 0.6
        for icon_imagem_string in wu_images:
            try:
                print(f"Trying: {icon_imagem_string}")
                return Image.get_center(icon_imagem_string, confidence, "wu_central", "assets")
            except pyautogui.ImageNotFoundException:
                continue
        raise Exception("WhatsApp window icon not found.")

