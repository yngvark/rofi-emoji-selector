#!/usr/bin/python
import json
import os
import subprocess
import sys
from pathlib import Path

def get_emojis_from_file(emojiFilename):
    emojis = dict()
    with open(emojiFilename, 'r') as f:
        emojis = json.loads(f.read().strip())

    return emojis


def print_emojis(emojis):
    for item in emojis:
        print(f'{item["emoji"]} {item["description"]}')


def print_all_emojis():
    p = Path(os.path.abspath(__file__))

    print_emojis(get_emojis_from_file(p.parent.joinpath("emoji_favourites.json")))
    print_emojis(get_emojis_from_file(p.parent.joinpath("emoji.json")))


def copy_stdin_clipboard():
    clipboardCommand = 'xsel --input --clipboard'.split()

    choice = sys.argv[1]

    # 🐛 bug -> 🐛
    emoji = choice.split(" ")[0]

    #with open("out.txt", 'w') as f:
    #    f.write(emoji)

    subprocess.run(clipboardCommand, input=emoji.encode('utf-8'))


if len(sys.argv) == 1:
    print_all_emojis()
else:
    copy_stdin_clipboard()
