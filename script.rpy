# The script of the game goes in this file.

default isInvitedStrawberry = False
default isInvitedWatermelon = False
default isInvitedLemon = False

default VisitedUni = False
default VisitedCircus = False
default VisitedGov = False

init:
    image stage = Movie(size = (1920, 1080), play = "images/performance.webm", loop = True)


style mytextbutton:
    color "#ffffff"
    hover_color gui.hover_color


screen skipButton():
    textbutton "Since the creator is too dumb to figure out how to make a proper skip button,\n                just click the screen anytime during the cutscene to skip it \n                         (the mouse pointer will not show but that's okay)\n                                     Click this text to move forward.":
        text_style "mytextbutton"
        xalign 0.5
        yalign 0.5
        action Return(0)
        # The button is sensitive only if there is no dialogue screen
        #sensitive (not renpy.get_screen("say"))

#screen test():
#    vbox:

        # # Using the style:
        # textbutton "Hello":
        #     text_style "mytextbutton"
        #     action NullAction()


        # # Formatting directly without the style:
        # textbutton "Hello":
        #     text_color "#f00"
        #     text_hover_color "#ff0"
        #     action NullAction()

# Skip button


transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])

    bar value time range timer_range xalign 0.5 yalign 0.6 xmaximum 300 at alpha_dissolve




label splashscreen:
    scene black with Pause(1)
    show text "{color=#FFFFFF}Hi!!! Welcome to my game!{/color}" with dissolve 
    with Pause(1.5)
    show text "{color=#FFFFFF}It is sorta scuff right now...{/color}" with dissolve 
    with Pause(2)
    show text "{color=#FFFFFF}But hopefully you are here for a reason :D{/color}" with dissolve 
    with Pause(2)
    show text "{color=#FFFFFF}Enjoy!{/color}" with dissolve 
    with Pause(1)
    hide text with dissolve
    with Pause(2)
    return

# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"


    scene black
    show god:
        zoom 1.3



    "God" "Hello there, human. Are you wondering why you are here?"
    "God" "Well, that's a very good question."
    "God" "Anyways... "
    scene bg void 
    "You get chucked into the void"
    "God" "Have fun :D"
    menu:
        "What in the world was that?":
            menu:
                "I'm just trying to date fruit.":
                    menu:
                        "God isn't a fruit.":
                            menu:
                                "Oh wow choices on the screen. Good job creator! How original!":
                                    menu:
                                        "To be a banana, or not to be a banana. That is the question.":
                                            menu: 
                                                "BANANAS RULE":
                                                    $ isBanana = True
                                                    jump choice1Banana
                                                "I want to remain a human":
                                                    $ isBanana = False
                                                    jump choice2Human

    label choice1Banana:
        show mirror at center:
            zoom 1.2
            yalign 0.0
        show banana
        "HWAT!?!? THATS ME!?!? Damn, I look so much better as a banana."
        jump continue1
    label choice2Human:
        "God" "Ok, a boring human you shall stay"
        "Hey! I'm very interesting for your information!"
        "God" "Sure sure whatever you say, boring human" 
        "*sigh*" 
        jump continue1

    label continue1:
        scene bg void
        "*continue falling*"
        menu:
            "AHHHHHHHHHHHHHHH!!!":
                jump enterStory

    label enterStory: 
        scene bg town                                           
        "CRASH!!!!"
        "You have fallen into the middle of the street and there are fruit looking at you"
        if isBanana: 
            "Random fruit numero uno" "OH MY GAWD A NEW FRUIT HAS ARRIVED!"
            "Random fruit numero dos" "Wow a banana!"
            "Random fruit numero tres" "I can't wait to talk to the banana!"
            scene bg town2
            show orange happy with zoomin
        else:
            "Random fruit numero uno" "OH MY GAWD SOMETHING DROPPED!"
            "Random fruit numero dos" "Wait, why is it a human?"
            "Random fruit numero tres" "Wow, is it real!?"
            show bg town2
            show orange happy with zoomin
            "Random fruit numero quatre (sorry, creator doesnt know spanish)" "Hey, let us not forget our education. Fruit or not, we must help this new individual in town."
        #orange now approaches
        o "Hi, I'm Orange. What's your name?"
        $ yn = renpy.input("What is your name?", "Banana", length=15, exclude=" 0123456789+=,.?!<>{}[]").strip() or "Banana"
        o "Hello [yn]! Nice to meet you!"
        o "I'm sure you are very disoriented, but worry not!"
        o "I can give you a tour!"
        menu:
            "Yes please! Thank you!":
                jump tourYes
            "I just want to go home :(":
                show orange upset
                o "Oh. Umm, sorry, but I don't think we can get you a home right now. However, we can try to figure something out."
                o "Would you like to do the tour or would you like to go somewhere to rest."
                menu:
                    "Oh. I would rather do the tour then.":
                        show orange happy
                        jump tourYes
                    "I'd like to rest and process everything.":
                        jump choiceHome

        label tourYes:
            o "Great! This town is called \"Fruit Bowl\"."
            o "Here we have roads, buildings, lights..."
            o "Well, everything a normal town would have."
            show sunnydale with dissolve:
                xalign 0.1 yalign 0.3
                xzoom 0.5 yzoom 0.5
            o "A notable landmarks is the Sunnydale University. In it we have some of our greatest minds and I believe I can talk to the principal and get you inside for a campus tour."
            hide sunnydale with dissolve
            show orange normal
            o "Oh, there are also the government buildings."
            o "I have permission to go inside, but there are probably more interesting things to explore." 
            show orange happy
            o "Now, there's also..."
            #cue the clown music
            show watermelon extra happy with moveinright 
            hide watermelon extra happy with moveoutleft
            show flier with easeintop
            #Watermelon rolling around in the back and a flier for the performance lands in your face
            o "Oops! Let me help you get that off your face."
            pause 0.5
            hide flier
            pause 1.5
            o "OH HOW COULD I FORGET! SunRipe circus has a performance today!"
            o "There are a lot more things in this town, but we can get to them all eventually." 
            o "So, where would you like to go first?"
            label choicesBeginning:
                menu:
                    "Lets go visit the university!":
                        jump choiceUni
                    "The circus sounds fun. Let's go there first!":
                        jump choiceCircus
                    "I LOVE THE GOVERNMENT! I WANT TO VISIT THE PRESIDENT!":
                        show orange normal
                        "God" "Orange is very disappointed in you"
                        jump choiceGov
                    "Hmm... I would like to just walk around and go home. Wait, do I even have a house here?":
                        o "Are you sure you don't want to go anywhere else? We won't be visiting any more locations once you go home."
                        menu:
                            "Yes. I am certain.":
                                jump choiceHome
                            "No. Let me choose again.":
                                o "No problem."
                                jump choicesBeginning
        
        
        
        label choiceUni: #meet Strawberry
            o "Good choice! Let's go!"
            $ VisitedUni = True
            scene bg void
            pause 0.5
            scene bg uni
            show orange happy
            o "Here we are! This is Sunnydale University."
            o "If you have any questions, please don't direct them at me. I don't actually know how the university works. I only know where things are."
            #garden library background
            show bg library
            o "Here is the garden library."
            o "As you can see, this is a popular spot for students to study."
            o "You can just use the shovel to dig a hole into the ground and curl up in there with a book. It's fun. Trust me."
            #Strawberry shows up 
            show orange happy at left
            show strawberry happy at right
            "A student" "Oh hey Orange! Are you giving a tour again?"
            o "Yeah! [yn], this is Strawberry and Strawberry, this is [yn]. Strawberry is studying fruit anatomy."
            s "Hi [yn]. It's a pleasure to meet you."
            menu:
                "WOWWWW THAT'S SO COOL! What's fruit anatomy like?":
                    jump choicewow
                "Orange, save me. Strawberry is intimidating.":
                    jump choicescary   
                "I love you Strawberry. Marry me.":
                    show strawberry shocked
                    #strawberry is shocked or flustered
                    s "Oh... ummm... thank you?"
                    menu:
                        "Sorry, that was supposed to be a joke.":
                            show strawberry happy
                            s "Oh, haha! Sorry, I didn't realize." 
                            s "You seem nice. I really need to get going though."
                            s "If you would like, you can come visit me later! Orange should be able to show you there."
                            menu:
                                "Great! I'll come by later!":
                                    s "Looking forward to it!"
                            $ isInvitedStrawberry = True
                            jump leavingUni
                        "Marry me.":
                            s "Oh."
                            o "Umm, let's not bother Strawberry anymore. Why don't we continue the tour."
                            menu:
                                "Awww :( ok.":
                                    show strawberry happy
                                    s "Bye!"
                                    jump leavingUni
            label choicewow:
                show strawberry shy
                s "Thanks, but it's nothing too interesting. It is just learning about what is going on inside each fruit."
                menu: 
                    "Shut up, that's super cool.":
                        jump continue2
                    "Oh.":
                        jump continue2
                label continue2:
                    show strawberry happy
                    s "Anyways, don't let me interrupt your tour. I'll be around tomorrow as well so you can visit me if you would like." 
                    $ isInvitedStrawberry = True
                    s "Bye!"
                    menu:
                        "WAIT! DON'T GO!":
                            s "Haha. Sorry, I really should get to my next class. Come visit me later though!"
                            jump leavingUni
                        "Bye!":
                            jump leavingUni
                        "Oh.":
                            jump leavingUni
            label choicescary:
                show strawberry upset
                o "Don't worry. Strawberry is very nice, much nicer that most of the others on this campus."
                s "Well... Don't let me take up too much of your time then."
                show strawberry happy
                s "Bye."
                menu:
                    "I love you, Orange.":
                        jump leavingUni
                    "Thank you, Orange.":
                        jump leavingUni
                    "Bye Strawberry.":
                        s "Bye! And feel free to come visit me later if you want!"
                        $ isInvitedStrawberry = True
                        jump leavingUni

            label leavingUni:
                hide strawberry happy
                show orange happy at center
                o "Cool! Let's continue!"
                o "Where would you like to go?"
                if VisitedCircus == False and VisitedGov == False:
                    menu:
                        "CIRCUS! CIRCUS! CIRCUS!":
                            jump choiceCircus

                        "GOVERNMENT!!!!! I'LL BECOME THE NEXT WORLD LEADER!":
                            show orange normal 
                            "God" "Orange is concerned for your sanity"
                            jump choiceGov

                        "I want to go home now, or to whatever is supposed to be my home here.":
                            jump choiceHome
                elif VisitedCircus == False and VisitedGov == True:
                    menu:
                        "CIRCUS! CIRCUS! CIRCUS!":
                            jump choiceCircus
                        "I want to go home now, or to whatever is supposed to be my home here.":
                            jump choiceHome
                elif VisitedGov == False and VisitedCircus == True:
                    menu:
                        "GOVERNMENT!!!!! I'LL BECOME THE NEXT WORLD LEADER!":
                            show orange normal
                            "God" "Orange is concerned for your sanity"
                            jump choiceGov

                        "I want to go home now, or to whatever is supposed to be my home here.":
                            jump choiceHome
                elif VisitedGov == True and VisitedCircus == True:
                    menu:
                        "I want to go home now, or to whatever is supposed to be my home here.":
                            jump choiceHome


        label choiceCircus: #meet watermelon
            $ VisitedCircus = True
            o "Let's go then! I'm so excited. Their productions have always amazed me."
            #display Gods void
            scene bg void
            #change scene to circus and start playing the music
            pause 1
            scene bg outside_circus
            show orange happy
            o "You see that striped tent? They perform in there."
            o "Seeing as their performance is in a week, they might be rehearsing inside."
            o "Usually rehearsals are closed off to the public but I may be able to talk to the director and get you inside for a sneak peak."
            o "Give me a moment. Just wait for me right here."
            menu: 
                "Ok! Good luck!":
                    hide orange happy with moveoutleft
                    #orange disappears then reappears
                    pause 0.5
                    show orange happy with moveinright
                    o "Ok, so just for you, the director has allowed me to introduce you to the troupe."
                    menu: 
                        "YIPPIE! LETS GO IN!":
                            o "I'm glad I was able to you happy."
                            o "I love your smile."
                            jump continue3
                        "Wow Orange, you must know a lot of people.":
                            o "Well, I guess you could say that..."
                            o "Lets go in now."
                            jump continue3
            label continue3:
                #change scene to inside tent
                scene bg circus1
                show orange happy
                o "Now, may I introduce you to the most magical part of Fruit Bowl, SunRipe circus!"
                menu:
                    "It seems everyone is really busy. Are you sure we aren't interupting?":
                        show orange normal
                        o "Well... actually, yes. The director did say to try to not get in the way of practice."
                show orange happy
                o "But worry not! There are a few members that are on break right now that we can go talk to."
                o "Come this way."
                scene bg circus2 with pushleft
                show orange happy:
                    xalign 1.0
                    yalign 1.0
                show watermelon extra happy:
                    xalign 0.0
                    yalign 1.0
                show pineapple:
                    xalign 0.25
                    yalign 1.0
                show mango:
                    xalign 0.5
                    yalign 1.0
                o "Here is Watermelon, Pineapple, and Mango."
                menu: 
                    "Hello! I am [yn]":
                        w "HELLO! I AM WATERMELON AND THESE ARE MY TEAMMATES!"
                        "Pineapple and Mango" "Hello!"
                w "I HOPE YOU WILL SHOW UP ON PERFORMANCE DAY!"
                $ isInvitedWatermelon = True
                w "I PROMISE YOU WON'T BE DISAPPOINTED!!!"
                w "SO PLEASE COME AND SUPPORT US!!!!!!"
                menu:
                    "Wow, so enthusiastic.":
                        show watermelon happy
                        w "I LOVE MY WORK!" 
                        w "HEY! ORANGE! COME AROUND AND VISIT MORE!"
                        w "DO YOU WANT ME TO SHOW YOU AROUND?"
                        menu:
                            "Sure!":
                                show watermelon extra happy
                                w "GREAT! HAVE FUN ORANGE! WE WILL BE BACK IN A BIT!"
                                jump watermelonTour
                            "No thanks. I would rather not ditch Orange.":
                                w "HAHA! A LOYAL FRIEND YOU GOT THERE ORANGE! I APPROVE! GO ON THEN YOU TWO! HAVE FUN VISITING THE SUNRIPE CIRCUS!!!"
                                jump orangeTour
                    "For sure! I will make time for it.":
                        w "GREAT!!"
                        w "OH WAIT YOU WERE HERE FOR A TOUR RIGHT?"
                        w "HEY ORANGE, YOU DON'T MIND ME TAKING OVER YOUR JOB DO YOU?"
                        w "HEHEHEHE YEAH OF COURSE YOU DON'T!"
                        w "COME ON, LETS GO! I'LL SHOW YOU THE BACKSTAGE! OOH MAYBE I CAN EVEN GET SOME EQUIPMENT FOR YOU TO TRY OUT!!"
                        menu:
                            "No. Get away. You are so strange. Orange, can we go?":
                                show watermelon happy
                                show orange normal
                                o "Oh. Are you sure? We haven't looked around yet."
                                menu:
                                    "Yes. I don't want to be in this tent.":
                                        o "Oh, um, alright then." 
                                        show orange happy
                                        o "Bye everyone and, Watermelon, thank you for offering. I'll take you up on that offer next time."
                                        w "HAHA SURE! MAKE SURE TO BRING MORE FRIENDS NEXT TIME!"
                                        $ isInvitedWatermelon = False
                                        jump leavingCircus
                                    "Actually, no. Orange, can you give me a tour?":
                                        show orange happy
                                        o "Yeah, sure! Sorry Watermelon. I'll have to take you up on that offer next time."
                                        w "NO PROBLEM, MY FRIEND! HAVE FUN"
                                        jump OrangeTour
                            "Oh, umm... maybe later? I'm pretty sure Orange has some things planned for me, don't you Orange?":
                                show orange happy
                                o "Oh yeah. I was planning to bring [yn] around to watch the rehearsal."
                                w "OH NO PROBLEM THEN! HAVE FUN!"
                                jump orangeTour
                            "Oh ok! Have fun Orange! I will be back in a bit.":
                                o "Bye! You have fun too! Watermelon is a great tour guide." 
                                show watermelon extra happy
                                w "THANKS FOR VOUCHING FOR ME, FRIEND! OK TIME TO VISIT THE BACKSTAGE!!!"
                                jump watermelonTour
            label watermelonTour:
                #scene change to backstage
                scene bg backstage
                show watermelon extra happy
                show dragonfruit at left
                show durian at right
                w "THIS IS THE BACKSTAGE WHERE WE HANG OUT OR WHERE WE WAIT FOR OUR TURN ON THE STAGE."
                w "WE ALSO SOMETIMES USE IT AS A CHANGING ROOM OR TEMPORARY STORAGE SPACE."
                "Random circus member" "Hi!"
                "Another random circus member" "Hello!"
                menu:
                    "Hi!":
                        jump continue4
                    "Hello!":
                        jump continue4
                label continue4:
                    w "HEY GUYS! I'M GIVING [yn] A TOUR RIGHT NOW! I WILL BE BACK SOON!"
                    w "ALRIGHT! NEXT PLACE! THE STAGE"
                    #change scene to stage
                    scene bg stage
                    show stage
                    show watermelon extra happy
                    w "RIGHT NOW ITS REHEARSALS! NORMALLY, THESE SEATS WOULD BE COMPLETELY FILLED!"
                    w "ALRIGHT NEXT UP, I GOT YOU A UNICYCLE! WANNA TRY?"
                    menu:
                        "Sure!":
                            w "YAYYYYYYY!"
                            w "OKAY, SO YOU JUST GET ON!"
                            w "THEN, JUST GO!"
                            w "SEE, NOT SO HARD!"
                            w "YOUR TURN!!!"
                            $ timer_range = 2.5
                            $ timer_jump = 'unicycleFail'
                            $ time = 2
                            show screen countdown
                            menu:
                                "Quick! Pedal!"

                                "Click me!!":
                                    hide screen countdown
                                    jump unicycleSuccess
                            label unicycleSuccess:
                                "You balance on the unicycle and manage to move around."
                                w "WOW!! YOU'RE A NATURAL! EVER CONSIDERED JOINING THE CIRCUS?"
                                menu:
                                    "Haha, thanks!":
                                        w "I LOVE THE UNICYCLE! COME BY SOMETIME AND WE CAN HAVE A RACE!"
                                jump continue8
                            label unicycleFail:
                                "You try it and fall immediately."
                                w "OH, WELL, THAT'S FINE! YOU JUST NEED SOME PRACTICE!"
                                w "TRUST ME, IT IS SUPER FUN ONCE YOU GET THE HANG OF IT!"
                                jump continue8
                            label continue8:
                                w "ANYWAYS, I SHOULD GET YOU BACK TO ORANGE!"
                                $ isInvitedWatermelon = True
                                jump leavingCircus
                        "No thanks.":
                            show watermelon happy
                            w "AWWWW THAT SUCKS :( WELL THEN, THAT CONCLUDES THE TOUR! TIME TO GET BACK TO ORANGE!"
                            #change scene to Orange
                            scene bg circus1
                            show orange happy at right
                            show watermelon extra happy at left
                            o "Hey! You guys are back!"
                            o "How was it?"
                            menu:
                                "FUNNN!!":
                                    o "That's great!"
                                    o "Thank you, Watermelon!"
                                    w "YOU ARE VERY WELCOME!!!"
                                    hide watermelon extra happy
                                    jump leavingCircus
                                "I was actually hoping for a little bit more...":
                                    o "Oh. Don't worry. We can come back again later, right Watermelon?"
                                    w "YES YES OF COURSE! COME BACK AND WATCH OUR SHOW!"
                                    $ isInvitedWatermelon = True
                                    w "BYEEEE!"
                                    hide watermelon extra happy
                                    jump leavingCircus


            label orangeTour:
                o "Alright, lets get going."
                o "Unfortunately, there's a lot of places that are off bounds for me so I won't be able to show you the full circus."
                o "However, I was thinking of watching part of the rehearsals with you. What do you say?"
                menu:
                    "Sounds like fun!":
                        o "Great! I'm so excited!"
                        scene bg stage
                        show stage
                        show orange happy
                        #scene change to rehearsal
                        o "Here we are! Oh look, they're up there, hanging from the rings on the ceiling!"
                        scene black
                        call screen skipButton
                        pause 1.0
                        $ renpy.movie_cutscene("images/performance.webm", loops = 0) 
                        scene bg black with Dissolve(1)
                        pause 0.5
                        "Time flies and you watch the entire rehearsal with Orange."
                        pause 0.5
                        scene bg stage with Dissolve(1)
                        show orange normal
                        o "Oh oops. We accidentally stayed for longer than I expected to."
                        show orange happy 
                        o "Don't worry though. We still have time to visit other places."
                        jump leavingCircus
                    "I would prefer to look around.":
                        o "Oh, that's fine too."
                        show bg stage
                        o "So here is the stage where they do rehearsals and performances."
                        o "In the left and right corners of the stage, you can see the doors that lead to the backstage."
                        o "The circus often draws in food trucks that park outside the tent." 
                        o "Sometimes, if the circus wants to, they set up their own food truck close to the entrance over there."
                        o "Anddd thats basically everything, I think."
                        jump leavingCircus

            label leavingCircus:
                scene bg outside_circus with dissolve 
                show orange happy at center with dissolve
                o "So, did you like the circus?"
                menu:
                    "YES! IT WAS SO MUCH FUN!":
                        o "Haha, I love this place too!"
                        jump continue5
                    "It was definitely interesting...":
                        show orange normal
                        o "Hmm, ok."
                        jump continue5
                label continue5:
                    show orange happy
                    o "Ok lets get going"
                    o "Where to next?"
                    if VisitedUni == False and VisitedGov == False:
                        menu:
                            "I want to see the university!":
                                jump choiceUni

                            "GOVERNMENT!!!!! I'M ON THE PATH TO WORLD DOMINATION!":
                                show orange normal 
                                "God" "Orange is concerned for your sanity"
                                jump choiceGov

                            "I want to go home now, or to whatever is supposed to be my home here.":
                                jump choiceHome
                    elif VisitedUni == False and VisitedGov == True:
                        menu:
                            "I want to see the university!":
                                jump choiceUni

                            "I want to go home now, or to whatever is supposed to be my home here.":
                                jump choiceHome
                    elif VisitedGov == False and VisitedUni == True:
                        menu:
                            "GOVERNMENT!!!!! I'M ON THE PATH TO WORLD DOMINATION!":
                                show orange normal 
                                "God" "Orange is concerned for your sanity"
                                jump choiceGov

                            "I want to go home now, or to whatever is supposed to be my home here.":
                                jump choiceHome
                    elif VisitedGov == True and VisitedCircus == True:
                        menu:
                            "I want to go home now, or to whatever is supposed to be my home here.":
                                jump choiceHome

        label choiceGov: #meet lemon 
            $ VisitedGov = True
            o "Hahhhh, so, are you absolutely sure you want to go?"
            menu: 
                "Yes, of course!":
                    o "Alright then. Here we go."
                    jump continue6
                "Do you not want to go?":
                    o "Uhhh, it's fine. I'll bring you there. Come on, lets make this quick."
                    jump continue6
            label continue6:
                scene bg void with dissolve
                pause 0.2
                scene bg outside_gov with dissolve 
                show orange upset
                o "We are here. Lets go inside."
                show bg gov with dissolve
                o "So, everything looks super majestic and nice in here but it is often closed to the public."
                o "We do occasionally have tours avaliable though."
                menu:
                    "Do you lead tours here?":
                        o "Well, sometimes. It pays better than other tours but I like showing people around other parts of town more."
                o "Maybe I could bring you on one of those tours sometime."
                o "I promise you won't be disappointed"
                menu:
                    "Looking forward to it!":
                        show bg council_chambers with moveinright 
                        o "Anyways, here are the main council chambers which is where most decision making takes place."
                o "This is also the chamber that is open to the public the most and where people can come in to watch the council make decisions."
                show bg offices with moveinright
                o "Further in, we have the offices. We aren't allowed to go inside these offices as there are currently people working."
                o "They also have some other council chambers for smaller decisions they don't want to make in the main chamber."
                show bg closed_lemons_office
                o "Then finally, we have the president's chamber."
                o "The contents of this room are top secret with only a select few knowing what goes on behind those doors."
                o "It is best not to stay here for too long."
                o "Lets get going"
                menu:
                    "Ok, sure.":
                        jump leavingGov
                    "*Knock on the door*":
                        o "WHAT ARE YOU DOING!? WE AREN'T ALLOWED IN THERE!"
                        menu:
                            "ehe :D Don't worry about it":
                                o "Come on. Lets go. Please"
                                menu: 
                                    "Ok, fine. What do you have against this place?":
                                        o "..."
                                        jump leavingGov
                                    "NO!":
                                        o "Please-"
                                        jump meetLemon
                label meetLemon:
                    hide orange upset with moveoutleft
                    scene bg open_lemons_office
                    show lemon happy
                    l "Hi. Are you here for something?"
                    menu: 
                        "Oh, hello! Are you the president? I'm [yn].":
                            menu:
                                "I would like to learn how to take over your position.":
                                    show lemon normal
                                    l "Well, that is rather straight forward"
                                    l "Unfortunately, I don't believe that would be possible."
                                    l "I wish you a good day. Bye."
                                    jump continue7
                                "I would like to get to know you":
                                    l "Well, there's not much you can learn about me"
                                    l "I am Lemon, the president, and I worked hard to get to where I am."
                                    menu:
                                        "I am sure you are a very intesting person. Could I have a chat with you?":
                                            l "For sure. Come by later today and we can have a chat."
                                            $ isInvitedLemon = True
                                            l "However, for now, I do have some important matters to attend to."
                                            l "Looking forwards to our chat later."
                                    jump continue7
                                "Pleased to make your acquaintance. I need a job. Please hire me.":
                                    l "Oh. You can apply through my staff. I'm sure you already know them."
                                    menu:
                                        "What? I do? No I don't.":
                                            l "Ohhh, I see how it is. Alright. No worries then. I can handle your application."
                                    l "Do you have a resume with you?"
                                    menu: 
                                        "Oops, I don't.":
                                            l "Don't worry. You can come by later today and come find me."
                                            $ isInvitedLemon = True
                                    l "Now, if there isn't anything else, I need to get back to work. Please excuse me."
                                    jump continue7
                    label continue7:
                    scene bg closed_lemons_office
                    show orange normal
                    #Lemon disappears and orange appears again  
                    o "So, how was it?"
                    menu:
                        "Great!":
                            o "That's good."
                        "It was interesting.":
                            o "Hmm, idk if that's supposed to be good or not but I won't ask."
                        "The president is so rude >:(":
                            o "It do be like that sometimes..."             
                    menu:
                        "Anyways, Orange, where did you go?":
                            show orange upset
                            o "Sorry, I just... have a not so great history with the president."
                            o "I just went out for some air."
                            menu:
                                "Oh.":
                                    show orange normal
                                    o "I'm fine now. We should get going."
                                    menu: 
                                        "Ok":
                                            jump leavingGov
                                "Are you feeling alright now?":
                                    show orange normal
                                    o "Yep, thanks for asking!"
                                    o "We should get going though."
                                    menu:
                                        "Ok":
                                            jump leavingGov           

            label leavingGov:
                #change scene to outside gov building
                scene bg outside_gov
                show orange happy
                o "Alright, where to next?"
                
                if VisitedCircus == False and VisitedUni == False:
                    menu: 
                        "I'm curious as to what the university looks like.":
                            o "Ok, let's go there next then :D"
                            jump choiceUni

                        "Can we go visit the circus?":
                            o "Absolutely! I'm so excited"
                            jump choiceCircus

                        "I want to go home now, or to whatever is supposed to be my home here.":
                            jump choiceHome
                elif VisitedCircus == False and VisitedUni == True:
                    menu: 
                        "Can we go visit the circus?":
                            o "Absolutely! I'm so excited"
                            jump choiceCircus

                        "I want to go home now, or to whatever is supposed to be my home here.":
                            jump choiceHome
                elif VisitedUni == False and VisitedCircus == True:
                    menu: 
                        "I'm curious as to what the university looks like.":
                            o "Ok, let's go there next then :D"
                            jump choiceUni
                        "I want to go home now, or to whatever is supposed to be my home here.":
                            jump choiceHome
                elif VisitedGov == True and VisitedCircus == True:
                    menu:
                        "I want to go home now, or to whatever is supposed to be my home here.":
                            jump choiceHome



        label choiceHome: 
            o "So, unfortunately, we do not yet have a house for you."
            o "But fear not! I have an extra room at my place you can stay in."
            if isInvitedStrawberry and isInvitedLemon and isInvitedWatermelon:
                menu:
                    "Ok! Thank you! (You will stay with Orange)":
                        jump OrangeStory

                    "Actually, remember how Strawberry invited me to visit? Could you lead me there?":
                        o "Oh, right! No problem! To Strawberry's house we go!!"
                        #show God's void again
                        scene bg void with dissolve
                        pause 0.2
                        jump StrawberryStory

                    "I believe I deserve the best accommodations to exist in Fruit Bowl. BRING ME TO THE GOVERNMENT!":
                        #orange not happy
                        show orange upset
                        o "..."
                        o "Well, I tried. I'll bring you there now."
                        #enter God's void again
                        scene bg void with dissolve
                        pause 0.2
                        jump LemonStory

                    "Oh no I shouldn't bother you. I actually have a lot of experience being homeless so I might go find Watermelon and the circus.":
                        o "Oh have fun then!"
                        o "Bye!"
                        scene bg void with dissolve
                        pause 0.2
                        jump WatermelonStory
            elif isInvitedStrawberry and isInvitedLemon:
                menu:
                    "Ok! Thank you! (You will stay with Orange)":
                        jump OrangeStory

                    "Actually, remember how Strawberry invited me to visit? Could you lead me there?":
                        o "Oh, right! No problem! To Strawberry's house we go!!"
                        #show God's void again
                        scene bg void with dissolve
                        pause 0.2
                        jump StrawberryStory

                    "I believe I deserve the best accommodations to exist in Fruit Bowl. BRING ME TO THE GOVERNMENT!":
                        #orange not happy
                        show orange upset
                        o "..."
                        o "Well, I tried. I'll bring you there now."
                        #enter God's void again
                        scene bg void with dissolve
                        pause 0.2
                        jump LemonStory
            elif isInvitedStrawberry and isInvitedWatermelon:
                menu:
                    "Ok! Thank you! (You will stay with Orange)":
                        jump OrangeStory

                    "Actually, remember how Strawberry invited me to visit? Could you lead me there?":
                        o "Oh, right! No problem! To Strawberry's house we go!!"
                        #show God's void again
                        scene bg void with dissolve
                        pause 0.2
                        jump StrawberryStory

                    "Oh no I shouldn't bother you. I actually have a lot of experience being homeless so I might go find Watermelon and the circus.":
                        o "Oh have fun then!"
                        o "Bye!"
                        scene bg void with dissolve
                        pause 0.2
                        jump WatermelonStory
            elif isInvitedLemon and isInvitedWatermelon:
                menu:
                    "Ok! Thank you! (You will stay with Orange)":
                        jump OrangeStory

                    "I believe I deserve the best accommodations to exist in Fruit Bowl. BRING ME TO THE GOVERNMENT!":
                        #orange not happy
                        show orange upset
                        o "..."
                        o "Well, I tried. I'll bring you there now."
                        #enter God's void again
                        scene bg void with dissolve
                        pause 0.2
                        jump LemonStory

                    "Oh no I shouldn't bother you. I actually have a lot of experience being homeless so I might go find Watermelon and the circus.":
                        o "Oh have fun then!"
                        o "Bye!"
                        scene bg void with dissolve
                        pause 0.2
                        jump WatermelonStory
            elif isInvitedStrawberry:
                menu:
                    "Ok! Thank you! (You will stay with Orange)":
                        jump OrangeStory

                    "Actually, remember how Strawberry invited me to visit? Could you lead me there?":
                        o "Oh, right! No problem! To Strawberry's house we go!!"
                        #show God's void again
                        scene bg void with dissolve
                        pause 0.2
                        jump StrawberryStory
            elif isInvitedLemon:
                menu:
                    "Ok! Thank you! (You will stay with Orange)":
                        jump OrangeStory

                    "I believe I deserve the best accommodations to exist in Fruit Bowl. BRING ME TO THE GOVERNMENT!":
                        #orange not happy
                        show orange upset
                        o "..."
                        o "Well, I tried. I'll bring you there now."
                        #enter God's void again
                        scene bg void with dissolve
                        pause 0.2
                        jump LemonStory     
            elif isInvitedWatermelon:
                menu:
                    "Ok! Thank you! (You will stay with Orange)":
                        jump OrangeStory

                    "Oh no I shouldn't bother you. I actually have a lot of experience being homeless so I might go find Watermelon and the circus.":
                        o "Oh have fun then!"
                        o "Bye!"
                        scene bg void with dissolve
                        pause 0.2
                        jump WatermelonStory
            else:
                menu:
                    "Ok! Thank you! (You will stay with Orange)":
                        jump OrangeStory

    # This ends the game.

    return
