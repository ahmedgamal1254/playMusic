# project to play music in folder by random
# user can use determine folder
# program automatic get music inside array and play in array it
import os
import random as rand

class musicPorgram:
    myFolder=''

    def __init__(self,folder):
        self.myFolder=folder

    def check_folder(self):
        list = self.myFolder.split('\\')
        rslt, s = list[0:len(list) - 1], ''
        for i in range(len(rslt)):
            if i != len(rslt) - 1:
                s += rslt[i]
            else:
                s += "\\" + rslt[i]
        os.chdir(f"{s}")
        newfolder=list[-1]
        if " " in list[-1]:
            newfolder = list[-1].replace(" ", "_")
            os.system(f'rename "{list[-1]}" "{newfolder}"')
        return newfolder

    def getFolder(self):
        return self.check_folder()

    def getMusic(self):
        rslt = self.getFolder()
        arr=os.listdir(rslt)
        return arr

    def randomMusic(self):
        random=rand.choice(self.getMusic())
        os.system(f'start {self.getFolder()}\\"{random}"')

    def getDirectory(self):
        return os.getcwd()
play=musicPorgram(input("enter path folder :- "))
while True:
    val=input("press enter to change music :- ")
    if val != 'exit':
        play.randomMusic()
    else:
        break