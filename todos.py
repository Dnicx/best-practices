# import re

listFile = "todos.txt"

def printList():
    tlist = []
    print("To do list:")
    counter = 0
    try:
        with open(listFile, "r") as f:
            for line in f:
                tlist.append(line)
                counter = counter+1;
                print(str(counter) + ' ' + line, end='')
    except IOError:
        print("No todo list yet")
        with open(listFile, "w") as f:
            f.write('')
        
    return tlist, counter

def addTodo():
    _, counter = printList()
    with open(listFile, "a") as f:
        print(str(counter+1) + " ", end='')
        line = input()
        while line != '':
            counter += 1
            print(str(counter+1) + " ", end='')
            f.write(line+"\n")
            line = input()
    printList()

def markAsDone():
    tlist, counter = printList()
    print("task: ", end='')
    num = input()
    with open(listFile, "w") as f:
        for i in range(counter):
            if str(i+1) != num:
                f.write(tlist[i])
    printList()


print("Welcome to pydo:")
print("select command:")
print("add : add item to todo")
print("done : mark item as done and remove from list")
print("quit : to exit program")

print("enter command: ", end='')
cm = input()
while (cm != 'quit'):
    if cm == 'add':
        addTodo()
    elif cm == 'done':
        markAsDone()
    elif cm == 'list':
        printList()
    else:
        print("command not found")
    print("enter command: ", end='')
    cm = input()




    
