from maps.house import house_map
from maps.dungeon import dungeon_map
from maps.farm import farm_map
from maps.house_upstairs import house_upstairs_map
from maps.basement import basement_map
from maps.basement_2 import basement_map_2
from maps.pitchblack import pitch_black_map
from maps.tunnel_1 import tunnel_1_map
from maps.tunnel_2 import tunnel_2_map
from maps.sewer import sewer_map
from maps.crypt_1 import crypt_1_map
from maps.crypt_2 import crypt_2_map
from maps.crypt_3 import crypt_3_map

MAPS = {
    "house": house_map,
    "house_upstairs": house_upstairs_map,
    "basement": basement_map,
    "basement 2": basement_map_2,
    "pitch black": pitch_black_map,
    "tunnel 1": tunnel_1_map,
    "tunnel 2": tunnel_2_map,
    "sewer": sewer_map,
    "dungeon": dungeon_map,
    "crypt 1": crypt_1_map,
    "crypt 2": crypt_2_map,
    "crypt 3": crypt_3_map,
    "farm outside": farm_map,
}