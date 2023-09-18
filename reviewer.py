#!/usr/bin/python
import yaml as yml
import os

# Semi Globals
file = None
chapters = None
questions = None
answers = None
fileIsOpen = False


def getFilesInThisDirectory():
    validFiles = [x for x in os.listdir() if os.path.splitext(x)[1] == ".yml"]
    print(validFiles)
    return validFiles

def openReviewFile():
    fileName = input("")


def createReviewFile():
    fileName = True
    while fileName is True:
        fileName = \
                input("Enter the name of your file that you wish to create:\
                (Enter nothing to go back)")
        if fileName == '':
            return
        # create file with read write permissions
        try:
            file = open(fileName, 'x')
        except FileExistsError:
            print(fileName, "- That exists, please specify a different name.")
            fileName = True
        except IOError:
            print(fileName, "- Dont have access to this...")
            fileName = True 


def loadReviewFile():
    validFiles = getFilesInThisDirectory()
    if len(validFiles) == 0:
        print("I couldnt find any valid '.yml' files here...")
        return False

    print("I only read from the current directory, here is what I could find:")
    [print(file) for file in validFiles]
    while fileName is True:
        fileName = \
                input("Select a file:\
                (Enter nothing to go back)")
        if fileName == '':
            return
        if not os.path.exists(fileName):
            print(fileName, "Dont have that...")
            fileName = True
    
    # load the yml file
    ymlFile = yml.safe_load(file)

    # load main keys, in this case they are the chapters
    chapters = [x for x in ymlFile]

    # load the questions from the chapter
    questions = [q for q in chapters['Questions']]

    # load the answers from the chapter
    answers = [a for a in chapters['Answers']]
 

    return open(fileName, 'rw')



def addQuestion(chapterName: str, questionText: str, answerText: str, questionBank: dict):
    pass


def prompt():
    valid = 0
    if fileIsOpen:
        print("""
          Welcome to the Review.
          Select an option below to get started.
          1. Open existing review
          2. Create new review
          3. Quit
          """)
        valid = (1, 2, 3)
    else:
        print("""
          Welcome to the Review.
          Select an option below to get started.
          1. Open existing review
          2. Create new review
          3. Start Review
          4. Quit
          """)
        valid = (1, 2, 3, 4)
    choice = input()
    return int(choice) in valid 





   


    
    

