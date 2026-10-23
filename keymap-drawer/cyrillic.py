"""Relabel the ua and ru layers of a parsed keymap with the letters macOS types there.

ZMK only sends US key positions; the Cyrillic letter comes from the macOS input
source (Ukrainian-PC / Russian-PC). keymap-drawer cannot know that, so this
script swaps the labels after `keymap parse`.

Usage: python cyrillic.py keymap.yaml
"""

import sys

import yaml

COMMON = {
    "Q": "Й", "W": "Ц", "E": "У", "R": "К", "T": "Е", "Y": "Н", "U": "Г", "I": "Ш",
    "O": "Щ", "P": "З", "[": "Х", "A": "Ф", "D": "В", "F": "А", "G": "П", "H": "Р",
    "J": "О", "K": "Л", "L": "Д", ";": "Ж", "Z": "Я", "X": "Ч", "C": "С", "V": "М",
    "B": "И", "N": "Т", "M": "Ь", ",": "Б", ".": "Ю", "/": ".", "Sft+/": ",",
}
LAYERS = {
    "ua": {**COMMON, "S": "І", "]": "Ї", "'": "Є", "`": "'", "\\": "Ґ"},
    "ru": {**COMMON, "S": "Ы", "]": "Ъ", "'": "Э", "`": "Ё", "\\": "\\"},
}

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    keymap = yaml.safe_load(f)

for layer, table in LAYERS.items():
    keys = keymap["layers"].get(layer, [])
    keymap["layers"][layer] = [table.get(k, k) if isinstance(k, str) else k for k in keys]

with open(path, "w", encoding="utf-8") as f:
    yaml.safe_dump(keymap, f, allow_unicode=True, sort_keys=False)
