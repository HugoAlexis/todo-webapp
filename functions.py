
TODOS_FILE = './todos.txt'


def load_todos_data(todos_list, todos_file_path=TODOS_FILE):
    """
    Read the todos_file_path to load the list of todo items
    into the todos_list list.
    """
    try:
        with open(todos_file_path, 'r') as f:
            for i_todo in f.readlines():
                todos_list.append(i_todo.strip())
    except FileNotFoundError:
        with open(todos_file_path, 'w') as f:
            f.write('')


def save_todos_data(todos_list, todos_path_file=TODOS_FILE):
    """
    Save the todos_list to the file todos_path_file in text mode.
    """
    with open(todos_path_file, 'w') as f:
        for i, i_todo in enumerate(todos_list):
            if i == len(todos_list) - 1:
                f.write(i_todo)
            else:
                f.write(i_todo + '\n')

def show_todos(list_todos, show_numbers=False):
    """
    Prints the list of todos.
    """
    for (i, i_todo) in enumerate(list_todos):
        print(' '*5, end='')
        if show_numbers:
            print(i, ' ', end='')
        print(i_todo)

def edit_todo(list_todos, selected, edited_todo, todos_file=TODOS_FILE):
    """
    Allow the user to edit a todo item from the todos list when the
    edit option is selected
    """
    list_todos[selected] = edited_todo
    save_todos_data(list_todos)
def todo_complete(list_todos, index_completed, todos_file=TODOS_FILE):
    """
    Allow the user to mark a todo item as completed when the option is selected,
    and removes it from the todos list.
    """
    list_todos.pop(index_completed)
    save_todos_data(list_todos)


def add_todo(list_todos, todo_item, todos_file=TODOS_FILE):
    list_todos.append(todo_item)
    with open(todos_file, 'r') as f:
        empty = not bool(f.readlines())
    with open(todos_file, 'a') as f:
        if empty:
            f.write(todo_item)
        else:
            f.write(f'\n{todo_item}')