print("Wellcome to Text Editor")
print("-----------------------")

"""
mode: character_count, word_count
"""

textInput = input("Text: ")

def textEditor(text, mode = "character_count"):

    if mode == "character_count":
        print("Character count is {}".format(len(textInput)))
    if mode == "word_count":
        print("Word count is {}".format(len(textInput.split(" "))))

textEditor(text=textInput, mode="word_count")