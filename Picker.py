__author__ = 'PaleToys'

import time
global gold
global Morty
Morty = 0
gold =  0






def start():
    print("hellow and welcome!")
    name = input("What's your name:")


    if name == "Rick":
        print("wubba lubba dub dub")
    if name == "rick":
        print("wubba lubba dub dub")


    print( "\nwelcome, " + name + "!")
    print ("the objective of this game is to collect Mortys.")
    print ("After collecting the Mortys you sell them. ")


    choice = input("\nDo you want to play Y/N?")
    choice.upper()
    if choice == "Y":
        begin()
    if choice == "N":
        end()
        print ("Okay, bye.....")



def begin():
    global Morty
    print( "And awaaaaay we go.")
    pick = input("Do you want to pick Morty?")
    pick.upper()
    if pick == "Y":
        time.sleep(1)
        print("You pick a Morty.")
        Morty= Morty + 1
        print ("You currently have, " + str(Morty) + " Morty")
        begin()
    if pick == "N":
        sell = input("Do you want to sell your Morty y/n?")
        sell.upper()
        if sell  == "Y":
            global gold
            global Morty
            print("You currently have," + str(Morty) + " Morty")
            print(" You've have sodld your Morty")
            gold = Morty * 10;
            Morty = 0;



def end():
    print(":;'';;;;;;;;;;;;;;;;;'+++++++++++++++++';;;;;;::';;''';:...............';;;,,,,,,,,,,,,,,,,,,,,,,,,,,,::::::::,.,,,:::::::.,,....,,,,,,,,,,.,,,,,,,,.:::;.:,,,:::::::::::::,,,,,,,,,,::::::::::::::,,,.,")
print(";;;;;';:,,......,,,,,;++++++'++++++++++;;;;;;;::,';;;;;;;;;;;;';;:,,...;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,::::::,.,,,,,,:::::::::::::,,,,,,,,,,.,,,,,,,,,,,;::;.,,...:::::::::,,,,,,,,,,,..,,::::::::::...,,,")
print(",,,,.,.....,.,,,,,,,,'++++++'++++++++++;;;;;;;::,.,,,,,,::;''';;;;;;;;;;;',,,,,,,,,,,,,,,,,,,.,,,,,:::::::.,,,,,,.::::::::::::::,,,..,,,,,,,,,,,,,,,.,,;::,:.,,,,.:::::,,,,,.,,.,,,,,,,,,,,,,::::::::,,,")
print(".,,,,......,:,,,,,,:;+++++++''++++++++#+;;';;;;:,.,,,,,,,,,,,,,,,,,,,:;;;:,,,,,,,,,,,,,,,,,,,,,,,::::::::::.,,,,,.::::::::::::,..,,,,,,,,,,,,,,,,,,,,,,,::;..,,,,,::::.,,.,,,.,,,..,,,,,,,,,,,.,,::::,,,")
print(",.,,......;;,,,,,,;;;;++'++++;'+++++++++':::'';:,.,,,,,,,,,,,,,,,,,,..;;;,,,,,,,,,,,,.,,,,,,,,,,,::::::::::::,,,.::::::::::::,.,,,,,,,,,,,,,,,,,,,,,.,..;:;,,,,,,.:::.,,.,.,,.,,,,,,,,,,,,,,,,,,,,.,:,,,")
print(",,.,,,,.:;;,,,,,,;;;;;'+;+++++:+++++++++'+::::;:,.,,,,,,,,,,,,,,,.,,,,;;;,,,,,,,,,,,,,,,,,,,,,,,,,..::::::::.,,,:::,:::::,..,.,,,,,,,,,,,,,,,,,,,,,...,.:::;:,,.,:::::..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
print(",,,,,,,;;;,,,,,,;;;;;:;;++++++;++++++++'++'+;:::;.:,,,,,,,,,,,,,,,,,,:;;:,,,,,,,,.,,,,,,.,,,,,,,,,,,,:::::,,,,,.,,,,:::,.,,,,,,,,,,,,,,,,,,,,,,,,,,....,.::::.:::::::,,,,,.,,,,,,,,,,.,,,,,,,,,,,,,,,,,,")
print(",,,,.;;;;,,,,,,;;;;;;;,:++++++;++++++++';;'+'+;:::'.,,,,,,,,,,,,,,,,,;;;,,,,,,,,,,,,,,.,,,,,,,,,,,,,,..,.,,,,,,....,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,.;::;:::::::,,,,,,,,,.,,,,,,.,,,,,,,,,,,,,.,,,,,")
print(",,.;;;;;:,,,,,,;;;;;;;:;+++++++++++++++';;;;;+'+;::',,,,,,,,.,,,,,,,,;;;,,,,,,,,.,,,.,,,,,,,,,,,,,,,,,,,,,,,...,,,,,,,,,,,,,,,,,,,,,,,.,,,,,,,,,,,,.,,.,,;::;:::::::,,,,,,,,.,,,,,,.,,,,,,,,,,,,.,,,,,,,")
print(",:;;;;:;,,,,,,;;;;;;;,;;++++++++++++++#+';;';;;+'+::,,,,,.,,.,,,,,,,,;;;:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,...,,,,,,,,,,,,,,,,,,,,,,...,,,,,,,,,,...,,.,,,.;::;::::::,,,.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
print(";;;;;;;,,,,,,;;;;;;;:,;;+++++++++++++++++#+';;;;'++;:,,,,,.,,,,,,,,,,:;;;,,,,,,,,.,,,,,,,,,,,,,,,,,,,,...,,,,,,,,,,,,,,,,,,,,,,...,,,,,,,,,,,,..,.,.,,..,;:::..,::;::,,,,,,,,,,.,,,,,,,,,,,,,,,.,,,,,,.,")
print(";;;;;;,,:,,;;;;;;;;,,,;;++++++++++++++++++++;+';';++.,,.,,,,,,,,,,,,,,;;;,,.,,,,.,,,,,,,,,,,,,,,,,,,...,,,,,,,,,,,,,,,,,,,,...,,,,,,,,,..,,,,..,.,.,,..,:;::::,,.........,::,,,,,,,,,,,,,,,..,,,,,,,.,,,")
print(";;;;;;,:,;;;;;;;;;,,,,;;++++++:;;''+++++++++';;'+';,,.,,,,,,,,,.:;,,,,;;;:,,,,,,,,,,,,,,,,,,,,,,,,..,,,,,,,,,,,,,,,,,,,,...,,,,,,,,.,.,,..,,,.,,.,,::::::;:::::::::;;;:,......,::,,,,,,.,,,,,,,,,,,.,,,,")
print(";;;;;;;:;;;:;,;;,,,,,,;;++++++'';;::::;'++++';;;;';;,,,,,,,,.:;;;.,,,,;;;::,,,.,,,,,,,,,,,,,,,,,..,,,,,,,,,,,,,,,,,,,...,,,,,,,,,,,.,,.,,,,,,,.,::::::::,:;:,::;;;::::::::;;:......,::,,,,,,,,,,,,,,,,,,")
print(";;;;;;;;;;;;;;,,,,,,,,;;++++++++++++++''+++++;;;;';:'',,,+#+++##:,,,,,,;;;.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,...,,,,,,...,,,,..,,,,,,,,,,,:::::::,:;:;,,,,,,,,,,:;;:::::::;;,......,::,,,,,,,,,,,,,")
print(";;;;;;;;;;;;:,,:,,,,,,;;+++++++++++++++++++++;;;;';:''++''''''''''++:,,:;;':.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,...,,,.,,,,,,,,,,..,,,,,,,,,,,,,,,:,.,,,::::;,,,,,,,,,,,,,,,,;;:::::::;:........::,,,,,,,,")
print(";;;;;;;;;;:,,,:,,,,,,,;;+++++++++++++++++++++;;;;';:++'''''''''''''''+#,;;;':,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..,,,,,,,,,,,,..,.,,,,,,,,,,,,,,,,,,,,,,,:,::;,,,,,,,,,,,,,,,,.,,,,:;;;:::::;;;,......::,,.,")
print(";;;;;:;;:,:::,,,,,,,,,;;+++++++++++++++++++++;;;;'#'''''''''''''''''''''+;;;;:,,,,,,,,,,,,,,,,,,,,,,,,,,,...,,,,,,,,,,.,,,,.,,,,,,,,,,,,,,,,,,,,,,,,:.;:;,,,,,,,,,,,,,,,,,,.,,,,,,,,:;;:::::::;:.,,...::")
print("'+#';;;,,,,,,,,,,,,::,;:++++++++++++++++;;::;''++''''''''''''''''''''''''+;;;;,,,,,,,,,,,,,,,,,,,,,,,,...,.,,,,,.,,,,,,,,,.,,,,,,,,,,,,,,,,,,,,,,,,:,::;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:;+#''''''''''+")
print("'''''+;```........,..,;;++++++++++++++++++++'#+'''''''''''''''''''''''''''+;;;;.:,,,,,,,,,,,,,,,,,,,,..,,,,,,,.,,,,,,,,,,.,,,,,,,,,,,,,,,,,,,,,,,,,:::;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:+''''''''''''''")
print("'''''''+;,,,,,,,......:;+++++++++++++++++++#+''''''''''''''''''''''''''''''#;;;;:;,,,,,,,,,,,,,,,,..,,,,,,,,.,,,,,,,,,,,.,,,,,,,,,,,,,,,,,,,,,,,:.;:;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,+''''''''''''''''")
print("'''''''''#,,,,,,,,,,,,;;++++++++++++++++++#'''''''''''''''''''''''''''''''''+;;;;;,,,,,,,,,,,,.,,.,,,,,,,.,,,,,,,,,,,,,.,,,,,,,,,,,,,,,,,,,,,,,,;::;:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;''''''''''''''''''")
print("''''''''''+:,,,,,,,,,,;;+++++++++++++++++#'''''''''''''''''''''''''''''''''''+;;;;;;:,,,,,.,,,..,,,.,,,,,,,,,,,,,,,,,,.,,,,,,,,,,,,,,,,,,,,,,:,;::;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,''''''''''''''''''''")
print("'''''''''''':,,,,,,,,,;;+++++++++++++++++'''''''''''''''''''''''''''''''''''''+,';;;;::,,,,,.,,,.,,,,..,.....,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:.;::;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,+''''''''''''''''''''")
print("''''''''''''':,,,,,,,,;;++++++++++++++++#'''''''''''''''''''''''''''''''''''''':,,';;;;;,;.,....:::::::::::::,,,,,,.,,,,,,,,,,,,,,,,,,,,,:.;::;:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..''''''''''''''''''''''")
print("'''''''''''''+,,,,,,,,;;+++++++++++++++#''''''''''''''''''''+#+';'#+'''''''''''+,,,,;;;;;;;,:;:::::::::::::::,,,,::::,,,,,,,,,,,,,,,,,:,,;::;:::.:,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,,:''''''''''''''''''''''")
print("''''''''''''''+.,,,,,,;;++++++++++++++#''''''''''''''''''#:..........:#+'''''''+,.,,,,:;;;;;;':,:;;::::::::::,::::::::,,,,,,,,,,,,::.,;:;;;,,,;:;:.:,,,,,,,,,,,,,,,,,,,,,,.,,,,.,'''''''''''''''''''''''")
print("'''''''''''''''+,,,,,,;;+++++++++++++#''''''''''''''''+;.................'+''''',,,,,....;';;;;;;;';,.:;;;::::::::::::,,,,,,,:::.,:;::;;:,,,,,,,;:;.,,,,,,,,,,,,,,,,,,,,,,,,,,,.+'''''''''''''''''''''''")
print("'''''''''''''''';,,,,.;;+####+###+++++''''''''''''''+;.....................+'''',,,....:;;:;;;;;;;;;;;;;;';;:,.,,:;;;:::,,.,:;;;;:;;:,,,,,,,,,,,,:;:;.;,,,,,,,,,.,,,,,,,,,,,,,,;''''''''''''''''''''''''")
print("''''''''''''''''+,,.,'#'''''''''''+##''''''''''''''+........................,+'',....:;;;:::;:;;;::;;;;;;;;;;;;;;;;;;;;;;;;'+###+:,,,,,,,,,,,,,,,,,;:;.,:#++''++#',,,,,,,,,,,,.+''''''''''''''''''''''''")
print("'''''''''''''''''::;+''''''''''''''''''''''''''''+:...........................+'...:;;;;;;:;.;;;;:::::::::;;;;;;;;;::::,'+'''''''''++,,,,,,,,,,,,,.,::#''''''''''''+',,,,,,,,,;'''''''''''''''''''''''''")
print("'''''''''''''''''+'''''''''''''''''#''''''''''''+..............................#,;;;;;;;;:;.;;;;:::::::::::::::::,,,,,;+''''''''''''''#,,,,,,,,,,,,.:+'''''''''''''''+,,.,,,..+'''''''''''''''''''''''''")
print("''''''''''''''''''+''''''''''''''''+'''''''''''+................................:;;:;;;;;;;,;;;;:::::::::::::::::,,,,+'''''''''''''''''';,,,,,,..,,'''''''''''''''''''';,,,,.:''''''''''''''''''''''''''")
print("''''''''''''''''''+'''''''''''''''''''''''''''+..............................,+';;;;;::;;;.;;::::::::::::::::::::::,+'''''''''''''''''''';,,,,....;''''''''''''''''''''';,,,,'''''''''''''''''''''''''''")
print("''''''''''''''''''+'''''''''''''''+''''''''''',..........;'+';,.............+....+;;';;;,:;;;::::::::::::::::::::::#'''''''''''''''''''''':,,,,,,:''''''''''''''''''''''':.,.+''''''''''''''''''''''''''")
print("''''''''''''''''''''''''''''''''''+'''''''''''.................,+..........;....,:+++';;;.;'::::::::::::::::;:::::+'''''''''''''''''''''''+,,,,,,''''''''''''''''''''''''',,,'''''''''''''''''''''''''''")
print("'''''''''''''''''''+''''''''''''''+'''''''''+....................,'................,#''+';;:::::::::::;::::::::::''''''''''''''''''''''''''+,,,,+'''''''''''''''''''''''''+.:'''''''''''''''''''''''''''")
print("'''''''''''''''''''#''''''''''''''+''''''''',.......................,................;''''':::::::::::;:;:::;::::''''''''''''''''''''''''''';,,:'''''''''''''''''''''''''''+;'''''''''''''''''''''''''''")
print("'''''''''''''''''''+''''''''''''''#''''''''+..........................................;''''+::::::::;;:;:;::::::+'''''''''''''''''''''''''''',,+''''''''''''''''''''''''''''+'''''''''''''''''''''''''''")
print("'''''''''''''''''''+''''''''''''''#'''''''':............+..............................+''''+:::;:::;::;+#+++#':'''''''''''''''''''''''''''''+,'''''''''''''''''''''''''''''+'''''''''''''''''''''''''''")
print("''''''''''''''''''''''''''''''''''#'''''''+............+............,,.................:'''''',,::::;'+''''''''+''''''''''''''''''''''''''''''+'''''''''''''''''''''''''''''+'''''''''''''''''''''''''''")
print("''''''''''''''''''''''''''''''''''+''''''''...........,..............'..................+''''':;;:;:#''''''''''+''''''''''''''''''''''''''''''+'''''''''''''''''''''''''''''+'''''''''''''''''''''''''''")
print("'''''''''''''''''''''''''''''''''''''''''',...........'........,:;;';'....';+':.``````.;+'''''++#':+''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''+'''''''''''''''''''''''''''")
print("'''''''''''''''''''+'''''''''''''+'''''''+............,.:+;,``````````;...:``+``````````'''''''+''#'''''''''''+'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''+'''''''''''''''''''''''''''")
print("'''''''''''''''''''+'''''''''''''#'''''''+...........,+```````````````+...,``;``````````'''''''+'+''''''''''''#''''''''''''''''''''''''''''''''+''''''''''''''''''''''''''''+'''''''''''''''''''''''''''")
print("'''''''''''''''''''+'''''''''''''+''''''';...........;```@````````````'...:`````````````''''''''''''''''''''''+''''''''''''''''''''''''''''''''+''''''''''''''''''''''''''''+'''''''''''''''''''''''''''")
print("'''''''''''''''''''#'''''''''''''+''''''',...........;````````````````+...'`````````````+'''''''#'''''''''''''+'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''+'''''''''''''''''''''''''''")
print("'''''''''''''''''''''''''''''''''''''''''............;````````````````'...:`````````````+'''''''+'''''''''''''+''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''+''''''''''''''''''''''''''")
print("''''''''''''''''''':'''''''''''''''''''''............,````````````````,....,```````````:''''''''+'''''''''''''+'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print("''''''''''''''''''+,''''''''''''''''''''+..............``````````````:.....:```````````+''''''''+'''''''''''''+''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''';,''''''''''''''''''''''''''")
print("''''''''''''''''''','''''''''''''+''''''+.............'``````````````:......'`````````'+''''''''+'''''''''''''#'''''''''''''''''''''''''''''''+''''''''''''''''''''''''''''';.''''''''''''''''''''''''''")
print("'''''''''''''''''',,'''''''''''''+''''''+...............````````````'........::`````,:.+''''''''+'''''''''''''+''''''''''''''''''''''''''''''''+'''''''''''''''''''''''''''';.+''''''''''''''''''''''''+")
print("'''''''''''''''''+.,''''''''''''''#'''''+..............;.``````````'.......#...,'++,...+''''''''+''''''''''''''''''''''''''''''''''''''''''''':''''''''''''''''''''''''''''''..'''''''''''''''''''''''';")
print("''''''''''''''''':.,''''''''''''''''''''+..............:.'```````,;.........'..........+''''''''+''''''''''''''+''''''''''''''''''''''''''''''..''''''''''''''''''''''''''':;..+''''''''''''''''''''''',")
print("''''''''''''''''+..:'''''''''''''''#''''+.,'..........:::',+;:;+,............;.........+''''''''+''''''''''''',#'''''''''''''''''''''''''''''+,.+''''''''''''''''''''''''''.;..,'''''''''''''''''''''''.")
print("'''''''''''''''''..;.;'''''''''''''''''''+............::;;..............,....;........,'''''''''''''''''''''';.;'''''''''''''''''''''''''''''.'.,'''''''''''''''''''''''''..:...+''''''''''''''''''''''.")
print("''''''''''''''''...;..+'''''''''''''#'''#.............:,':...............',.:.........,''''''''+.+'''''''''''..;+'''''''''''''''''''''''''''+..,.+'''''''''''''''''''''''+..,...,'''''''''''''''''''''':")
print("'''''''''''''''+...;..''''''''''''''+'''.............,:.',............................;'''''''';.:'''''''''''..;;''''''''''''''''''''''''''+:..:..+''''''''''''''''''''''+...,...+'''''''''''''''''''''+")
print("'''''''''''''''....,..'''''''''''''''+'+.............:;.'.............................+'''''''':.,''''''''''';.,.+''''''''''''''''''''''''','..:...+'''''''''''''''''''''#...;....+'''''''''''''''''''''")
print("'''''''''''''',...,...+'''''''''''''''++.............;:.'.............................+''''''','.''''''''''''',...+''''''''''''''''''''''':.:.,;....,+''''''''''''''''''',+..;.....+''''''''''''''''''''")
print("''''''''''''',....;...'''''''''''''''+.+.............:,.'............................,''''''':.;;,+''''''''+,'++:..'''''''''''''''''''''';.,.:'+.......#'''''''''''''++..#''.,......;'''''''''''''''''''")
print("'''''''''''+......;..+''''''''''''''....:............:,.'............................+'''''+...+.;.+'''''###::.+#....''''''''''''''''''+...#''''+........'#+'''''++'....'.'''#:.......+'''''''''''''''''")
print("''''''''''+.......,:;'+'''''''''+;......,...........;'+.'............................+'''+,...+''+..+''+++++++::.'....,+'''''''''''''+:...,,''''';.....................;..#'''+.........''''''''''''''''")
print("''''''''+........:.......,:;:,...........;,.........,'+.'..............,'+++........'+#'.....:'''''..,+++;++##+#..:......:+++''++#',......:.#''''':........,'++'':....''...+''':..........+'''''''''''''")
print("'''''''..........:'........,:,..........,+',+:.......+#:++...........':.............,........'''''+:..;++'##:;#++;.:.....................;,.;+''''':.....+.........,;+.:,...+'''............,++'''''''''")
print("'''+'...........;.,+..',.......:;......,++#,...........+'+.........+,..............'........+''+'...:.++;#++++++++:'....................+:.,;,''''''+..+.............'.,'....,'##................,:;;:,.")
print("+:.............,.#''#.............+...;++#...'.........+++........................',,:'...,,.........,+#++++++#++++,+.......;'':,......+':..:,,+'''''',...............,,.;.......'......................")
print("...............,..+'...............,'#++#.....'.........,:.......................;......;'.....',....;+++#++;:++++++'+;..':........;,+''',,..;..,++'',.................:..'.......'.............'';:''+'")
print("..............:...,..................#++,......;................................,.........+......;.:'#+++##,':;++#+++''+.............+''+,,::.'.....;...................'''+..:+:..'.........::.........")
print(";............;...:....................##........;..............................,...........'.......++++++#:;:;,,';+++#,...............''',.,.,'#..,;,....................:'';+......'......',...........")
print("..'.........:...;.....................:,.........;............................,,............;......:,++++:;:;:;,:::;++.................+:.,..+''#..;.....................:''+........,:..;,.............")
print("....'.....,,...'.......................;..........+..........................;..............,,.....;;++'';,;:,:#;#'#+#..................',,,,:++...:......................+;:..........,+...............")
print("......'..+.............................,..........;.+.......................+,:..............'....:.#+''::;,,''+++#+++..................,,,.,.:....,......................''...........;................")
print(".......'......'.........................,........'....+,.................,+...,,..................;.''+;;',,++##++++#+...................',,`,:...,........................'..........;.................")
print("........:....,..........................'.......'.......,'++';:,.....,''.......:..............'...:''+;'+,,'''#+#+++++...................,,.',....:........................#.........,..................")
print(".........'...'.................................,................................+.............:.,:''#';:':+,'##+#++.#+....................:.;'....;....................,...+.........'..................")
print(".............,...........................,.....;.................................:.........,....,';.#;';'+:::#+#++'.#+....................'++:....'....;................,..:...:........................")
print("..........'.:....:.......................'....;..................................:.........,...;';..+:+#;'.#+'#+#,..#+....................:'',.,..'....;................:..,...'....'...................")
print("..........,.;....;...................,...:....,...................................'........,...'',..;;+++;.#++++.'..#+,....................''..,..;....;................;...,..;....:...................")
print("...........:,....;...................,...,...+....................................,........,..;';...:'++++#+++:.;...#+,................,...+'..,..;....:................;...:..,........................")
print("...........'.....;...................,.............................................'.......,.++,'..,:+++++++#..,,...#+:....................#:..,..;....,................;...;......,....................")
print("...........:.....:...................,....,.'......................................,.......,:'''';+;;,#++#'....+....#+:....................;:..,..'.....................;...;...,..;....................")
print(".................,...................,....,.:.......................................+......,,+#.;..:'.:.......+;....++:....................+'..,..'.....,...............:...:...:..;....................")
print("............,....,...................,....::................................................++,.;..:',,......:.:....++:....................''.,,..;.....,...............,;';;'''...:....................")
print("............:...,....................,...:.'.................................;.......'......;...'.,;;;.......,......'+:....................;'.:,..,;:;'+....................:..:...,....................")
print("............'',.,....................,.,.:.,.................................;........;.....:...;.+;'.......'.,.....;+:...................,#+.,,...;...:................,...;,.,..........;.............")
print("....,.......;..,'....................,...:;.........:........................;........,.....:...;.'+.......'..:.....;+:....................;#..,...:...:.................,..;:....,.......:.............")
print("............;..;:....................,,..,;........,.........................;.........'....,...;.'',.....:....:+:..;+:....................:#..,...:...:.................,..;:....,.......:.............")
print("............;..;'....................,,..,.........;.........................;..........:...,,..:;++,.....,...,....::+:....................,#..,...:...:.................:..;:....:.......,.............")
print("...:........;...+....................,:..'.........'.........................:..........:...,:..;.;;.....;....:.....:+:.....................#:.,...:...:.................;..;,.,..:.......,.............")
print("...;........;...'....................:,..;.........,.........................,........;+;'..,,.,,.......+.....'.....;+:.....................#'.,...:...:.................'..;,.:..:.....................")
print("...;........;.;.;....................:............,.........................,;......;,..,,+.:,.,.......':.....'...:.;+:.................,...,'.,...:...:.................'..',.:..:........,............")
print("...;........;.'.;....................:..:.........+.........................,:.....'.....+:.:,:.......:+:.....:...',;+:.....................:'.,...:...:.................'..+..;..,........,............")
print("...:........;.;.:....................:..+.........;.........................:.'...;.......+.::.......,,+:.........;,'+,....................,;;.,...:...:.................;..+..'..,........,............")
print("...:........;.;.,....................:..;...................................;..,.,;.......'.;........:.+,.........,,'+,....................;:..,...:...;.................:..#..'...........,............")
print("...,........;.:.,....................:...........:..........................;..'.';........;........'..+,....,.....,'+,....................+,,,....:...;.................:..#..;...,.......,............")
print("...,........:.:......................;.,.........'..........................'...+'.'......;........+:..+,....,....,,++,....................:..',...;...;.................,..'..:...:.......,............")
print("............,.,......................;.;.........;..........................'....+.:.....;........',:..+,....,....,,++,.......................#....;...;.................,.,:..,...;.....,;.............")
print("..............,......................;.'....................................'....;..+............'..:..+,.........,:++....................,...+#+':;...;...................,'..++++'+.....;.............")
print("...,.......,..,......................;.:........:...........................'........;..........;:..:..+:.........,,++....................;..:`;'++;...:...................:'..+++'++.....;.............")
print("...;;';....'..,,.....................;,.........'...........................'........,.........:,:..:..+:.........,:#+....................;....''+':...,...................;:..++'#++.....;.............")
print("...;.....'....,,.....................;,+........;...........................'.........'.......:,':..:..+;.........,:++....................+''''+''+,.......................'...#+'+++.....;.............")
print("...;.....+....++.....................;;;.+;.....:...........................;..........'.....:.:+:..;..+;.........#;+#....................:,,,,;+++........................+#.,+'+'++.....;.............")
print("...:.....#...,++.....................;+'....,;++,...........................;...........,...:..;;;,.'+++######....+++#...................,,,,,,;'++...,...................,;+;:'++;++.....;.............")
print("...,.....#...,++.....................+.+......;.............................;...........,+'''..:;;:,'+++#'++++....++++...................:,,,,,:+++...;...................:;+':#'#'++.....;.............")
print("...,.....#...:+#.....................;.'......'.............................;...............::.,#;;::+++#'++++....++++...................',,,,,:+++...'...................:'+++'+','+.....;.............")
print(".........+...:++.....................;`:......:.............................;...............,.,,+;';;+'+#+','+,...++++..................,;,,,,,,+++...'...................;+''+'+:,'+.....:.............")
print("..,......;...;++.....................:.,......,.............................##++;:;:,,,;+#++'..,+++#,+++#+','+,...+++'..................,:,,,,,,+++...;...................;#'''++,,;+.....:.............")
print("..,.....,+...;'+.....................''......,,.............................#++++''''''''+'+::';'+'+,#+##+;,'+:...+++'..................,;;::::;+++...,...................;+++''+;'++.....:.............")
print("..:.....:;...'+'.....................:;......'..............................#+''++++'''''+++::'+'+'+,#'##':,'+:...+++'..................:,,,,,,,+++...,...................:+'''+',,:+.....:.............")
print("..;.....;;...++'.....................:'......'..............................#+''''++++'''+'#;;'#''++'++##''''+:...+++;..................',,,,,,,+'+.:.'...................,+''+',,,:+.....;.............")
print("..;.....';...++'.....................::......:..............................#'''''+,;+'''''+;;;;'+'+:++##+,,'+;...#:+;..................;,,,,,,,+''.:.++#+;,....,,,,:'+++;,++''+,,,,+.....;.............")
print("..;.....+:...+''.....................,,.....................................#'''''+,;++''''+,,,,+++++#+##+,,'+;...#`+;..................:,,,,,,,+';.,.'+'++''+'''''''++'+;;+++'+,,,,+.....;.............")
print("..;.....+....''+....................,,,.....,,..............................#+''''+,;#+''+'',,,,#'+'##+##+,,'+;...+`+;..................:,,,,,,,++:,.::'''''+'++''''+'''+;'++'+',,,,+.....;.............")
print("..;.....+..:.;'+....................;,,.....:,..............................#+''''+,;#+'''+;,,,,;+''+++#++,,'#;...#,+;..................:,,,,,,,++;;;:;''''''+++''''''''+;'''+':,,,,+.....;.............")
print("..;.....#..:.:''#+,,,...........,;+++,,.....::..............................#+''+++,;#+''++;,,,,,++++++#+#,,'+,...+,+'.................,,,,,,,,,++';::#'''''++;'':+''''''':'+'':,,,,+.....;.............")
print("..;.....+....,+++++'''++++++#++''+'++,,.....::..............................#+''+++,;#+'''+:,,,,:++++++#++,,'+..:.',+#;,..........,'+++',,,,,,,,+'+;:,+'''''++,,,,++''''';,++'';,,,,#.....;.............")
print("..;.....+.....+'++''+''+''+'+''''+''+,,.....;:..............................#''''+',;#''+'+,,,,,:'+'+#+#++,,'+..;.,,+#'''+++++'''''+''+',,,,,,,,+'+;:'++'''''+,,,,++''''';,+''';,,,,#.....:.............")
print("..;.....+,.,,,++'+''''''''+''''''''++,,.....;:..............................#+'''+',;#''+'+,,,,,;+++++'##+,,'+......+#'+'+''''''''''''+;,,,,,,,,++'++++''''''',,,,++'''++;,+'++:,,,,+.....,.............")
print("..;.....'+..,'+''+'+'''''++++''''''++,,.....':..............................#+'''';,+++'''+,,,,,'''+'+'##+,,''.:..':+#'''''''''''''''++;,,,,,,,,+''+'++'''''+;,,,,++''''';,+''+;,,,,'...................")
print("..;.....'':.,++''#++''''+','++'''+'++,......':..............................#+'''';,++''''+,,,,,+''';+'##+,,''.'';+;+#'''''+###++''''++:,,,,,,,,+'':`,++''''+,,,,,++''''+;,+'''',,,,:...................")
print("++#+++++###++############@+##########+++++++#+++++++++++++++++++++++++++++++@#####++#######+++++####+##@@#++##+####+#@######+++########+++++++++###+'+#######+++++########+#####++++++++++++++++++++++++")


start()