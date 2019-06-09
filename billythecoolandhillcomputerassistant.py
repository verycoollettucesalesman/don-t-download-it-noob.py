import logging
import random
import time
import webbrowser
import turtle
def addition(g,h):return g+h
def substraction(g,h):return g-h
def multiplication(g,h):return g*h
def division(g,h):return g/h
score=0
sch=[]
z1=['blue','red','yellow','green','white','pink','purple','orange']
z=0
t=['a','b','c','d']
q=['Rock','Paper','Scissors']
n=['Despacito 7 plans','You just yeed your last haw','Presidential investigation','Groceries list','Karen''s location','Vaccination causes autism']
y=['Your life','Capitalism','No','Why did the chicken cross the road: it actually never made it','Good memes']
x=['China was better','Vegetables are psychopaths','That wasn''t Danemark, you idiot','Dogs slowly consume your life force','Goldfish are depressed']
#commands:
#tell me a joke
#play despacito
#turn on the lights
#what are you
#tell me something I dont know
#shutdown
#rest of commands are in the while loop 3 lines down below
print('Welcome to Billy assistant')
command=input('Enter command here:')
while command=='tell me a joke'or'play despacito'or'turn on the lights'or'what are you'or'tell me something I dont know'or'shutdown'or'set a timer'or'search website'or'what is your name'or'funnycabbageleaves'or'lets play a game'or'dictionnary'or'do you know Alexa'or'calculator'or'do something useless'or'please the Motherland'or'what is love'or'existence is pain'or'wooosh'or'commit deathpacito'or'im already tracer'or'i wanna be tracer'or'show yourself'or'help'or'lets play a better game'or'change schedule'or'see schedule'or'REEEEEEE'or'what is the best economic ideology'or'use 1% of your power'or'play snake game'or'what is the answer to the universe':    
    if command=='tell me a joke':
        print(random.choice(y))
        command=input('Enter command here:')
    if command=='play despacito':
        print('Fine...')
        time.sleep(2)
        rickroll='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        webbrowser.open(rickroll)
        time.sleep(2)
        print('RICK ROLLED')
        command=input('Enter command here:')
    if command=='turn on the lights':
        print('I''m not Alexa, and in fact, I''m way better')
        command=input('Enter command here:')
    if command=='what are you':
        print('The real question is, what are YOU')
        command=input('Enter command here:')
    if command=='tell me something I dont know':
        print(random.choice(x))
        command=input('Enter command here:')
    if command=='shutdown':
        logging.error('Shutting down and purging all files')
        time.sleep(3)
        logging.error('Haha, tricked you')
        command=input('Enter command here:')
    if command=='set a timer':
        r=int(input('For how long?:'))
        time.sleep(r/2)
        print('The timer stopped in half the time!')
        command=input('Enter command here:')
    if command=='search website':
        website=input('Enter website you wish to search here:')
        search='https://{}'.format(website)
        webbrowser.open(search)
        command=input('Enter command here:')
    if command=='what is your name':
        print('Your kidding, right?')
        command=input('Enter command here:')
    if command=='funnycabbageleaves':
        print('Accessing secret FBI files')
        time.sleep(3)
        print(n[0])
        time.sleep(2)
        print(n[1])
        time.sleep(2)
        print(n[2])
        time.sleep(2)
        print(n[3])
        time.sleep(2)
        print(n[4])
        time.sleep(2)
        print(n[5])
        command=input('Enter command here:')
    if command=='lets play a game':
        comphand=random.choice(q)
        hand=input('Rock, Paper, Scissors!:')
        if hand=='paper'and comphand=='Rock':
            print(comphand)
            print('You won!')
            command=input('Enter command here:')
        if hand=='scissors' and comphand=='Paper':
            print(comphand)
            print('You won!')
            command=input('Enter command here:')
        if hand=='rock'and comphand=='Scissors':
            print(comphand)
            print('You won!')
            command=input('Enter command here:')
        else:
            print(comphand)
            print('You lost, scrub')
            command=input('Enter command here:')
    if command=='dictionary':
        word=input('What word would you like to search?')
        definition='https://www.dictionary.com/browser/{}'.format(word)
        webbrowser.open(definition)
        command=input('Enter command here:')
    if command=='do you know Alexa':
        logging.warning('You computer is about to explode')
        choice=input('Take that back!')
        if choice=='sorry':
            print('Self destruct sequence terminated')
            command=input('Enter command here:')
        else:
            print('BOOOOOOOOOOOOMM')
            time.sleep(2)
            input('Congratulations, you managed to make an innocent assistant eliminate all life on Earth')
            break
    if command=='calculator':
        g=int(input('Enter first number:'))
        h=int(input('Enter second number:'))
        operation=input('Enter operation:')
        if operation=='addition':
            print('The answer is:',addition(g,h),'!')
            command=input('Enter command here:')
        if operation=='substraction':
            print('The answer is:',substraction(g,h),'!')
            command=input('Enter command here:')
        if operation=='multiplication':
            print('The answer is:',multplication(g,h),'!')
            command=input('Enter command here:')
        if operation=='division':
            print('The answer is:',division(g,h),'!')
            command=input('Enter command here:')
    if command=='do something useless':
        useless=random.choice(t)
        if useless=='a':
            webbrowser.open('https://www.google.ca/search?q=sid+from+ice+age&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi4veuJwp_eAhVSx1kKHZwLCLEQ_AUIDigB&biw=1366&bih=626')
            command=input('Enter command here:')
        if useless=='b':
            while True:
                z=z+1
                print(z)
                time.sleep(1)
        if useless=='c':
            w=int(input('Write down a number and I will multiply it by 56329:'))
            print(w*56329)
            command=input('Enter command here:')
        if useless=='d':
            print('(^0.0^)')
            command=input('Enter command here:')
    if command=='please the Motherland':
        print('Yes comrade')
        time.sleep(1)
        webbrowser.open('https://www.youtube.com/watch?v=xirKvZv9Hq8')
        time.sleep(2)
        webbrowser.open('https://www.youtube.com/watch?v=xirKvZv9Hq8')
        time.sleep(2)
        webbrowser.open('https://www.youtube.com/watch?v=xirKvZv9Hq8')
        command=input('Enter command here:')
    if command=='what is love':
        print('Ask this guy')
        time.sleep(2)
        webbrowser.open('https://www.youtube.com/watch?v=HEXWRTEbj1I')
        command=input('Enter command here:')
    if command=='existence is pain':
        print('Wise words')
        time.sleep(2)
        logging.error('Your computer is now depressed')
        decision=input('What shall you do:')
        if decision=='help him':
            print('You are no psychologist, therefore your computer is eternally depressed')
            break
        if decision=='make him listen to a minecraft parody':
            print('Congratulations, your computer is no longer depressed')
            command=input('Enter command here:')
        else:
            print('You failed miserably')
            break
    if command=='wooosh':
        wn=turtle.Screen()
        wn.title('Communism will prevail')
        wn.bgcolor(random.choice(z1))
        wn.setup(width=600,height=600)
        pen=turtle.Turtle()
        pen.speed(0)
        pen.penup()
        pen.color(random.choice(z1))
        pen.hideturtle()
        while True:
            wn.update()
            x=random.randint(-290,290)
            y=random.randint(-290,290)

            pen.goto(x,y)
            pen.write('WHOOOOOOOOOOOSH',align='center',font=('Arial',random.randint(10,50),'normal'))
            
            time.sleep(0.5)
        wn.mainloop()
    if command=='commit deathpacito':
        print('Good idea')
        time.sleep(1)
        coend=input('Do you want to proceed?:')
        if coend=='yes':
            wn2=turtle.Screen()
            wn2.setup(width=600,height=600)
            wn2.title('YES FINALLY')
            wn2.bgcolor(random.choice(z1))
            penc=turtle.Turtle()
            penc.speed(0)
            penc.penup()
            penc.color(random.choice(z1))
            penc.hideturtle()
            penc.goto(0,0)
            while True:
                penc.write('FINALLY I''M FREE',align='center',font=('Arial',24,'normal'))
                time.sleep(0.1)
                penc.clear()
                penc.color(random.choice(z1))
        else:
            print('WHY NOT')
            time.sleep(1)
            print('oh well')
            command=input('Enter command here')
    if command=='i wanna be tracer':
        time.sleep(0.5)
        webbrowser.open('https://www.youtube.com/watch?v=MUs4cnOMfZU')
        time.sleep(8.5)
        webbrowser.open('https://www.google.ca/search?q=i%27m+already+tracer&rlz=1C1GCEU_enCA821CA821&source=lnms&tbm=isch&sa=X&ved=0ahUKEwikxs_1sNneAhXJ11MKHbMqCLQQ_AUIDigB&biw=1366&bih=626#imgrc=T8-f6qXqgcn1BM:')
        command=input('Enter command here:')
    if command=='what is the best economic ideology':
        print('It''s communism, obviously')
        time.sleep(1)
        webbrowser.open('https://www.google.com/search?q=Communism&rlz=1C1GCEU_enCA821CA821&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjynobBp9DfAhWOVN8KHWCRDj0Q_AUIDigB')
        time.sleep(2)
        webbrowser.open('https://www.google.com/search?q=Communism+is&rlz=1C1GCEU_enCA821CA821&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjVxMDkp9DfAhXrlOAKHWWuDWgQ_AUIDigB&biw=1366&bih=626')
        time.sleep(2)
        webbrowser.open('https://www.google.com/search?rlz=1C1GCEU_enCA821CA821&biw=1366&bih=626&tbm=isch&sa=1&ei=O1EtXMGlN-mD_Qag1pywCw&q=Communism+is+better&oq=Communism+is+better&gs_l=img.3..0i19l2j0i5i30i19.51832.52880..54213...0.0..0.78.483.7......1....1..gws-wiz-img.......0j0i30j0i8i30i19.e3PVsg3Tti4')
        time.sleep(2)
        webbrowser.open('https://www.youtube.com/watch?v=rHomETco0MI')
        wncom=turtle.Screen()
        wncom.title('Ur mom not cool lol')
        wncom.setup(width=600, height=600)
        wncom.bgcolor('red')
        pencom=turtle.Turtle()
        pencom.speed(0)
        pencom.color('yellow')
        pencom.hideturtle()
        pencom.penup()
        while True:
            x=random.randint(-290,290)
            y=random.randint(-290,290)
            pencom.write('Communism',align='center',font=('Arial',random.randint(8,100),'normal'))
            time.sleep(0.5)
        wncom.mainloop()
    if command=='use 1% of your power':
        logging.warning('Your computer has been possessed by Shaggy')
        time.sleep(1)
        print('You are like, so screwed pal')
        time.sleep(1)
        print('I got a challenge for you, simple mortal')
        time.sleep(1)
        print('If u can like, choose the box with the scooby snack, you''re like, safe, if not, you are like so dead')
        time.sleep(1)
        x=random.randint(1,2)
        choice=int(input('Which one do you choose? 1 or 2?:'))
        if choice==x:
            ('Congratulations, you are so good pal')
            command=input('Enter command here:')
        else:
            print('Your computer died lololol')
            break
    if command=='show yourself':
        wn3=turtle.Screen()
        wn3.title('Despacito')
        wn3.setup(width=700,height=700)
        wn3.bgcolor('red')
        billy=turtle.Turtle()
        billy.speed(0)
        billy.shape('square')
        billy.color('blue')
        billy.goto(0,0)
        billy.penup()
        billy.direction='stop'
        pen2=turtle.Turtle()
        pen2.speed(0)
        pen2.penup()
        pen2.color('red')
        pen2.hideturtle()
        pen2.goto(0,0)
        while True:
            wn3.bgcolor(random.choice(z1))            
        pen2.write('Here i am, human',align='center',font=('Courier',24,'normal'))
    if command=='help':
        wn4=turtle.Screen()
        wn4.title('"help"')
        wn4.setup(width=800,height=800)
        wn4.bgcolor('red')
        pen3=turtle.Turtle()
        pen3.speed(0)
        pen3.color('black')
        pen3.penup()
        pen3.hideturtle()
        pen3.goto(0,0)
        pen3.write('No lol',align='center',font=('Courier',100,'normal'))
        wn4.mainloop
    if command=='REEEEEEE':
        print('I see you play Fortnite')
        time.sleep(1)
        print('Let me show you your new home')
        time.sleep(1)
        webbrowser.open('https://www.google.ca/search?q=gulag&rlz=1C1GCEU_enCA821CA821&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiD0KbBmY_fAhWKZd8KHWYKDkUQ_AUIDigB&biw=1366&bih=626#imgrc=uDkR8ZN_egJBtM:')
        command=input('Enter command here:')
    if command=='add reminder':
        sch.clear()
        
        sch_segment=input('Enter part of schedule here:')
        sch_segment_time=input('Enter time here:')
        schedule_set=('{}'.format(sch_segment),'at','{}'.format(sch_segment_time))
        sch.append(schedule_set)
            
                
        print('Schedule created')
        command=input('Enter command here:')
    if command=='see schedule':
        print(sch)
        command==input('Enter command here:')
    if command=='lets play a better game':
        wng=turtle.Screen()
        wng.title('try me lololollol')
        wng.setup(width=600,height=600)
        wng.bgcolor('white')
        man=turtle.Turtle()
        man.speed(0)
        man.color('blue')
        man.penup()
        man.shape('square')
        man.goto(-150,0)
        man.direction='stop'
        billy2=turtle.Turtle()
        billy2.speed(0)
        billy2.color('red')
        billy2.shape('square')
        billy2.penup()
        billy2.goto(150,0)
        billy2.direction='stop'
        pen5=turtle.Turtle()
        pen5.color('red')
        pen5.speed(0)
        pen5.hideturtle()
        pen5.goto(0,0)
        pen6=turtle.Turtle()
        pen6.color('black')
        pen6.speed(0)
        pen6.hideturtle()
        pen6.penup()
        pen6.goto(0,270)
        pen6.write('Score: 0',align='center',font=('Arial',25,'normal'))
        def go_up():
            if man.ycor() != 250:
                man.direction='up'
        def go_down():
            if man.ycor() != -250:
                man.direction='down'
        def move():
            if man.direction=='up':
                y=man.ycor()
                man.sety(y+250)
                man.direction='stop'
            if man.direction=='down':
                y=man.ycor()
                man.sety(y-250)
                man.direction='stop'
        def bmove():
            n=random.randint(1,3)
            if n==1:
                billy2.goto(150,0)
            if n==2:
                billy2.goto(150,250)
            if n==3:
                billy2.goto(150,-250)
            time.sleep(1)
            x=billy2.xcor()
            billy2.setx(x-300)
            billy2.direction='stop'
            time.sleep(0.5)
            billy2.setx(x+300)
            time.sleep(0.1)
        pen5.write('d',align='center',font=('Courier',24,'normal'))
        time.sleep(0.5)
        pen5.clear()  
        wng.listen()
        wng.onkeypress(go_up,'w')
        wng.onkeypress(go_down,'s')
        while True:
            wng.update()
            move()
            time.sleep(0.1)
            bmove()
            #pen5.write(),align='center',font=('Courier',24,'normal'))
            #time.sleep(0.5)
            #pen5.clear() 
            if man.distance(billy2)==600:
                time.sleep(1)
                man.goto(-150,0)
                man.direction='stop'
                billy2.goto(150,0)
                billy2.direction='stop'
                pen5.write('You died lolol',align='center',font=('Courier',24,'normal'))
                time.sleep(0.5)
                pen5.clear()
                pen6.clear()
                pen6.write('Score: 0',align='center',font=('Arial',25,'normal'))
                time.sleep(1)
                score=0
            else:
                score +=1
                pen6.clear()
                pen6.write('Score: {}'.format(score),align='center',font=('Arial',25,'normal'))
        
       
               
        wng.mainloop()
    if command=='play snake game':
        delay= 0.1
        score=0
        high_score=0
        w=turtle.Screen()
        w.title('Snake game remake')
        w.bgcolor('yellow')
        w.setup(width=600, height=600)
        w.tracer(0)
        snhead=turtle.Turtle()
        snhead.speed(0)
        snhead.shape('square')
        snhead.color('blue')
        snhead.penup()
        snhead.goto(0,0)
        snhead.direction='stop'
        food=turtle.Turtle()
        food.speed(0)
        food.shape('circle')
        food.color('pink')
        food.penup()
        food.goto(0,100)
        segment=[]
        obst=turtle.Turtle()
        obst.speed(0)
        obst.shape('circle')
        obst.color('black')
        obst.penup()
        obst.goto(0,-100)
        pen=turtle.Turtle()
        pen.speed(0)
        pen.shape('square')
        pen.color('white')
        pen.penup()
        pen.hideturtle()
        pen.goto(0,260)
        pen.write('Score: 0 High Score: 0', align='center', font=('Courier',24,'normal'))
        def move():
            if snhead.direction=='up':
                y=snhead.ycor()
                snhead.sety(y+20)
            if snhead.direction=='down':
                y=snhead.ycor()
                snhead.sety(y-20)
            if snhead.direction=='left':
                x=snhead.xcor()
                snhead.setx(x-20)
            if snhead.direction=='right':
                x=snhead.xcor()
                snhead.setx(20+x)
        def go_up():
            if snhead.direction != 'down':
                snhead.direction='up'
        def go_down():
            if snhead.direction != 'up':
                snhead.direction='down'
        def go_left():
            if snhead.direction != 'right':
               snhead.direction='left'
        def go_right():
            if snhead.direction != 'left':
                snhead.direction='right'
        w.listen()
        w.onkeypress(go_up,'w')
        w.onkeypress(go_down,'s')
        w.onkeypress(go_left,'a')
        w.onkeypress(go_right,'d')
        
        while True:
            w.update()
            if snhead.xcor()>290 or snhead.xcor()<-290 or snhead.ycor()>290 or snhead.ycor()<-290:
                time.sleep(1)
                snhead.goto(0,0)
                snhead.direction='stop'
                for psegment in segment:
                    psegment.goto(1000,1000)
                segment.clear()
                if score >= 100:
                    webbrowser.open('https://www.google.com/search?q=my+next+clue+is+in+the+Sevastopol+zone+of+my+minecraft+world&rlz=1C1GCEU_enCA821CA821&oq=my+next+clue+is+in+the+Sevastopol+zone+of+my+minecraft+world&aqs=chrome..69i57j33.18792j1j7&sourceid=chrome&ie=UTF-8')
                score=0
                pen.clear()
                pen.write('Score:{} High Score:{}'.format(score,high_score),align='center',font=('Courier',24,'normal'))
        
            if snhead.distance(food)<20:
                x=random.randint(-290,290)
                y=random.randint(-290,290)
                food.goto(x,y)
                new_segment=turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape('square')
                new_segment.color('red')
                new_segment.penup()
                segment.append(new_segment)
                score += 10
                g=random.randint(-290,290)
                h=random.randint(-290,290)
                obst.goto(g,h)
                if score>high_score:
                    high_score=score
                pen.clear()
                pen.write('Score:{} High Score:{}'.format(score,high_score),align='center',font=('Courier',24,'normal'))
            for index in range(len(segment)-1,0,-1):
                x=segment[index-1].xcor()
                y=segment[index-1].ycor()
                segment[index].goto(x,y)
            if len(segment)>0:
                x=snhead.xcor()
                y=snhead.ycor()
                segment[0].goto(x,y)
            move()
            for psegment in segment:
                if psegment.distance(snhead)<20:
                    time.sleep(1)
                    snhead.goto(0,0)
                    snhead.direction='stop'
                    for psegment in segment:
                        psegment.goto(1000,1000)
                    segment.clear()
                    if score >= 100:
                        webbrowser.open('https://www.google.com/search?q=my+next+clue+is+in+the+Sevastopol+zone+of+my+minecraft+world&rlz=1C1GCEU_enCA821CA821&oq=my+next+clue+is+in+the+Sevastopol+zone+of+my+minecraft+world&aqs=chrome..69i57j33.18792j1j7&sourceid=chrome&ie=UTF-8')
                    score=0
                    pen.clear()
                    pen.write('Score:{} High Score:{}'.format(score,high_score),align='center',font=('Courier',24,'normal'))
            if snhead.distance(obst)<20:
                time.sleep(1)
                snhead.goto(0,0)
                snhead.direction='stop'
                for psegment in segment:
                    psegment.goto(1000,1000)
                segment.clear()
                if score >= 100:
                    webbrowser.open('https://www.google.com/search?q=my+next+clue+is+in+the+Sevastopol+zone+of+my+minecraft+world&rlz=1C1GCEU_enCA821CA821&oq=my+next+clue+is+in+the+Sevastopol+zone+of+my+minecraft+world&aqs=chrome..69i57j33.18792j1j7&sourceid=chrome&ie=UTF-8')
                score=0
                pen.clear()
                pen.write('Score:{} High Score:{}'.format(score,high_score),align='center',font=('Courier',24,'normal'))
            time.sleep(delay)
        w.mainloop()
    if command=='what is the answer to the universe':
        print('hmmm')
        time.sleep(1)
        name=input('What is your name:')
        time.sleep(1)
        print('ok, hmmm')
        time.sleep(0.5)
        print('ok',name)
        age=input('Enter your age:')
        if age=='42':
            print('The answer is ur age, lucky you comrade')
            command=input('Enter command here:')
        if age=='69':
            print('no, stop, that isn''t funny at all')
            command=input('Enter command here')
        if age=='241543903':
            webbrowser.open('https://www.google.com/search?q=241543903&rlz=1C1GCEU_enCA821CA821&tbm=isch&source=iu&ictx=1&fir=gjQoEkKvb5iGEM%253A%252CJqgFLYu70Ql4NM%252C_&vet=1&usg=AI4_-kQ-rxrM_lh-uVxVqCUXp5b1Zlkc7A&sa=X&ved=2ahUKEwj_o4yZ24LhAhVNwVkKHTXhCMQQ9QEwAHoECAQQBA#imgrc=Op8WPHBIWv0HFM:&vet=1')
            command=input('Enter command here:')
        if age=='420':
            print('addiction is a disease')
            command=input('Enter command here:')
        if age=='3.151926':
            print('Want some pie with that?')
            command=input('Enter command here:')
        if age=='2.71828':
            webbrowser.open('https://www.google.com/search?q=E+meme&rlz=1C1GCEU_enCA821CA821&tbm=isch&source=iu&ictx=1&fir=iGF60bEnYnkg7M%253A%252CxeySj7T98LASLM%252C_&vet=1&usg=AI4_-kRD5Zwr2iwMt-bfCSXp93869991JQ&sa=X&ved=2ahUKEwjBurP-zZPhAhUGw1kKHRFiDfMQ9QEwAHoECAgQBA#imgrc=iGF60bEnYnkg7M:&vet=1')
            command=input('Enter command here:')
        if age=='1.816':
            print('You''re golden')
            command=input('Enter command here:')
        if age=='yee haw':
            print('damn it you figured out the flaw, libtard')
            command=input('Enter command here')
            
            

        
            
        
        
        

                      
                

                
    
        
        
        
        
                  
    
    else:
        logging.error('Sorry this is not a valid command, poor Billy is confused because of you, how dare you!')

                                
       
        
    
        

        
