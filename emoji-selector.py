#!/usr/bin/python
import json
import os
import subprocess
import sys

def print_emojis():
    EMOJI_DICT_PATH = "emoji.json"

    emojis = dict()
    with open(EMOJI_DICT_PATH, 'r') as f:
        emojis = json.loads(f.read().strip())
    list_output = ''
    for item in emojis:
        print(f'{item["emoji"]} {item["description"]}')

def copy_stdin_clipboard():
    CLIPBOARD_COMMAND = 'xsel --input --clipboard'.split()

    choice = sys.argv[1]

    # 🐛 bug -> 🐛
    emoji = choice.split(" ")[0]

    #with open("out.txt", 'w') as f:
    #    f.write(emoji)

    subprocess.run(CLIPBOARD_COMMAND, input=emoji.encode('utf-8'))


if len(sys.argv) == 1:
    print_emojis()
else:
    copy_stdin_clipboard()
