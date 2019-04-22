import redis

listFile = "todos.txt"
red = redis.Redis(host='localhost', port=6379, db=0)

dic = ''

try:
    dic = red.get('keys')
    dic = dic.decode("utf-8")
    # print("successfully retrive dict")
except:
    # print("dict not found")
    dic = '0'
    red.set('keys', dic)
klist = dic.split(" ")
# print(dic)

def printList():
    
    tlist = []
    print("To do list:")
    counter = 0
    print('klist is ' ,end='')
    print(klist)
    try:
        if len(klist) <= 0: 
            return [], 0
        for i in klist :
            if i == '' or int(i) < 1:
                continue
            counter = counter+1
            print(str(counter) + ' ' + red.get(i).decode('utf-8'))
    except IOError:
        print("No todo list yet")
        with open(listFile, "w") as f:
            f.write('')
    return tlist, counter

def addTodo():
    _, counter = printList()
    
    print(str(counter+1) + " ", end='')
    line = input()
    while line != '':
        counter += 1
        print(str(counter+1) + " ", end='')
        red.set(str(int(klist[-1])+1), line)
        global dic 
        dic = dic + ' ' + str(int(klist[-1]) +1)
        klist.append(str(int(klist[-1])+1))
        print(dic)
        red.set('keys', dic)
        line = input()

    printList()

def markAsDone():
    tlist, counter = printList()
    print("task: ", end='')
    num = int(input())
    if (num < 1 or num > counter):
        print("item not found")
        return
    red.delete(str(klist[num]))
    klist.pop(num)
    dic = ''
    for item in klist:
        dic += str(item)
    red.set('keys', dic)
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
        print()
    else:
        print("command not found")
    print("enter command: ", end='')
    cm = input()