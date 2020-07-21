# dnd-helper
Simple script to retrieve class spells or spells info

A **huge** thanks to the creators of dnd5eapi.co. 

## Usage

This script was done for my own use and consume, therefore might not suit everyone's needs.

```bash
./dnd.py -h
usage: dnd.py [-h] [-c DNDCLASS] [-l LEVEL] [-s SPELL] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -c DNDCLASS, --dndclass DNDCLASS
                        Get all spells for a certain class
  -l LEVEL, --level LEVEL
                        Spell level
  -s SPELL, --spell SPELL
                        Get a specific spell
  -o OUTPUT, --output OUTPUT
                        Output file

```

If `-s` switch is used, it has precedence over the other (i.e., the others are ignored).
In this case the string used as a parameter will be used to search a spell, and if one result
and only one result will be found, it will print useful information about it.

Example:

```json
./dnd.py -s "Mirror Image"
{
  "name": "Mirror Image",
  "school": "Illusion",
  "ritual": false,
  "casting_time": "1 action",
  "range": "Self",
  "components": [
    "V",
    "S"
  ],
  "concentration": false,
  "duration": "1 minute",
  "description": "Three illusionary duplicates of yourself appear in your space. Until the end of the spell, duplicates move with you and imitate your actions, swapping their position so that it is impossible to determine which image is real. You can use your action to dispel the illusory duplicates. Whenever a creature is targeting you with an attack during the duration of the spell, roll 1d20 to determine if the attack does not target rather one of your duplicates. If you have three duplicates, you need 6 or more on your throw to lead the target of the attack to a duplicate. With two duplicates, you need 8 or more. With one duplicate, you need 11 or more. The CA of a duplicate is 10 + your Dexterity modifier. If an attack hits a duplicate, it is destroyed. A duplicate may be destroyed not just an attack on key. It ignores other damage and effects. The spell ends if the three duplicates are destroyed. A creature is unaffected by this fate if she can not see if it relies on a different meaning as vision, such as blind vision, or if it can perceive illusions as false, as with clear vision.",
  "level": 2
}
```

If `-c` switch is used, the parameter will be used to query a class spells. Each spell will be printed
with all its info (equivalent to using `-s` for every spell).
If `-l` switch is used together with `-c`, the spells will be filtered by the level specified.

Example:

```json
./dnd.py -c Paladin -l 5
[
  {
    "casting_time": "1 action",
    "components": [
      "V",
      "S",
      "M"
    ],
    "concentration": true,
    "description": "Shimmering energy surrounds and protects you from fey, undead, and creatures originating from beyond the Material Plane. For the duration, celestials, elementals, fey, fiends, and undead have disadvantage on attack rolls against you. You can end the spell early by using either of the following special functions. Break Enchantment. As your action, you touch a creature you can reach that is charmed, frightened, or possessed by a celestial, an elemental, a fey, a fiend, or an undead. The creature you touch is no longer charmed, frightened, or possessed by such creatures. Dismissal. As your action, make a melee spell attack against a celestial, an elemental, a fey, a fiend, or an undead you can reach. On a hit, you attempt to drive the creature back to its home plane. The creature must succeed on a charisma saving throw or be sent back to its home plane (if it isn't there already). If they aren't on their home plane, undead are sent to the Shadowfell, and fey are sent to the Feywild.",
    "duration": "Up to 1 minute",
    "level": 5,
    "name": "Dispel Evil and Good",
    "range": "Self",
    "ritual": false,
    "school": "Abjuration"
  },...
```

The `-o` switch can be used to save the result to a file (still json).