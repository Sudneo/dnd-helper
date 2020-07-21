#!/usr/bin/env python3
import argparse
import json
from helpers.spells import *
from helpers.classes import *


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--dndclass', help="Get all spells for a certain class")
    parser.add_argument('-l', '--level', help="Spell level", type=int)
    parser.add_argument('-s', '--spell', help="Get a specific spell")
    parser.add_argument('-o', '--output', help="Output file")
    return parser.parse_args()


def main():
    arguments = get_args()
    if arguments.spell is not None:
        # Get description of a specific spell
        spell_info = get_spell_info_by_name(arguments.spell.lower())
        print(json.dumps(spell_info, indent=2, sort_keys=False))
        if arguments.output is not None:
            with open(arguments.output, "w") as fp:
                json.dump(spell_info, fp, indent=2, sort_keys=False)
        exit(0)
    if arguments.dndclass is not None:
        spell_list = get_class_spells(arguments.dndclass, arguments.level)
        print(json.dumps(spell_list, indent=2, sort_keys=True))
        if arguments.output is not None:
            with open(arguments.output, "w") as fp:
                json.dump({'spells': spell_list}, fp, indent=2, sort_keys=False)
        exit(0)


if __name__ == '__main__':
    main()
