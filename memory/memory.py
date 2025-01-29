def main():
    history = []#history is a list

    while True:
        action = input('Action: ')#action = what is typed
        print(history)#print what is stored in the list so far

        if action == 'Undo':
            undone = history.pop()#undone = using the pop function to remove the last from the history list
            print(f'Undone: {undone}')#print confirming what was undone
        elif action == 'Restart':
            history.clear()#clear all history if Restart is typed
        else:
            history.append(action)
        if action =='End':
            break#if End if typed break the True loop 


            

main()