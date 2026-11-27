from enum import Enum
from wu_central.typed_dict.Template import Template

class MovingTemplate(Enum):
    WITH_LOCKED_AND_ARCHIVED = Template(
        center_reference = (87, 335),
        move_all_directions = {
            "to_left": 68,
            "to_up": 42,
            "to_right": 365,
            "to_bottom": 30
        }
    )
    SLIM = Template(
        center_reference = (87, 216),
        move_all_directions = {
            "to_left": 68,
            "to_up": 42,
            "to_right": 365,
            "to_bottom": 30
        }
    )
