from programatic_x.Image import Image
import pyautogui
from datetime import datetime
from pathlib import Path
from typing import Dict, List
from programatic_x.named_tuples.Coordinate import Coordinate
from programatic_x.named_tuples.XYsize import XYsize
from wu_central.enums.MovingTemplate import MovingTemplate
from wu_central.typed_dict.Template import Template

class PickLastContactedContacts:
    def pick(self, lasting_contact_name: str):
        centers_and_sizes = self._getImageIconWindowCenter()
        print(centers_and_sizes)
        valid_center_size = self._filterImageIconWindowCenter(centers_and_sizes)

        if not valid_center_size:
            raise RuntimeError("No valid image center and size were found.")
        image_name, center_size_scale = next(iter(valid_center_size.items()))
        scale = center_size_scale[2]
        center_found = center_size_scale[0]

        template = MovingTemplate.WITH_LOCKED_AND_ARCHIVED.value
        center_to_first_contact = self._moveToFirstContact(scale, center_found, template)

        self._contactPrintScreen(
            center_to_first_contact,
            template
        )

        next_center = Coordinate(
            x=center_to_first_contact.x, 
            y=center_to_first_contact.y + 80
        )

        self._contactPrintScreen(
            next_center,
            template
        )

        next_center = Coordinate(
            x=next_center.x, 
            y=next_center.y + 80
        )

        self._contactPrintScreen(
            next_center,
            template
        )

        next_center = Coordinate(
            x=next_center.x, 
            y=next_center.y + 80
        )

        self._contactPrintScreen(
            next_center,
            template
        )
        
    def _getImageIconWindowCenter(
        self
    ) -> Dict[str, tuple[List[Coordinate], List[XYsize], float]]:
        wu_images = [
            ("WhatsApp_1.5x_window_icon.png", 1.5),
            ("WhatsApp_dark_1.5x_window_icon.png", 1.5),
            ("WhatsApp_1x_window_icon.png", 1.0),
            ("wu_web_dark_1x.png", 1.0),
            ("wu_web_dark_poured_1x.png", 1.0)
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
            
    def _moveToFirstContact(
        self, 
        scale: float, 
        center_origin_position: Coordinate, 
        template_value: Template
    ) -> Coordinate:        
        move_x = template_value["center_reference"][0] * scale
        move_y = template_value["center_reference"][1] * scale

        new_x_position = center_origin_position.x + move_x
        new_y_position = center_origin_position.y + move_y

        pyautogui.moveTo(new_x_position, new_y_position, 1)
        return Coordinate(x = new_x_position, y = new_y_position)

    def _contactPrintScreen(
            self, 
            center: Coordinate,
            template: Template
        ) -> Path:
        print_screens_path = Path("print_screens")
        print_screens_path.mkdir(exist_ok=True)

        to_left = template["move_all_directions"]["to_left"]
        to_top = template["move_all_directions"]["to_up"]
        to_right = template["move_all_directions"]["to_right"]
        to_bottom = template["move_all_directions"]["to_bottom"]

        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        screenshot_path = print_screens_path / f"{timestamp}.png"
        suffix = 1
        while screenshot_path.exists():
            screenshot_path = print_screens_path / f"{timestamp}-{suffix:03d}.png"
            suffix += 1

        region = (int(center.x - to_left), int(center.y - to_top), to_left + to_right, to_top + to_bottom)
        pyautogui.screenshot(region=region).save(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
        return screenshot_path
