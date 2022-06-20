from tkinter import Button, PhotoImage, Tk, Canvas
from tkinter.constants import NW
import random

pause = False  # Pause default


def left(event):
    # Stops circle from leaving the window
    circlePosition = canvas.coords(circle)
    if circlePosition[0] < 1:
        canvas.move(circle, 0, 0)
    else:
        canvas.move(circle, -10, 0)


def right(event):
    circlePosition = canvas.coords(circle)
    if circlePosition[2] > 1599:
        canvas.move(circle, 0, 0)
    else:
        canvas.move(circle, 10, 0)


def quit(event):  # quits game to home page
    global pause
    pause = True
    canvas.delete("all")
    home()


def cheat(event):  # Increments score by 10
    canvas.pack()
    global score
    score += 10
    txt = "score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)


def bosskeyReturnNormal(event):  # Opens main game
    global pause
    pause = False
    NormalGameWindow()


def bossKeyNormal(event):  # closes main game and opens fake terminal image
    global pause
    global terminalImage
    pause = True
    canvas.delete("all")
    window.title("Terminal")
    terminalImage = PhotoImage(
        file="/home/csimage/16321_python_coursework_c43480ct/BossKey.png")
    canvas.create_image(0, 0, anchor=NW, image=terminalImage)
    window.bind("<b>", bosskeyReturnNormal)


def bosskeyReturnHard(event):  # Opens main game
    global pause
    pause = False
    hardGameWindow()


def bossKeyHard(event):
    global pause
    global terminalImage
    pause = True
    canvas.delete("all")
    window.title("Terminal")
    terminalImage = PhotoImage(
        file="/home/csimage/16321_python_coursework_c43480ct/BossKey.png")
    canvas.create_image(0, 0, anchor=NW, image=terminalImage)
    window.bind("<b>", bosskeyReturnHard)


def bosskeyReturnImpossible(event):
    global pause
    pause = False
    impossibleGameWindow()


def bossKeyImpossible(event):
    global pause
    global terminalImage
    pause = True
    canvas.delete("all")
    window.title("Terminal")
    terminalImage = PhotoImage(
        file="/home/csimage/16321_python_coursework_c43480ct/BossKey.png")
    canvas.create_image(0, 0, anchor=NW, image=terminalImage)
    window.bind("<b>", bosskeyReturnImpossible)


def restartNormal(event):  # restarts game
    canvas.delete("all")
    NormalGameWindow()


def restartHard(event):
    canvas.delete("all")
    hardGameWindow()


def restartImpossible(event):
    canvas.delete("all")
    impossibleGameWindow()


def pauseGame(event):  # Pauses game
    global pause
    if not pause:
        pause = True
    else:
        pause = False


def gameOver1():  # Displays text if square makes contact with circle.
    global square1
    global circle
    global pause
    squarePosition = canvas.coords(square1)
    circlePosition = canvas.coords(circle)
    if squarePosition[0] < circlePosition[2] and squarePosition[2] > circlePosition[
            0] and squarePosition[1] < circlePosition[3] and squarePosition[3] > circlePosition[1]:
        pause = True
        canvas.create_text(
            canvasCenter,
            text="You lost",
            fill="red",
            font=(
                "Arial Bold",
                25))
    window.after(20, gameOver1)


def gameOver2():
    global square2
    global circle
    global pause
    squarePosition = canvas.coords(square2)
    circlePosition = canvas.coords(circle)
    if squarePosition[0] < circlePosition[2] and squarePosition[2] > circlePosition[
            0] and squarePosition[1] < circlePosition[3] and squarePosition[3] > circlePosition[1]:
        pause = True
        canvas.create_text(
            canvasCenter,
            text="You lost",
            fill="red",
            font=(
                "Arial Bold",
                25))
    window.after(20, gameOver2)


def gameOver3():
    global square3
    global circle
    global pause
    squarePosition = canvas.coords(square3)
    circlePosition = canvas.coords(circle)
    if squarePosition[0] < circlePosition[2] and squarePosition[2] > circlePosition[
            0] and squarePosition[1] < circlePosition[3] and squarePosition[3] > circlePosition[1]:
        pause = True
        canvas.create_text(
            canvasCenter,
            text="You lost",
            fill="red",
            font=(
                "Arial Bold",
                25))
    window.after(20, gameOver3)


def gameOver4():
    global square2
    global circle
    global pause
    squarePosition = canvas.coords(square4)
    circlePosition = canvas.coords(circle)
    if squarePosition[0] < circlePosition[2] and squarePosition[2] > circlePosition[
            0] and squarePosition[1] < circlePosition[3] and squarePosition[3] > circlePosition[1]:
        pause = True
        canvas.create_text(
            canvasCenter,
            text="You lost",
            fill="red",
            font=(
                "Arial Bold",
                25))
    window.after(20, gameOver4)


def scoreboard():  # updates score by 1
    canvas.pack()
    global score
    score += 1
    txt = "score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)


def moveSquare1(squareY1):  # moves square down at random speed from 3-6
    global randSpeed1
    randSpeed1 = random.randint(3, 6)
    if not pause:
        canvas.move(square1, 0, randSpeed1)
        squareY1 += randSpeed1
        if squareY1 > 1060:
            scoreboard()
            canvas.delete(square1)
            generateSquare1()
            return
    else:
        canvas.move(square1, 0, 0)
    window.after(20, moveSquare1, squareY1)


def moveSquare2(squareY2):
    global randSpeed2
    randSpeed2 = random.randint(3, 6)
    if not pause:
        canvas.move(square2, 0, randSpeed2)
        squareY2 += randSpeed2
        if squareY2 > 1060:
            scoreboard()
            canvas.delete(square2)
            generateSquare2()
            return
    else:
        canvas.move(square1, 0, 0)
    window.after(20, moveSquare2, squareY2)


def moveSquare3(squareY3):
    global randSpeed3
    randSpeed3 = random.randint(3, 6)
    if not pause:
        canvas.move(square3, 0, randSpeed3)
        squareY3 += randSpeed3
        if squareY3 > 1060:
            scoreboard()
            canvas.delete(square3)
            generateSquare3()
            return
    else:
        canvas.move(square1, 0, 0)
    window.after(20, moveSquare3, squareY3)


def moveSquare4(squareY4):
    global randSpeed4
    randSpeed4 = random.randint(3, 6)
    if not pause:
        canvas.move(square4, 0, randSpeed4)
        squareY4 += randSpeed4
        if squareY4 > 1060:
            scoreboard()
            canvas.delete(square4)
            generateSquare4()
            return
    else:
        canvas.move(square1, 0, 0)
    window.after(20, moveSquare4, squareY4)


def generateSquare1():  # creates square
    canvas.pack()
    global square1, squareX1, squareY1
    squareX1 = random.randint(0, 240)
    squareY1 = 160
    squareXY1 = (squareX1, 0, squareX1 + 160, squareY1)
    square1 = canvas.create_rectangle(squareXY1, fill="red")
    moveSquare1(squareY1)


def generateSquare2():
    canvas.pack()
    global square2, squareX2, squareY2
    squareX2 = random.randint(400, 640)
    squareY2 = 160
    squareXY2 = (squareX2, 0, squareX2 + 160, squareY2)
    square2 = canvas.create_rectangle(squareXY2, fill="red")
    moveSquare2(squareY2)


def generateSquare3():
    canvas.pack()
    global square3, squareX3, squareY3
    squareX3 = random.randint(800, 1040)
    squareY3 = 160
    squareXY3 = (squareX3, 0, squareX3 + 160, squareY3)
    square3 = canvas.create_rectangle(squareXY3, fill="red")
    moveSquare3(squareY3)


def generateSquare4():
    canvas.pack()
    global square4, squareX4, squareY4
    squareX4 = random.randint(1280, 1440)
    squareY4 = 160
    squareXY4 = (squareX4, 0, squareX4 + 160, squareY4)
    square4 = canvas.create_rectangle(squareXY4, fill="red")
    moveSquare4(squareY4)


def moveSquare1Hard(squareY1):  # moves square down at random speed from 4-7
    global randSpeed1
    randSpeed1 = random.randint(4, 7)
    if not pause:
        canvas.move(square1, 0, randSpeed1)
        squareY1 += randSpeed1
        if squareY1 > 1060:
            scoreboard()
            canvas.delete(square1)
            generateSquare1Hard()
            return
    else:
        canvas.move(square1, 0, 0)
    window.after(20, moveSquare1Hard, squareY1)


def moveSquare2Hard(squareY2):
    global randSpeed2
    randSpeed2 = random.randint(4, 7)
    if not pause:
        canvas.move(square2, 0, randSpeed2)
        squareY2 += randSpeed2
        if squareY2 > 1060:
            scoreboard()
            canvas.delete(square2)
            generateSquare2Hard()
            return
    else:
        canvas.move(square1, 0, 0)
    window.after(20, moveSquare2Hard, squareY2)


def moveSquare3Hard(squareY3):
    global randSpeed3
    randSpeed3 = random.randint(4, 7)
    if not pause:
        canvas.move(square3, 0, randSpeed3)
        squareY3 += randSpeed3
        if squareY3 > 1060:
            scoreboard()
            canvas.delete(square3)
            generateSquare3Hard()
            return
    else:
        canvas.move(square1, 0, 0)
    window.after(20, moveSquare3Hard, squareY3)


def moveSquare4Hard(squareY4):
    global randSpeed4
    randSpeed4 = random.randint(4, 7)
    if not pause:
        canvas.move(square4, 0, randSpeed4)
        squareY4 += randSpeed4
        if squareY4 > 1060:
            scoreboard()
            canvas.delete(square4)
            generateSquare4Hard()
            return
    else:
        canvas.move(square1, 0, 0)
    window.after(20, moveSquare4Hard, squareY4)


def generateSquare1Hard():  # creates square
    canvas.pack()
    global square1, squareX1, squareY1
    squareX1 = random.randint(0, 240)
    squareY1 = 160
    squareXY1 = (squareX1, 0, squareX1 + 160, squareY1)
    square1 = canvas.create_rectangle(squareXY1, fill="#bfbfb0", outline="")
    moveSquare1Hard(squareY1)


def generateSquare2Hard():
    canvas.pack()
    global square2, squareX2, squareY2
    squareX2 = random.randint(400, 640)
    squareY2 = 160
    squareXY2 = (squareX2, 0, squareX2 + 160, squareY2)
    square2 = canvas.create_rectangle(squareXY2, fill="#bfbfb0", outline="")
    moveSquare2Hard(squareY2)


def generateSquare3Hard():
    canvas.pack()
    global square3, squareX3, squareY3
    squareX3 = random.randint(800, 1040)
    squareY3 = 160
    squareXY3 = (squareX3, 0, squareX3 + 160, squareY3)
    square3 = canvas.create_rectangle(squareXY3, fill="#bfbfb6", outline="")
    moveSquare3Hard(squareY3)


def generateSquare4Hard():
    canvas.pack()
    global square4, squareX4, squareY4
    squareX4 = random.randint(1280, 1440)
    squareY4 = 160
    squareXY4 = (squareX4, 0, squareX4 + 160, squareY4)
    square4 = canvas.create_rectangle(squareXY4, fill="#bfbfb0", outline="")
    moveSquare4Hard(squareY4)


# moves square down at random speed from 4-7
def moveSquare1Impossible(squareY1):
    global randSpeed1
    randSpeed1 = random.randint(4, 7)
    if not pause:
        canvas.move(square1, 0, randSpeed1)
        squareY1 += randSpeed1
        if squareY1 > 1060:
            scoreboard()
            canvas.delete(square1)
            generateSquare1Impossible()
            return
    else:
        canvas.move(square1, 0, 0)
    window.after(20, moveSquare1Impossible, squareY1)


def moveSquare2Impossible(squareY2):
    global randSpeed2
    randSpeed2 = random.randint(4, 7)
    if not pause:
        canvas.move(square2, 0, randSpeed2)
        squareY2 += randSpeed2
        if squareY2 > 1060:
            scoreboard()
            canvas.delete(square2)
            generateSquare2Impossible()
            return
    else:
        canvas.move(square1, 0, 0)
    window.after(20, moveSquare2Impossible, squareY2)


def moveSquare3Impossible(squareY3):
    global randSpeed3
    randSpeed3 = random.randint(4, 7)
    if not pause:
        canvas.move(square3, 0, randSpeed3)
        squareY3 += randSpeed3
        if squareY3 > 1060:
            scoreboard()
            canvas.delete(square3)
            generateSquare3Impossible()
            return
    else:
        canvas.move(square1, 0, 0)
    window.after(20, moveSquare3Impossible, squareY3)


def moveSquare4Impossible(squareY4):
    global randSpeed4
    randSpeed4 = random.randint(4, 7)
    if not pause:
        canvas.move(square4, 0, randSpeed4)
        squareY4 += randSpeed4
        if squareY4 > 1060:
            scoreboard()
            canvas.delete(square4)
            generateSquare4Impossible()
            return
    else:
        canvas.move(square1, 0, 0)
    window.after(20, moveSquare4Impossible, squareY4)


def generateSquare1Impossible():  # creates square
    canvas.pack()
    global square1, squareX1, squareY1
    squareX1 = random.randint(0, 240)
    squareY1 = 160
    squareXY1 = (squareX1, 0, squareX1 + 160, squareY1)
    square1 = canvas.create_rectangle(squareXY1, fill="#bfbfb6", outline="")
    moveSquare1Impossible(squareY1)


def generateSquare2Impossible():
    canvas.pack()
    global square2, squareX2, squareY2
    squareX2 = random.randint(400, 640)
    squareY2 = 160
    squareXY2 = (squareX2, 0, squareX2 + 160, squareY2)
    square2 = canvas.create_rectangle(squareXY2, fill="#bfbfb6", outline="")
    moveSquare2Impossible(squareY2)


def generateSquare3Impossible():
    canvas.pack()
    global square3, squareX3, squareY3
    squareX3 = random.randint(800, 1040)
    squareY3 = 160
    squareXY3 = (squareX3, 0, squareX3 + 160, squareY3)
    square3 = canvas.create_rectangle(squareXY3, fill="#bfbfb6", outline="")
    moveSquare3Impossible(squareY3)


def generateSquare4Impossible():
    canvas.pack()
    global square4, squareX4, squareY4
    squareX4 = random.randint(1280, 1440)
    squareY4 = 160
    squareXY4 = (squareX4, 0, squareX4 + 160, squareY4)
    square4 = canvas.create_rectangle(squareXY4, fill="#bfbfb6", outline="")
    moveSquare4Impossible(squareY4)


def NormalGameWindow():  # creates normal difficulty game
    global circle
    global score
    global scoreText
    global pause

    pause = False

    canvas.delete("all")
    window.title("Escape The Blocks")

    score = -1

    txt = "Score:" + str(score)
    scoreText = canvas.create_text(
        800,
        10,
        text="Score: " +
        str(score),
        fill="green",
        font=(
            "Arial Bold",
            15))

    circleXY = (720, 735, 880, 895)
    circle = canvas.create_oval(circleXY, fill="#03a5fc")

    generateSquare1()
    generateSquare2()
    generateSquare3()
    generateSquare4()
    gameOver1()
    gameOver2()
    gameOver3()
    gameOver4()
    scoreboard()

    window.bind("<Left>", left)

    window.bind("<Right>", right)

    window.bind("<Escape>", quit)

    window.bind("<u>", cheat)

    window.bind("<space>", pauseGame)

    window.bind("<b>", bossKeyNormal)

    window.bind("<r>", restartNormal)


def hardGameWindow():  # creates hard difficulty game
    global circle
    global score
    global scoreText
    global pause

    pause = False

    canvas.delete("all")
    window.title("Escape The Blocks")

    score = -1

    txt = "Score:" + str(score)
    scoreText = canvas.create_text(
        800,
        10,
        text="Score: " +
        str(score),
        fill="green",
        font=(
            "Arial Bold",
            15))

    circleXY = (720, 735, 880, 895)
    circle = canvas.create_oval(circleXY, fill="#03a5fc")

    generateSquare1Hard()
    generateSquare2Hard()
    generateSquare3Hard()
    generateSquare4Hard()
    gameOver1()
    gameOver2()
    gameOver3()
    gameOver4()
    scoreboard()

    window.bind("<Left>", left)

    window.bind("<Right>", right)

    window.bind("<Escape>", quit)

    window.bind("<u>", cheat)

    window.bind("<space>", pauseGame)

    window.bind("<b>", bossKeyHard)

    window.bind("<r>", restartHard)


def impossibleGameWindow():  # creates impossible difficulty game
    global circle
    global score
    global scoreText
    global pause

    pause = False

    canvas.delete("all")
    window.title("Escape The Blocks")

    score = -1

    txt = "Score:" + str(score)
    scoreText = canvas.create_text(
        800,
        10,
        text="Score: " +
        str(score),
        fill="green",
        font=(
            "Arial Bold",
            15))

    circleXY = (720, 735, 880, 895)
    circle = canvas.create_oval(circleXY, fill="#bfbfb6", outline="")

    generateSquare1Impossible()
    generateSquare2Impossible()
    generateSquare3Impossible()
    generateSquare4Impossible()
    gameOver1()
    gameOver2()
    gameOver3()
    gameOver4()
    scoreboard()

    window.bind("<Left>", left)

    window.bind("<Right>", right)

    window.bind("<Escape>", quit)

    window.bind("<u>", cheat)

    window.bind("<space>", pauseGame)

    window.bind("<b>", bossKeyImpossible)

    window.bind("<r>", restartImpossible)


def selectDifficulty():  # Opens window to select game difficulty
    canvas.delete("all")
    window.title("Controls")
    canvas.create_text(800, 50, fill="black", font=(
        "Arial Bold", 60), text="Select Difficulty")

    normalDifficulty = Button(
        window,
        text="Normal",
        command=NormalGameWindow,
        background="red",
        fg="black",
        width=30,
        height=10)
    normalDifficulty = canvas.create_window(
        270, 450, anchor=NW, window=normalDifficulty)
    canvas.create_oval(320, 720, 480, 880, fill="#03a5fc")

    hardDifficulty = Button(
        window,
        text="Hard",
        command=hardGameWindow,
        background="#bfbfb0",
        fg="black",
        highlightthickness=0,
        bd=0,
        width=30,
        height=10)
    hardDifficulty = canvas.create_window(
        670, 450, anchor=NW, window=hardDifficulty)
    canvas.create_oval(720, 720, 880, 880, fill="#03a5fc")

    impossibleDifficulty = Button(
        window,
        text="Impossible",
        command=impossibleGameWindow,
        background="#bfbfb6",
        fg="black",
        highlightthickness=0,
        bd=0,
        width=30,
        height=10)
    impossibleDifficulty = canvas.create_window(
        1070, 450, anchor=NW, window=impossibleDifficulty)
    canvas.create_oval(1120, 720, 1280, 880, fill="#bfbfb6", outline="")


def controlsInfo():  # Displays window with controls
    canvas.delete("all")
    window.title("Controls")
    canvas.create_text(
        800, 50, fill="black", font=(
            "Arial Bold", 60), text="Controls")
    canvas.create_text(
        300,
        500,
        fill="black",
        font=(
            "Arial Bold",
            30),
        text="Move left: Left arrow key\nMove right: Right arrow key\nPause: Space bar\nBoss Key: 'b'\nIncrease score by 10: 'u'\nRestart: 'r'\nClose game: 'Esc'")
    controlsInfoButton = Button(
        window,
        text="Back",
        command=home,
        background="white",
        fg="green")
    controlsInfoButton = canvas.create_window(
        793, 783, anchor=NW, window=controlsInfoButton)


global window

cavnasWidth = 1600
canvasHeight = 900
canvasCenter = cavnasWidth / 2, canvasHeight / 2
window = Tk()
window.title("Escape The Blocks")
canvas = Canvas(window, bg="#bfbfbd", width=cavnasWidth, height=canvasHeight)
canvas.delete("all")


def home():  # Creates home window
    global wallpaper
    global canvas

    wallpaper = PhotoImage(
        file="/home/csimage/16321_python_coursework_c43480ct/EscapeTheBlocks.png")
    canvas.create_image(0, 0, anchor=NW, image=wallpaper)
    controlsInfoButton = Button(
        window,
        text="Learn Controls",
        command=controlsInfo,
        background="white",
        fg="green")
    controlsInfoButton = canvas.create_window(
        30, 785, anchor=NW, window=controlsInfoButton)

    playButton = Button(
        window,
        text="Play!",
        command=selectDifficulty,
        background="white",
        fg="green")
    playButton = canvas.create_window(793, 783, anchor=NW, window=playButton)


home()

canvas.pack()
window.mainloop()
