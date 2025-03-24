import os
import sys
import urllib.request
import platform

# Bestimme das Betriebssystem
system = platform.system()

try:
    import progressbar
except ImportError:
    print("Das 'progressbar2' Modul ist nicht installiert. Bitte installieren Sie es mit 'pip install progressbar2'.")
    sys.exit(1)

logo = r"""
   ______                          _ __        ____        __
  / ____/___  ____ ___  ____ ___  (_) /_      / __ )____  / /_
 / /   / __ \/ __ `__ \/ __ `__ \/ / __/_____/ __  / __ \/ __/
/ /___/ /_/ / / / / / / / / / / / / /_/_____/ /_/ / /_/ / /_
\____/\____/_/ /_/ /_/_/ /_/ /_/_/\__/     /_____/\____/\__/ lol
"""

while True:
    # Bildschirm leeren - plattformabhängig
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
    print(logo)
    print("\n\t\tCREATED BY SPEEDX | UPGRADED by 0xj0n1")
    print("\n\n1 - Start BOT ")
    print("2 - How To USE")
    print("3 - Exit")
    inp = input('Enter OPTION > ')
    
    if '1' in inp:
        url = 'https://www.google.com'
        try:
            urllib.request.urlopen(url)
        except:
            print('You Are Not Connected To Internet!!!\nPlease Connect To Internet To Continue....')
            print('For Any Queries Join Me On WhatsApp!!!')
            print('\t    Group Link: http://bit.do/speedxgit')
            print('\n             Mail: ggspeedx29@gmail.com')
            print('\n  YouTube Channel: https://www.youtube.com/c/GyanaTech')
            sys.exit(2)
        
        try:
            nc = int(input('Enter Number Of Commits To Do: '))
        except ValueError:
            print('[!] Error Please Enter A Valid Number...')
            input('Press Enter To Continue...')
            continue
        
        gu = input('Enter FULL Git Repository URL (including https://): ')
        gn = input('Enter Your Github UserName: ')
        ge = input('Enter Your Github E-Mail: ')
        
        if nc <= 1:
            print('[!] Error Please Enter Number of Commits Greater Than 1 ...')
            input('Press Enter To Continue...')
            continue
        
        if not gu.startswith('https'):
            print('\n\nALWAYS ENTER FULL REPOSITORY URL\n\tExample: https://github.com/TheSpeedX/commit-bot')
            input('\n\nPress Enter To Continue...')
            continue
        
        if gu.endswith('.git'):
            gu = gu[:-4]
        
        try:
            if urllib.request.urlopen(gu).getcode() != 200:
                raise Exception
        except:
            print('[!] Wrong Repository URL !!!')
            print('\n\nALWAYS ENTER FULL REPOSITORY URL\n\tExample: https://github.com/TheSpeedX/commit-bot\n')
            print('For Any Queries Join Me On WhatsApp!!!')
            print('\t    Group Link: http://bit.do/speedxgit')
            print('\n             Mail: ggspeedx29@gmail.com')
            print('\n  YouTube Channel: https://www.youtube.com/c/GyanaTech')
            input('\n\nPress Enter To Continue...')
            continue
           
        print('[+] Initializing....')
        
        # Windows-kompatible Befehle
        if not os.path.exists('test'):
            os.makedirs('test', exist_ok=True)
            print('[+] Test Directory Not Found Creating One ....')
        else:
            if system == 'Windows':
                os.system('cd test && del /s /q *')
            else:
                os.system('cd test && rm -rf *')
            print('[+] Test Directory Found Using It ....')
        
        print('[+] Preparing Directory...')
        print('[+] Pulling REMOTE Repository To Local Directory ...')
        
        # Git-Befehle sind plattformunabhängig
        os.system(f'cd test && git clone {gu}')
        rn = gu[gu.rfind('/') + 1:]
        
        # Dateien von Unterverzeichnis ins Hauptverzeichnis verschieben
        if system == 'Windows':
            os.system(f'xcopy /E /Y test\\{rn}\\* test\\ > NUL')
            os.system(f'xcopy /E /Y test\\{rn}\\.* test\\ > NUL 2>&1')
        else:
            os.system(f'mv -f test/{rn}/* test 2>/dev/null')
            os.system(f'mv -f test/{rn}/.??* test 2>/dev/null')
        
        os.system(f'cd test && git remote add origin {gu}')
        
        if system == 'Windows':
            os.system(f'rd /s /q test\\{rn}')
        else:
            os.system(f'cd test && rm -rf {rn}')
            
        print('[+] Repository Successfully Pulled')
        
        if not os.path.exists('test/README.md'):
            with open('test/README.md', 'w') as f:
                f.write('')
        
        with open('test/temp.speedx', 'w') as f:
            f.write('# This Repo Was Committed By SpeedX\'s Commit Bot\n')
            f.write('### GITHUB LINK\n')
            f.write('<a href=\'https://github.com/thespeedx/commit-bot\'> Click Here </a>\n\n')
        
        # Dateien zusammenführen
        if system == 'Windows':
            try:
                with open('test/README.md', 'r', encoding='utf-8', errors='ignore') as readme:
                    content = readme.read()
                with open('test/temp.speedx', 'r', encoding='utf-8') as temp:
                    temp_content = temp.read()
                with open('test/tmp.xxxx', 'w', encoding='utf-8') as tmp:
                    tmp.write(temp_content + content + temp_content)
                os.system('cd test && copy /Y tmp.xxxx README.md')
                os.system('cd test && del temp.speedx tmp.xxxx')
            except Exception as e:
                print(f"Fehler beim Bearbeiten der README.md: {e}")
                print("Erstelle eine neue README.md...")
                with open('test/README.md', 'w', encoding='utf-8') as f:
                    f.write('# Repository bearbeitet mit Commit-Bot\n')
        else:
            os.system('cat test/temp.speedx test/README.md test/temp.speedx > test/tmp.xxxx')
            os.system('cd test && mv tmp.xxxx README.md')
            os.system('cd test && rm temp.speedx')
        
        os.system(f'cd test && git config user.name "{gn}"')
        os.system(f'cd test && git config user.email "{ge}"')
        os.system('cd test && git add .')
        
        print('[+] Directory Initialized')
        print('[+] Starting Commits To Gain Contribution...')
        
        for i in progressbar.progressbar(range(nc - 1), redirect_stdout=True):
            if system == 'Windows':
                with open('test/temp.speedx.xxx', 'a') as f:
                    f.write('THIS IS A COMMIT BY SPEEDX COMMIT BOT\n')
                os.system('cd test && git add temp.speedx.xxx . > NUL 2>&1')
                os.system('cd test && git commit -m "Commit By SpeedX Bot!!!" > NUL 2>&1')
            else:
                os.system('echo "THIS IS A COMMIT BY SPEEDX COMMIT BOT" >> test/temp.speedx.xxx')
                os.system('cd test && git add temp.speedx.xxx . > /dev/null')
                os.system('cd test && git commit -m \'Commit By SpeedX Bot!!!\' > /dev/null')
        
        print('\n[+] Cleaning Repository...')
        if system == 'Windows':
            os.system('del test\\temp.speedx.xxx')
        else:
            os.system('rm test/temp.speedx.xxx')
        
        os.system('cd test && git gc')
        print('[+] Repository Cleaned')
        print('[-] Final Commit')
        
        os.system('cd test && git add .')
        os.system('cd test && git commit -m "Commit By SpeedX Bot!!!"')
        print('[+] Pushing Repo To Remote URL: ' + gu)
        os.system('cd test && git push -u --force origin master')
        
        print(f'[+] {nc} Commits Done ... \n\t\tYou Can See it in your Contributions Soon\n\tIf You Don\'t Check Notes in README.md')
        print('[+] Closing Bot....')
        break
    
    elif '2' in inp:
        if system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        
        print('                       HELP')
        print('           -----------------------------')
        print(logo + '\n')
        print('This is A COMMIT BOT Created By SpeedX to get CONTRIBUTIONS For FREE...')
        print('This Script Generates Fake Commits And is Very Fast....')
        print('\nALWAYS USE AN EMPTY REPOSITORY WITH AN INITIAL COMMIT FOR COMMIT BOT!!\n')
        print('We Take The Following Inputs:\n')
        print('\t Number Of Commits -   To Generate That Amount Of Fake Commits')
        print('\t Repository URL    -   To Push And Pull Code To/From That Repository(Must Be Yours)')
        print('\t Github Username   -   Sometimes Github Asks For UserName (Enter A Real One) ...')
        print('\t Github Email      -   Sometimes Github Asks For Email (Enter A Real One) ...')
        print('\nWe Never Keep Your Github Username, Email or Password...')
        print('If You Don\'t Trust Us Then Push The Repository Yourself After Successful Commits By:')
        print('\t\tcd test && git push -u --force origin master')
        print('\n\tFor More Details Check README.md\nHope You Liked This Project!!!')
        print('You can Check My Other Projects Here: https://github.com/TheSpeedX')
        print('For Any Queries Join Me On WhatsApp!!!')
        print('\t    Group Link: http://bit.do/speedxgit')
        print('\n             Mail: ggspeedx29@gmail.com')
        print('\n  YouTube Channel: https://www.youtube.com/c/GyanaTech')
        input('\n\nPress Enter To Continue...')
    
    elif '3' in inp:
        break
    
    else:
        print("Invalid Input !!!\nTry Again!!!\n Press Enter To Continue...")
        input()

print(logo)
print('\nThanks For Using My Project')
print('PLEASE LEAVE A STAR IT, FORK IT, WATCH IT IF YOU LIKE IT')
print('You can Check My Other Projects Here: https://github.com/TheSpeedX')
print('For Any Queries Join Me On WhatsApp!!!')
print('\t    Group Link: http://bit.do/thespeedx')
print('\n             Mail: ggspeedx29@gmail.com')
print('\n  YouTube Channel: https://www.youtube.com/c/GyanaTech')
sys.exit(0)
