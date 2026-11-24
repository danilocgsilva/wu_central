from programatic_x.Image import Image
import pyautogui

class PickLastContactedContacts:
    def pick(self, lasting_contact_name: str):
        self._getImageIconWindowCenter()

    def _getImageIconWindowCenter(self):
        wu_images = [
            ("WhatsApp_1.5x_window_icon.png", 150),
            ("WhatsApp_1x_window_icon.png", 100)
        ]

        confidence = 0.8
        image_instance = Image()
        for icon_imagem_string, scale in wu_images:
            print("---")
            centers = image_instance.get_centers(icon_imagem_string, confidence, "wu_central", "assets")
            print(centers)
            for center in centers:
                print(center)
                pyautogui.moveTo(center[0], center[1], 1)
            

