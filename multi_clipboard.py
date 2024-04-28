import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'

def save_items(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)
    # clipboard.copy(json.dumps(data))

def load_items(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


if len(sys.argv) == 2:
    data = load_items(SAVED_DATA)
    command = sys.argv[1]
    if command == 'save':
        key = input('Enter key: ')
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        print('Saved')
    elif command == 'paste':
        key = input('Enter key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Copied to clipboard')
        else:
            print('Key not found')
        
    elif command == 'list':
        print(data)
    else:
        print('Unknown command')
else:
    print("Please specify a command: copy, paste, list")
    
    