from textwrap import wrap
import cv2
import numpy as np
from keras.models import model_from_json
from windowcapture import WindowCapture
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
from windowcapture import WindowCapture
from keras.models import load_model
from tkinter import *
from tkinter import messagebox
from PyDictionary import PyDictionary
from random import randint
import tkinter.scrolledtext as st
import pyautogui

my_list = []
for x in pyautogui.getAllWindows():  
    win_name = (x.title)
    if win_name == '' or win_name == 'Program Manager' or win_name == 'Microsoft Text Input Application' or win_name == "ZPToolBarParentWnd" or win_name == "ZPTNativeTransferWnd" or win_name == "Settings" or win_name == "ZPTNativeTransferWnd" or win_name == "Word" or win_name == "ZPTNativeTransferWnd" or win_name == "File Explorer" or win_name == "ZPTNativeTransferWnd" or win_name == "PowerPoint":
        continue
    my_list.append(str(x.title.title()))

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

root = Tk()
app_width = 600 # Width 
app_height = 600 # Height
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen

screen_x = (screen_width/2) - (app_width/2)
screen_y = (screen_height/2) - (app_height/2)

root.geometry('%dx%d+%d+%d' % (app_width , app_height, screen_x, screen_y))
root.resizable(False, False)
bg = PhotoImage(file="images/emtnbg.png")
face_btn = PhotoImage(file="images/button1.png")
game_btn = PhotoImage(file="images/button2.png")
exit_btn = PhotoImage(file="images/button3.png")
gamebackground = PhotoImage(file="images/gameicons/gb4.png")
gbg2 = PhotoImage(file="images/gameicons/game_background.png")
play_btn = PhotoImage(file="images/gameicons/play.png")
interval_btn = PhotoImage(file="images/gameicons/interval.png")
check_btn = PhotoImage(file="images/gameicons/check.png")
search_btn = PhotoImage(file="images/gameicons/search.png")
entry_bg = PhotoImage(file="images/gameicons/entrybg.png")
submit =  PhotoImage(file="images/submit.png")
canvas1 = Canvas(root, width=600,
                height=600)
canvas1.pack(fill=BOTH, expand=True)
canvas1.create_image(0, 0, image=bg,
                    anchor="nw")
# canvas1.create_text( 200, 250, text = "Welcome", font=("Georgia", 40, "bold"), fg="purple")
app_label = canvas1.create_text(
    300, 100, text='EMOTION RECOGNITION', font=('Century Gothic', 35, 'bold'))
canvas1.itemconfig(app_label, fill='#6A3892')
app_description = canvas1.create_text(
    300, 140, text='TEACHER COMPANION FOR ONLINE LEARNING', font=('Century Gothic', 17, 'normal'))
canvas1.itemconfig(app_label, fill='#6A3892')
canvas1.itemconfig(app_description, fill='#3F3D3D')

    ################################################# Start of game ##################################################
def only_numbers(char):
    return char.isdigit()
validation = root.register(only_numbers)

delayervalue = 10
    
def delay_btn():
    global delayervalue
    interval = intervalEntry.get()
    delayervalue = int(interval)
    messagebox.showinfo("Updated Successfully", "You've successfully change the interval value.")

def show(selected_win):
    selected_win = clicked.get()
    def minigame():
        root.iconify()
        game_width = 889
        game_height = 500
        game_x = (screen_width/2) - (game_width/2)
        game_y = (screen_height/2) - (game_height/2)
        gameWindow = Toplevel(root)
        # sets the title of the
        gameWindow.title("MiniGame")

        # sets the geometry of toplevel
        gameWindow.geometry('%dx%d+%d+%d' % (game_width , game_height, game_x, game_y))
        gameWindow.resizable('False', 'False')
        canvas2 = Canvas(gameWindow, width=889,
                        height=500)
        canvas2.pack(fill="both", expand=True)
        canvas2.create_image(0, 0, image=gamebackground,
                            anchor="nw")

        def shuffle(s):
            stringLenght = len(s)
            li = list(s)

            for i in range(0, stringLenght - 1):
                pos = randint(i + 1, stringLenght - 1)

                li[pos], li[i] = li[i], li[pos]
                res = ""
                for i in range(stringLenght):
                    res = res + li[i]
                return res

        def Randomized():
            getresult = MyEntryBox.get().lower()
            global s
            global x
            s = getresult
            x = s
            shuffle(s)
            myTKlabel['text'] = shuffle(s)

        def CheckInputValue():
            answer = answerEntry.get().lower()
            if answer == '':
                messagebox.showwarning("Word not found", "Please try again!", parent=gameWindow)
            elif answer == x:
                messagebox.showinfo("Congratulation", "You are Correct!", parent=gameWindow)
            else:
                messagebox.showwarning("Wrong", "Want to try again?", parent=gameWindow)
        meaning_width = 550
        meaning_height = 280        
        meaning_x = (screen_width/2) - (meaning_width/2)
        meaning_y = (screen_height/2) - (meaning_height/2)
        def meaning():            
            dictionary=PyDictionary()
            meanings_list = dictionary.meaning(s)
            strip_word = str(meanings_list).replace("{","").replace("}", "").replace("[", '').replace("]", '').replace("'", '')
            if strip_word == 'None':
                messagebox.showwarning("Definition not found", "Please check the spelling", parent=gameWindow)
            elif s == '':
                messagebox.showwarning("Word not found", "Please try again!", parent=gameWindow)
            else:
                secondary_window = Toplevel()
                secondary_window.title(f'The meaning of "{x.upper()}"')
                secondary_window.geometry('%dx%d+%d+%d' % (meaning_width , meaning_height, meaning_x, meaning_y))
                secondary_window.resizable(False, False)
                canvas_board = Canvas(secondary_window, width=600,
                            height=350)
                canvas_board.configure(bg='#ffffff')
                canvas_board.pack(fill="both", expand=True)
                text_area = st.ScrolledText(canvas_board,width = 30,fg='#582308', bg="#f5b98c", height = 8, font = ("Bookman Old Style",20))
                text_area.grid(column = 0, pady = 10, padx = 10)
                # Inserting Text which is read only
                text_area.insert(INSERT,strip_word)
                # Making the text read only
                text_area.configure(state ='disabled')


        # Create Tkinter Entry Widget
        MyEntryBox = Entry(canvas2, borderwidth=0, show="•",
                        width=14,fg='#d6bda9', bg="#825e3e",font=('Bookman Old Style', 38))
        myTKlabel = Label(canvas2, borderwidth=0, relief="ridge",
                        width=15,fg='#d6bda9',bg="#825e3e", font=('Bookman Old Style', 37))
        answerEntry = Entry(canvas2, borderwidth=0,bg="#825e3e", width=14,fg='#d6bda9',
                            font=('Bookman Old Style', 38))
        randomizedButton = Button(
            canvas2, borderwidth=0, image=play_btn, bg='#825e3e', height=61, width=61, command=Randomized)
        answerChckButton = Button(
            canvas2, borderwidth=0, image=check_btn,bg='#825e3e', height=61, width=61, command=CheckInputValue)
        searchButton = Button(canvas2, borderwidth=0,image=search_btn,bg='#825e3e', height=61, width=61, command=meaning)

        MyEntryBox.place(x=214, y=62)
        myTKlabel.place(x=215, y=184)
        answerEntry.place(x=214, y=312)
        randomizedButton.place(x=622, y=62)
        answerChckButton.place(x=622, y=312)
        searchButton.place(x=560, y=312)
        # searchButton.place(x=(game_width/2) - (73/2), y=312)
        ################################################# end of game #################################################


    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
    green = (0, 255, 0)
    red = (0, 0, 255)
    orange = (0, 165, 255)
    yellow = (0, 255, 255)
    blue = (172, 117, 86)
    grey = (220, 220, 220)
    purple = (128, 0, 128)
    # load json and create model
    json_file = open('emotion_model(75).json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    emotion_model = model_from_json(loaded_model_json)

    # load weights into new model
    emotion_model.load_weights("emotion_model(75).h5")
    print("Loaded model from disk")

    # start the webcam feed
    #cap = cv2.VideoCapture(0)

    # pass here your video path
    # you may download one from here : https://www.pexels.com/video/three-girls-laughing-5273028/
    # cap = cv2.VideoCapture(0)

    # wincap = WindowCapture("New Tab - Google Chrome")
    wincap = WindowCapture(selected_win)

    def recognizeemtn():
        existenceOfEmtn = 0
        noExistenceOfEmtn = 0
        PERCENTAGEOFPSTEMTN = 35

        while True:
            initialize = False
            numberOfHappyFace = 0
            numberOfNotSmiling = 0
            # Find haar cascade to draw bounding box around face
            screenshot = wincap.get_screenshot()
            frame = screenshot
            frame = cv2.resize(frame, (1280, 720))
            face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # detect faces available on camera
            num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
            # take each face available on the camera and Preprocess it
            for (x, y, w, h) in num_faces:
                # cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
                roi_gray_frame = gray_frame[y:y + h, x:x + w]
                cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
                # count number of faces
                countFaces = len(num_faces)
                # predict the emotions
                emotion_prediction = emotion_model.predict(cropped_img)
                maxindex = int(np.argmax(emotion_prediction))
                countFaces = len(num_faces)

                class BarBackground:
                    def __init__(self, color):
                        self.color = color
                    def emotion_rect(self):
                        cv2.rectangle(frame, (x, y - 18), (x + w, y), self.color, -1)
                        cv2.rectangle(frame, (x, y), (x+w, y+h), self.color, 1)
                        cv2.line(frame, (x, y), (x+30, y), self.color, 3)  # Top Left
                        cv2.line(frame, (x, y), (x, y+30), self.color, 3)
                        cv2.line(frame, (x1, y), (x1-30, y), self.color, 3)  # Top Right
                        cv2.line(frame, (x1, y), (x1, y+30), self.color, 3)
                        cv2.line(frame, (x, y1), (x+30, y1), self.color, 3)  # Bottom Left
                        cv2.line(frame, (x, y1), (x, y1-30), self.color, 3)
                        cv2.line(frame, (x1, y1), (x1-30, y1), self.color, 3)  # Bottom right
                        cv2.line(frame, (x1, y1), (x1, y1-30), self.color, 3)
                        cv2.putText(frame, emotion_dict[maxindex], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 0, 1), 1)

                bc_0 = BarBackground(red) #angry
                bc_1 = BarBackground(purple) #disgusted
                bc_2 = BarBackground(orange) #fear
                bc_3 = BarBackground(green) #happy
                bc_4 = BarBackground(grey) #neutral
                bc_5 = BarBackground(blue) #sad
                bc_6 = BarBackground(yellow) #surprised
                #    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

                if maxindex == 3:
                    numberOfHappyFace += 1
                    initialize = True
                    x1, y1 = x+w, y+h
                    bc_3.emotion_rect()
                    
                else:
                    numberOfNotSmiling += 1
                    initialize = True
                    # # font style
                    # x1, y1 = x+w, y+h
                    # bc_0.emotion_rect()

                percentageOfEmotion = numberOfHappyFace / countFaces * 100
                percentageOfNegativeEmtn = numberOfNotSmiling / countFaces * 100
                frameX, frameY, frameWidth, FrameHeight = 0, 0, 250, 100

                if maxindex == 0:
                    x1, y1 = x+w, y+h
                    bc_0.emotion_rect()
                elif maxindex == 1:
                    x1, y1 = x+w, y+h
                    bc_1.emotion_rect()
                
                elif maxindex == 2:
                    x1, y1 = x+w, y+h
                    bc_2.emotion_rect()

                elif maxindex == 4:
                    x1, y1 = x+w, y+h
                    bc_4.emotion_rect()
                
                elif maxindex == 5:
                    x1, y1 = x+w, y+h
                    bc_5.emotion_rect()

                elif maxindex == 6:
                    x1, y1 = x+w, y+h
                    bc_6.emotion_rect()

                cv2.rectangle(frame, (frameX, frameX), (frameX + frameWidth, frameY + FrameHeight), (0, 0, 0), -1)
                # Show the data of the emotion here
                cv2.putText(frame, "Number of Students: " + str(countFaces), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0, 1), 1)
                cv2.putText(frame, "Number of Smiling: " + str(numberOfHappyFace), (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0, 1), 1)
                cv2.putText(frame, "Percentage of Happy: " + f'{percentageOfEmotion:0.1f}', (10, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0, 1), 1)
            if (initialize == True and percentageOfNegativeEmtn == 100) and percentageOfEmotion == 0:
                noExistenceOfEmtn += 1
                # counting += 1
                # print(delayervalue)
                if noExistenceOfEmtn == delayervalue:
                    MsgBox = messagebox.askquestion(
                        'Notification', 'Do you want to open the minigame', icon='warning')
                    if MsgBox == 'yes':
                        # messagebox.showinfo(
                        #     "Advisory", "Please click the computer vision window and press 'q' on keyboard")
                        minigame()
                        cv2.destroyAllWindows()
                        break
                    else:
                        noExistenceOfEmtn = 0
                        messagebox.showinfo(
                            'Return', 'You will now return to the application screen')
            elif initialize == True and percentageOfEmotion <= PERCENTAGEOFPSTEMTN:
                existenceOfEmtn += 1
                # print(delayervalue)
                if existenceOfEmtn == delayervalue:
                    MsgBox = messagebox.askquestion(
                        'Notification', 'Do you want to open the minigame', icon='warning')
                    if MsgBox == 'yes':
                        # messagebox.showinfo(
                        #     "Advisory", "Please click the computer vision window and press 'q' on keyboard")
                        minigame()
                        cv2.destroyAllWindows()
                        break
                    else:
                        existenceOfEmtn = 0
                        messagebox.showinfo(
                            'Return', 'You will now return to the application screen')
            else:
                noExistenceOfEmtn = 0
            cv2.imshow("Computer Vision", frame)
            cv2.waitKey(1)
            if cv2.getWindowProperty('Computer Vision', cv2.WND_PROP_VISIBLE) < 1:
                break
        cv2.destroyAllWindows()

    def exits():
        root.destroy()


    # Creating a button that will allow the user to set the frequency of the pop-up.
    button1 = Button(canvas1, image=face_btn, borderwidth=0, command=recognizeemtn)
    button1.place(x=200, y=350)
    button2 = Button(canvas1, image=game_btn, borderwidth=0, command=minigame)
    button2.place(x=200, y=425)
    button3 = Button(canvas1, image=exit_btn, borderwidth=0, command=exits)
    button3.place(x=200, y=500)
options = my_list

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set('Select Window')


# Create Dropdown menu
interval_label = canvas1.create_text(300, 255, text='POP-UP FREQUENCY (1-100)', font=('Century Gothic', 8, 'bold'))
canvas1.itemconfig(interval_label, fill='#6A3892')
intervalEntry = Entry(canvas1,validate="key", validatecommand=(validation, '%S'), borderwidth=1, width=11, font=('Century Gothic', 22))
intervalEntry.insert(0, "(1-100)")
intervalEntry.place(x=202, y=276)
intervalButton = Button(canvas1, borderwidth=0, image=interval_btn,  command=delay_btn)
intervalButton.place(x=368, y=275)
drop = OptionMenu( canvas1 , clicked , *options, command=show)
drop.place(x=202, y=200)
drop.config(width = 15, font=('Century Gothic', 15, 'bold'))
# button = Button(canvas1, image=submit, borderwidth=0, command=show)
# button.place(x=160, y=2)
root.mainloop()
