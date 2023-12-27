import os

lad = os.getenv('LOCALAPPDATA')

def main():
  os.system('cls')
  if os.path.isfile(f'{lad}\\Undertale_Yellow\\Save.sav'):
    Choice = input('Save found! Load debug onto current save? [Y/N] >>  ')
    if 'n' in Choice.lower():
      print('Canceled')
      os.system('pause')
    elif 'y' in Choice.lower():
      os.system('cls')
      convert()
    else:
      print('Unknown choice, please try again...')
      os.system('pause')
      main()
  else:
    print(f"Undertale Yellow save not found. Make sure your save is located at {lad}\\Undertale_Yellow\\Save.sav")
    os.system("pause")

def convert():
  with open(f'{lad}\\Undertale_Yellow\\Save.sav', 'r') as f:
    lines = f.readlines()
  with open(f'{lad}\\Undertale_Yellow\\Save.sav', 'w') as f:
    for i,line in enumerate(lines):
      if 'room="' in line:
        line = 'room="rm_mainmenu_debug"\n'
        lines[i] = line
    Choice = input('Done! Would you like to change your LV? [Y/N] >>  ')
    if 'n' in Choice.lower():
      os.system('cls')
    elif 'y' in Choice.lower():
      Choice = input('Enter a LOVE value, no extra characters >>  ')
      for i,line in enumerate(lines):
        if 'LV="' in line:
          line = f'LV="{Choice}.000000"\n'
          lines[i] = line

    f.writelines(lines)
    os.system('cls')
    f.close

  print('Done! Launch Yellow and make sure it works.')

main()