FILEPATH = "todo.txt"

def printTodos(todos):
    """
    Print out the todo list.
    Return None
    """
    newTodos = [f"{index1+1} - {item1.strip('\n')}" for index1,item1 in enumerate(todos)]
    print(newTodos)

def saveTodos(content, filepath = FILEPATH):
    with open(filepath,'w') as file:
        file.writelines(content)
    
def loadTodos(filepath = FILEPATH):
    with open(filepath,'r') as file:
        content = file.readlines()
    return content

if __name__ == "__main__":
    todos = loadTodos()
    printTodos(todos)