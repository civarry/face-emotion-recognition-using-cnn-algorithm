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

# my_list = []
# for x in pyautogui.getAllWindows():  
#     win_name = x.title
#     if win_name == '' or 'Telegram' in win_name or win_name == 'gameicons' or win_name == 'Program Manager' or win_name == 'Microsoft Text Input Application' or win_name == "ZPToolBarParentWnd" or win_name == "ZPTNativeTransferWnd" or win_name == "Settings" or win_name == "ZPTNativeTransferWnd" or win_name == "Word" or win_name == "ZPTNativeTransferWnd" or win_name == "File Explorer" or win_name == "ZPTNativeTransferWnd" or win_name == "PowerPoint":
#         continue
#     my_list.append(str(x.title.title()))
my_list = []
for x in pyautogui.getAllWindows():  
    win_name = x.title
    if win_name == '':
        continue
    if "Google Chrome" in win_name or "Edge" in win_name or "Opera" in win_name or "Firefox" in win_name or "Browser" in win_name or "Meet" in win_name:
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
information_btn = PhotoImage(file="images/gameicons/infobtn.png")
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

DELAY_VALUE_MIN = 1
DELAY_VALUE_MAX = 100
delayer_value = 10

def delay_btn():
    interval_str = intervalEntry.get()
    try:
        interval = int(interval_str)
        if interval < DELAY_VALUE_MIN or interval > DELAY_VALUE_MAX:
            messagebox.showwarning("Value Exceeded", f"Please adjust the value between {DELAY_VALUE_MIN}-{DELAY_VALUE_MAX} only")
        else:
            messagebox.showinfo("Updated Successfully", "You've successfully change the interval value.")
            global delayer_value
            delayer_value = interval
    except ValueError:
        messagebox.showerror("Invalid Value", "Please enter a valid integer value between 1-100.")
        
def info_btn():
    messagebox.showinfo("Notification Frenquency", "You can change the sensitivity of the notification feature here. This allows you to control how often or how quickly you receive notifications when the system detects negative emotions.")

def show(selected_win):
    selected_win = clicked.get()
    def minigame():
        # Create a Toplevel window for the game
        game_window_width = 889
        game_window_height = 500
        game_window_x = (screen_width / 2) - (game_window_width / 2)
        game_window_y = (screen_height / 2) - (game_window_height / 2)
        game_window = Toplevel(root)
        game_window.title("MiniGame")
        game_window.geometry('%dx%d+%d+%d' % (game_window_width, game_window_height, game_window_x, game_window_y))
        game_window.resizable(False, False)

        def shuffle_word():
            # Shuffle the word entered by the user
            original_word = my_entry_box.get().lower()
            global shuffled_word
            global original_word_global
            shuffled_word = original_word
            original_word_global = original_word
            shuffled_word = shuffle(shuffled_word)
            my_tk_label['text'] = shuffled_word

        def shuffle(word):
            # Shuffle the characters in the given word
            word_length = len(word)
            characters = list(word)

            for i in range(0, word_length - 1):
                pos = randint(i + 1, word_length - 1)

                characters[pos], characters[i] = characters[i], characters[pos]
            shuffled_word = ""
            for i in range(word_length):
                shuffled_word = shuffled_word + characters[i]
            return shuffled_word

        def check_input_value():
            # Check if the user's answer is correct
            answer = answer_entry.get().lower()
            if answer == '':
                messagebox.showwarning("Word not found", "Please try again!", parent=game_window)
            elif answer == original_word_global:
                messagebox.showinfo("Congratulations", "You are Correct!", parent=game_window)
            else:
                messagebox.showwarning("Wrong", "Want to try again?", parent=game_window)

        def show_meaning():
            # Show the meaning of the original word
            dictionary = PyDictionary()
            meanings_list = dictionary.meaning(original_word_global)
            strip_word = str(meanings_list).replace("{","").replace("}", "").replace("[", '').replace("]", '').replace("'", '')
            if strip_word == 'None':
                messagebox.showwarning("Definition not found", "Please check the spelling", parent=game_window)
            elif original_word_global == '':
                messagebox.showwarning("Word not found", "Please try again!", parent=game_window)
            else:
                # Create a new window to display the meaning
                meaning_window_width = 550
                meaning_window_height = 280        
                meaning_window_x = (screen_width / 2) - (meaning_window_width / 2)
                meaning_window_y = (screen_height / 2) - (meaning_window_height / 2)
                secondary_window = Toplevel()
                secondary_window.title(f'The meaning of "{original_word_global.upper()}"')
                secondary_window.geometry('%dx%d+%d+%d' % (meaning_window_width, meaning_window_height, meaning_window_x, meaning_window_y))
                secondary_window.resizable(False, False)
                
                # Create a canvas to hold the meaning text
                canvas_board = Canvas(secondary_window, width=600, height=350)
                canvas_board.configure(bg='#ffffff')
                canvas_board.pack(fill="both", expand=True)
                
                # Create a ScrolledText widget to display the meaning
                text_area = st.ScrolledText(canvas_board, width=30, fg='#582308', bg="#f5b98c", height=8, font=("Bookman Old Style", 20))
                text_area.grid(column=0, pady=10, padx=10)
                
                # Insert the meaning text into the widget and make it read-only
                text_area.insert(INSERT, strip_word)
                text_area.configure(state='disabled')

        # Create the game window when the main window is minimized
        # Create a canvas to hold the game elements
        game_canvas = Canvas(game_window, width=889, height=500)
        game_canvas.pack(fill="both", expand=True)
        game_canvas.create_image(0, 0, image=gamebackground, anchor="nw")
        
        # Create a Tkinter Entry widget for the user to input a word
        my_entry_box = Entry(game_canvas, borderwidth=0, show="•", width=14,fg='#d6bda9', bg="#825e3e",font=('Bookman Old Style', 38))
        my_tk_label = Label(game_canvas, borderwidth=0, relief="ridge",
                        width=15,fg='#d6bda9',bg="#825e3e", font=('Bookman Old Style', 37))
        answer_entry = Entry(game_canvas, borderwidth=0,bg="#825e3e", width=14,fg='#d6bda9',
                            font=('Bookman Old Style', 38))
        
        # Create buttons for the user to shuffle the word and check their answer
        shuffle_button = Button(game_canvas, borderwidth=0, image=play_btn, bg='#825e3e', height=61, width=61, command=shuffle_word)
        check_button = Button(game_canvas, borderwidth=0, image=check_btn,bg='#825e3e', height=61, width=61, command=check_input_value)
        meaning_button = Button(game_canvas, borderwidth=0,image=search_btn,bg='#825e3e', height=61, width=61, command=show_meaning)
        
        # Place the widgets on the canvas
        my_entry_box.place(x=214, y=62)
        my_tk_label.place(x=215, y=184)
        answer_entry.place(x=214, y=312)
        shuffle_button.place(x=622, y=62)
        check_button.place(x=622, y=312)
        meaning_button.place(x=560, y=312)
        root.iconify()
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
    # print("Loaded model from disk")

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
                frameX, frameY, frameWidth, FrameHeight = 0, 0, 220, 30

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

                cv2.rectangle(frame, (10, 10), (10 + frameWidth, 10 + FrameHeight), (97,107,255), -1)
                cv2.circle(frame, (224, 25), 16, (97,107,255), -2)
                cv2.rectangle(frame, (10, 42), (10 + frameWidth, 42 + FrameHeight), (144,238,144), -1)
                cv2.circle(frame, (224, 57), 16, (144,238,144), -2)
                cv2.rectangle(frame, (10, 74), (10 + frameWidth, 74 + FrameHeight), (230,211,139), -1)
                cv2.circle(frame, (224, 89), 16, (230,211,139), -2)
                # Show the data of the emotion here
                cv2.putText(frame, "Number of Students: " + str(countFaces), (12, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                cv2.putText(frame, "Number of Smiling: " + str(numberOfHappyFace), (12, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                cv2.putText(frame, "Positive Emotion: " + f'{percentageOfEmotion:0.1f}%', (12, 95),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            if (initialize == True and percentageOfNegativeEmtn == 100) and percentageOfEmotion == 0:
                noExistenceOfEmtn += 1
                # counting += 1
                # print(delayervalue)
                if noExistenceOfEmtn == delayer_value:
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
                        root.iconify()
                        messagebox.showinfo(
                            'Return', 'You will now return to the application screen')
            elif initialize == True and percentageOfEmotion <= PERCENTAGEOFPSTEMTN:
                existenceOfEmtn += 1
                # print(delayervalue)
                if existenceOfEmtn == delayer_value:
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
infoButton = Button(canvas1, borderwidth=0, image=information_btn,  command=info_btn)
infoButton.place(x=380, y=251)
drop = OptionMenu( canvas1 , clicked , *options, command=show)
drop.place(x=202, y=200)
drop.config(width = 15, font=('Century Gothic', 15, 'bold'))
# button = Button(canvas1, image=submit, borderwidth=0, command=show)
# button.place(x=160, y=2)
root.mainloop()
