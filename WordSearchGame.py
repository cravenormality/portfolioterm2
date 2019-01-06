#Dominic Santistevan & Jessica Weinburger
#Question list, their corresponding answers, and a score
import random
questionList = ["If within another if statement","Checks for a character wihtin a string",
                "Another option within an if statement","How you end an if statement",
                "Data type for a number", "What the user enters",
                "Displays a string","The value after an operation",
                "A value that is passed to a method when it is invoked",
                "A variable defined by a method that receives a value when the method is called",
                "Can be assigned a value","An error type when something isn't defined",
                "Examples: For & While","Examples are characters, ints, & floats",
                "Characters put together","Used to check conditions",
                "Used to create code comments","Splits indexes",
                "Position within an ordered list","A block of code"]
answerList = ["nested","instatement","elif","else",
              "int","input","print","returnvalue",
              "arguments","parameters",
              "variables","nameerror","loop",
              "datatype","strings","ifstatement","poundsign",
              "slicing","index","function"]
score = 0
puzzle = ("geyiwkiaahgvxrrldksadplntdildmasjepopewrxzmsvsbdxdtptfkogdra"
              "nwxteqpeeriuouipsuhgrauaytkgitroanmthgocoumtddpnnnsretemarap"
              "vwfennguvgtegikjosljibemrsvapieknosxtqidwfiecrlswshpknenmotf"
              "jmsnruottdzubdetzecikspteynrnnvgnmhtlgpzndfvapifiumiuutpnfzl"
              "hzomhtyzrorggnicilsuusdvwfetpprttpolynmzshgphrxmtaieumcqmtpj"
              "tnizepsceaxtscfetekfqhfqxxkdgntmwmkuluhmhmzjaiujywtvariables"
              "inputgyokvvldqfthkqgxvytcaewnaswctlevbhm")


#Main function
def main():
    print("Welcome to the trivia, word search game!")
    while len(questionList) > 0:
        answer = question(questionList, answerList)
        findWord(answer,puzzle)
    print("Congratulations")

#Chooses a question and its corresponding answer
def question(questionList, answerList):
    global score
    attempts = 10
    print("Enter your answer in all lowercase and no spaces")

    #Chooses a random question then finds its corresponding answer
    x = random.randrange(len(questionList))
    question = questionList[x]
    answer = answerList[x]

    #Creates a loop for the player if the answer is incorrect
    while True:
        response = input(question)

        #Checks to see if the input is the correct answer
        #If correct, it deletes the answer & question
        if response == answer:
            score = score + attempts*10
            print("Correct")
            del questionList[x]
            del answerList[x]
            return answer

        #If it's incorrect it loops
        else:
            attempts -= 1
            print("Wrong, try again")
            


def findWord(answer,puzzle):
    wordSearch(puzzle)

    #Asks & gets index positions
   
    while True:
        p = input("Enter in the locations of the word")
        ip = ""
        bw = ""
        for i in p:

            #Looks for a comma for index seperation &
            #To build word
            if i == ",":
                x = int(ip)
                bw = bw + puzzle[x]
                ip = ""

            else:
                ip += i
        if bw == answer:
            print("Correct")
            break
        else:
            print("Wrong, try again")
    
#Sets up the how the word search will look
def wordSearch(puzzle):
    
    line1="|"
    line2="|"
    line3="|"
    line4="|"
    line5="|"
    line6="|"
    line7="|"
    line8="|"
    line9="|"
    line10="|"
    for i in range(len(puzzle)):
        if i<=19:
            line1 = line1 + puzzle[i]+"|"
        elif i<=39:
            line2 = line2 + puzzle[i]+"|"
        elif i<=59:
            line3 = line3 + puzzle[i]+"|"
        elif i<=79:
            line4 = line4 + puzzle[i]+"|"
        elif i<=99:
            line5 = line5 + puzzle[i]+"|"
        elif i<=119:
            line6 = line6 + puzzle[i]+"|"
        elif i<=139:
            line7 = line7 + puzzle[i]+"|"
        elif i<=159:
            line8 = line8 + puzzle[i]+"|"
        elif i<=179:
            line9 = line9 + puzzle[i]+"|"
        elif i<=199:
            line10 = line10 + puzzle[i]+"|"
    print("_________________________________________")
    print(line1)
    print("-----------------------------------------")
    print(line2)
    print("-----------------------------------------")
    print(line3)
    print("-----------------------------------------")
    print(line4)
    print("-----------------------------------------")
    print(line5)
    print("-----------------------------------------")
    print(line6)
    print("-----------------------------------------")
    print(line7)
    print("-----------------------------------------")
    print(line8)
    print("-----------------------------------------")
    print(line9)
    print("-----------------------------------------")
    print(line10)
    print("-----------------------------------------")

main()

