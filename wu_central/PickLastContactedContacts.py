from programatic_x.Image import Image
import pyautogui
from typing import Dict, List
from programatic_x.named_tuples.Coordinate import Coordinate
from programatic_x.named_tuples.XYsize import XYsize

class PickLastContactedContacts:
    def pick(self, lasting_contact_name: str):
        centers_and_sizes = self._getImageIconWindowCenter()
        print(centers_and_sizes)
        
        for image_name, (coordinates, _) in centers_and_sizes.items():
            print(f"--- {image_name} ---")
            for center in coordinates:
                print(center)
                pyautogui.moveTo(center[0], center[1], 1)

    def _getImageIconWindowCenter(self) -> Dict[str, tuple[List[Coordinate], List[XYsize]]]:
        wu_images = [
            ("WhatsApp_1.5x_window_icon.png", 150),
            ("WhatsApp_dark_1.5x_window_icon.png", 150),
            ("WhatsApp_1x_window_icon.png", 100),
            ("wu_web_dark_1x.png", 100)
        ]

        confidence = 0.9
        image_instance = Image()
        results: Dict[str, tuple[List[Coordinate], List[XYsize]]] = {}
        
        for icon_imagem_string, scale in wu_images:
            centers = image_instance.get_centers(
                icon_imagem_string, 
                confidence, 
                "wu_central", 
                "assets"
            )
            image_name = icon_imagem_string.split('.')[0]
            dimensions = image_instance.get_dimensions()
            results[image_name] = (centers, dimensions)
        
        return results
            
    def _moveToFirstContact(self, scale: float, center_origin_position: tuple):
        move_x = 87 * scale
        move_y = 216 * scale
        new_x_position = center_origin_position[0] + move_x
        new_y_position = center_origin_position[1] + move_y
        pyautogui.moveTo(new_x_position, new_y_position, 1)
