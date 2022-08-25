import os, platform, time
print('\n\x1b[1;37m Checking Update...');time.sleep(0.5)
def Update():
    exit('\033[1;31m(×) Commands On Update Please Wait For Update ❤ ')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            print("\x1b[1;92m 𝗖𝗢𝗡𝗚𝗥𝗔𝗧𝗦 ! 𝗗𝗘𝗔𝗥, 𝗬𝗢𝗨𝗥 𝗗𝗘𝗩𝗜𝗖𝗘 𝗦𝗨𝗣𝗣𝗢𝗨𝗥𝗧 𝗧𝗛𝗜𝗦 𝗧𝗢𝗢𝗟")

            from Sourav import Menu
            login()
        else:
            exit('\033[1;31m[×] Device Not Support 32bit')
Run()
