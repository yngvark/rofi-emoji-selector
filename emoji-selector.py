#!/usr/bin/python
import json
import os
import subprocess
import sys
from pathlib import Path

def print_emojis():
    p = Path(os.path.abspath(__file__))
    emojiFile = p.parent.joinpath("emoji.json")

    emojis = dict()
    with open(emojiFile, 'r') as f:
        emojis = json.loads(f.read().strip())
    list_output = ''
    for item in emojis:
        print(f'{item["emoji"]} {item["description"]}')

def copy_stdin_clipboard():
    clipboardCommand = 'xsel --input --clipboard'.split()

    choice = sys.argv[1]

    # 🐛 bug -> 🐛
    emoji = choice.split(" ")[0]

    #with open("out.txt", 'w') as f:
    #    f.write(emoji)

    subprocess.run(clipboardCommand, input=emoji.encode('utf-8'))


if len(sys.argv) == 1:
    print_emojis()
else:
    copy_stdin_clipboard()
