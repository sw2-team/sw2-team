import pickle

dbfilename = 'assignment3.dat'
print('--------------------Score Manager--------------------')
def readScoreDB():
    try:
        fh = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print('New DB: ', dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fh)
    except:
        print('Empty DB: ', dbfilename)
    else:
        print('Open DB: ', dbfilename)
    for record in scdb:                  #Age와 Score을 정수형으로 받는 부분
        for t in record:                 #
            if t == 'Name':              #
                continue                 #
            record[t] = int(record[t])   #
    fh.close()
    return scdb

def writeScoreDB(scdb):
    fh = open(dbfilename, 'wb')
    pickle.dump(scdb, fh)
    fh.close()

def doScoreDB(scdb):
    while(True):
        inputstr = input('Score DB >>> ')
        if inputstr == '':
            continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            if len(parse) != 4:                                           #예외(에러)처리 부분
                print('There are not enough arguments to "add command".') #
                continue
            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
            scdb += [record]
        elif parse[0] == 'command':
            command_manual()
        elif parse[0] == 'find':
            for p in scdb:
                if p['Name'] == parse[1]:
                    person_name = [p]
                    findScoreDB(person_name)
                    break
            if not parse[1] in p['Name']:                      # 예외(에러)처리 부분
                print("'"+parse[1]+"'", 'is not name in list.')#
                print('Please add to the list')                #
        elif parse[0] == 'inc':
            for p in scdb:
                if p['Name'] == parse[1]:
                    p['Score'] += int(parse[2])
                    break
            if not parse[1] in p['Name']:                      #예외(에러)처리 부분
                print("'"+parse[1]+"'", 'is not name in list.')#
                print('Please add to the list')                #
        elif parse[0] == 'del':
            for p in scdb:
                if p['Name'] == parse[1]:
                    scdb.remove(p)
                    print('delete', "'"+parse[1]+"'")
            if not parse[1] in p['Name']:                      #예외(에러)처리 부분
                print("'"+parse[1]+"'", 'is not name in list.')#
        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif (parse[0] == 'quit') or (parse[0] == 'exit'):
            break
        else:
            print('Invalid command: ' + parse[0])

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + '=' + str(p[attr]), end=' ')
        print()

def findScoreDB(pname):
    for p in pname:
        for attr in sorted(p):
            print(attr + '=' + str(p[attr]), end=' ')
        print()

def command_manual():
    print('add: "add + Name + Age + Score"')
    print('find: "find + Name"')
    print('increase: "inc + Name + Amount"')
    print('delete: "del + Name"')
    print('show: "show + SoretingKey(Can be omitted)"')
    print('exit: "quit OR exit"')


print('If you want a manual, type the following command: "command"')
scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
