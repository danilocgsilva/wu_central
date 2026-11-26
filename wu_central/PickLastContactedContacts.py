from programatic_x.Image import Image
import pyautogui
from datetime import datetime
from pathlib import Path
from typing import Dict, List
from programatic_x.named_tuples.Coordinate import Coordinate
from programatic_x.named_tuples.XYsize import XYsize

class PickLastContactedContacts:
    def pick(self, lasting_contact_name: str):
        centers_and_sizes = self._getImageIconWindowCenter()
        valid_center_size = self._filterImageIconWindowCenter(centers_and_sizes)

        if not valid_center_size:
            raise RuntimeError("No valid image center and size were found.")
        image_name, center_size_scale = next(iter(valid_center_size.items()))
        scale = center_size_scale[2]
        center_found = center_size_scale[0]

        center_to_first_contact = self._moveToFirstContact(scale, center_found)

        print("-=-")
        print(center_to_first_contact.x)
        print(center_to_first_contact.y)
        print("-=-")

        self._contactPrintScreen(
            center_to_first_contact,
            60,
            40,
            180,
            40
        )
        
    def _getImageIconWindowCenter(
        self
    ) -> Dict[str, tuple[List[Coordinate], List[XYsize], float]]:
        wu_images = [
            ("WhatsApp_1.5x_window_icon.png", 1.5),
            ("WhatsApp_dark_1.5x_window_icon.png", 1.5),
            ("WhatsApp_1x_window_icon.png", 1.0),
            ("wu_web_dark_1x.png", 1.0)
        ]

        confidence = 0.9
        image_instance = Image()
        results: Dict[str, tuple[List[Coordinate], List[XYsize], float]] = {}
        
        for icon_imagem_string, scale in wu_images:
            detected_centers = image_instance.get_centers(
                icon_imagem_string, 
                confidence, 
                "wu_central", 
                "assets"
            )
            centers = [
                Coordinate(center[0], center[1])
                for center in detected_centers
            ]
            image_name = icon_imagem_string.split('.')[0]
            dimensions = image_instance.get_dimensions()
            results[image_name] = (centers, dimensions, scale)
        
        return results

    def _filterImageIconWindowCenter(
        self,
        results: Dict[str, tuple[List[Coordinate], List[XYsize], float]]
    ) -> Dict[str, tuple[Coordinate, XYsize, float]]:
        return {
            image_name: (coordinates[0], dimensions[0], scale)
            for image_name, (coordinates, dimensions, scale) in results.items()
            if coordinates and dimensions
        }
            
    def _moveToFirstContact(self, scale: float, center_origin_position: Coordinate) -> Coordinate:
        template_1 = (87, 216)
        template_2 = (87, 335)
        template = template_2
        move_x = template[0] * scale
        move_y = template[1] * scale

        new_x_position = center_origin_position.x + move_x
        new_y_position = center_origin_position.y + move_y

        pyautogui.moveTo(new_x_position, new_y_position, 1)
        return Coordinate(x = new_x_position, y = new_y_position)

    def _contactPrintScreen(
            self, 
            center: Coordinate,
            to_left: int = 60,
            to_top: int = 40,
            to_right: int = 60,
            to_bottom: int = 40
        ) -> Path:
        print_screens_path = Path("print_screens")
        print_screens_path.mkdir(exist_ok=True)

        screenshot_path = print_screens_path / f"{datetime.now():%Y%m%d-%H%M%S}.png"
        region = (int(center.x - to_left), int(center.y - to_top), to_left + to_right, to_top + to_bottom)
        pyautogui.screenshot(region=region).save(screenshot_path)
        return screenshot_path
