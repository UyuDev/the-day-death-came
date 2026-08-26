from maps.house import house_map
from maps.dungeon import dungeon_map
from maps.town import town_map
from maps.house_upstairs import house_upstairs_map
from maps.basement import basement_map
from maps.pitchblack import pitch_black_map

MAPS = {
    "house": house_map,
    "house_upstairs": house_upstairs_map,
    "basement": basement_map,
    "pitch black": pitch_black_map,
    "dungeon": dungeon_map,
    "town": town_map,
}