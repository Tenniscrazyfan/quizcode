import pgzrun


WIDTH = 800
HEIGHT = 600


q_box = Rect(20,100,610,90)
answer1=  Rect(20,200,300,100)
answer2 = Rect(20,310,300,100)
answer3 = Rect(330,200,300,100)
answer4 = Rect(330,310,300,100)
timer = Rect(700,100,90,90)
skipbox = Rect(700,200,90,210)

times = 10
questions = []

answers = [answer1,answer2,answer3,answer4]
question_count = 10
question_index = 0
gameover = False
q = ""

def draw():
    global q, times
    screen.fill("Black")
    screen.draw.filled_rect(q_box,"Blue")
    screen.draw.filled_rect(timer,"Blue")
    screen.draw.filled_rect(skipbox,"Green")
    for i in answers:
        screen.draw.filled_rect(i,"orange")
    screen.draw.textbox("SKIP",skipbox,color = "Black")
    screen.draw.textbox(str(times),timer,color = "White")
    screen.draw.textbox(q[0].strip(),q_box,color = "White")
    index = 1
    for abox in answers:
        screen.draw.textbox(q[index].strip(),abox,color = "White")
        index = index + 1
    if gameover == True :
        q = [" It is wrong", "-" ,"-","-","-",5]
        times  = 0




def time() :
    global times,gameover
    if gameover == False :

        times = times- 1
    


clock.schedule_interval(time,1)

def read_question_file():
    global questions
    q_file = open("quiz.txt","r")
    questions = q_file.readlines()
    print(questions)



def readquestion():
    global q,questions,question_index
    question_index = question_index + 1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    global q, questions,gameover,times
    index = 1
    for abox in answers:
        if abox.collidepoint(pos):
            if index == int(q[5]):
                q = readquestion()
                times = 10
                print(q)
            else:
                gameover = True
        index = index + 1
    if skipbox.collidepoint(pos):
       skip_question()

def skip_question():
     global q, times
     if gameover == False:
        q = readquestion()
        times = 10


read_question_file()
q = readquestion() 



pgzrun.go()
