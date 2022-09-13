from time import sleep

fireworks = '''
               *    *
   *         '       *       .  *   '     .           * *
                                                               '
       *                *'          *          *        '
   .           *               |               /
               '.         |    |      '       |   '     *
                 \*        \   \             /
       '          \     '* |    |  *        |*                *  *
            *      `.       \   |     *     /    *      '
  .                  \      |   \          /               *
     *'  *     '      \      \   '.       |
        -._            `                  /         *
  ' '      ``._   *                           '          .      '
   *           *\*          * .   .      *
*  '        *    `-._                       .         _..:='        *
             .  '      *       *    *   .       _.:--'
          *           .     .     *         .-'         *
   .               '             . '   *           *         .
  *       ___.-=--..-._     *                '               '
                                  *       *
                *        _.'  .'       `.        '  *             *
     *              *_.-'   .'            `.               *
                   .'                       `._             *  '
   '       '                        .       .  `.     .
       .                      *                  `
               *        '             '                          .
     .                          *        .           *  *
             *        .                                    '
'''

treasure = '''
                                   .-----.   ()()
                                  /       \ .'()
                                  |__...__|/
                                  |_....._|
                                .-'  ___  '-.
                                \_.-`. .`-._/
          __ .--. _              (|\ (_) /|)
       .-;.-"-.-;`_;-,            ( \_=_/ )
     .(_( `)-;___),-;_),          _(_   _)_
    (.( `\.-._)-.(   ). )       /` ||'-'|| `\
  ,(_`'--;.__\  _).;--'`_)  _  /_/ (_>o<_) \_\
 // )`--..__ ``` _( o )'(';,)\_//| || : || |\\
 \;'        `````  `\\   '.\\--' |`"""""""`|//
 /                   ':.___//     \___,___/\_(
|                      '---'|      |__|__|
;      This threasure is yours now ;""|"";
 \                         /       [] | []
  '.                     .'      .'  / \  '.
 jgs'-,.__         __.,-'        `--'   `--'
     (___/`````````\___)
'''

castle = '''
   /\                                                        /\
  |  |                                                      |  |
 /----\              Welcome to Treasure Castle            /----\
[______]             Where Brave Knights Tremble          [______]
 |    |         _____                        _____         |    |
 |[]  |        [     ]                      [     ]        |  []|
 |    |       [_______][ ][ ][ ][][ ][ ][ ][_______]       |    |
 |    [ ][ ][ ]|     |  ,----------------,  |     |[ ][ ][ ]    |
 |             |     |/'    ____..____    '\|     |             |
  \  []        |     |    /'    ||    '\    |     |        []  /
   |      []   |     |   |o     ||     o|   |     |  []       |
   |           |  _  |   |     _||_     |   |  _  |           |
   |   []      | (_) |   |    (_||_)    |   | (_) |       []  |
   |           |     |   |     (||)     |   |     |           |
   |           |     |   |      ||      |   |     |           |
 /''           |     |   |o     ||     o|   |     |           ''\
[_____________[_______]--'------''------'--[_______]_____________]
'''

lamp = '''
         |
 \     _____     /
     /       \
    (         )
-   ( ))))))) )   -
     \ \   / /
      \|___|/
  /    |___|    \
       |___| prs
       |___|
       '''

girlwithknife = '''
              ___
            ,'/|\`.
           :,',^.`.:
           |,'_ _`.|
           |:`*)*';|
           ;|\ _ /|:
        ,-(||.)-(.||)-.
       |'  \|(\ /)|/  `|
       `:. (  `|'  ) .;'
        | : \ ,^. / : |
       ,'`'\-`.._/_/; |
       `:=..-...______;_
       \`\ \'`. .-'\`: /
       ;' \ \/|  \_,\ `:
      /  / \ \;   \  \ .\
     / //  _) `.'--`-----,
    /  /  `-'-.)____...-' \
   / ,(    ;    |  .    ) \\
  //   `-./     |   \.-'    \
 /   /     ``---'-''  \  .   \
(   ,   ,     |     \  `  `   )
 `./      ,   ' .   .     \_.'
    `-._ /    . |    \ _.''
        ``-.._|___..-''
             |.'//
             |'::
             |=||
            ,'.|`._
           '--^'^--` a girl with a knife'''

print(castle)
sleep(0.5)

print("Your mission is to find the treasure...")
sleep(0.5)

print("You open the heavy rusty doors of the castle.")
sleep(0.5)

print("You are in the hallway and looking for the light switch.\n")

sleep(1.5)

print(lamp)

sleep(1.5)
print("There are 2 doors in the hallway and 2 doors to some rooms...")

print("Where is this adventurer going to? ")

up = input("Go up the stairs [up], enter room 1 [1] or room 2 [2]\n")

if up.lower() != "up":
    print(f"You entered room {up} and an ork cut of your head.")
    exit(1)
    
print("You walk up the noisy stairs. \n")
sleep(1.5)

print("When entering the first floor there are 3 doors. Which one do you like to enter?\n")
sleep(1.5)

door = input("door [1], door [2], door[3]\n")

if door == "1":
    print("You enter door 1")
    sleep(2)
    print(girlwithknife)
    sleep(2)
    print("A girl with a knife awaits you. You woke her up and now she is mad.")
    sleep(1)
    if(input("Do you [run] or [hide]") == "run"):
        print("You can run, but there is nowhere to hide.")
        sleep(2)
        print("She cuts your throat and you die.")
        exit(1)
    else:
        print("You hide but she found you. You died.")
elif door == "2":
    print("You enter door 2")
    sleep(2)
    print(treasure)
    sleep(2)
    print("You won this game.")
    print(fireworks)
    
else:
    print("You open the door and walk in. Unfortunately there is no floor.")
    sleep(1.5)
    print("You fall into the basement.")
    sleep(1.5)
    print("There is nothing you can do now.")
    sleep(1.5)
    print("You died.")
    exit(0)
    