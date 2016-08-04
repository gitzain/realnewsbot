import sqlite3
from bottle import route, run, debug
from bottle import redirect, request, template, validate

#----------------------------------------------------------------------
@route('/edit/:no', method='GET')
@validate(no=int)
def edit_item(no):
    """
    Edit a TODO item
    """

    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        status = request.GET.get('status','').strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        redirect("/")
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()
        
        return template('edit_task', old=cur_data, no=no)
    
#----------------------------------------------------------------------
@route('/item:item#[0-9]+#')
def show_item(item):
    """
    Show just one item
    """
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (item))
    result = c.fetchall()
    c.close()
    if not result:
        return 'This item number does not exist!'
    else:
        return 'Task: %s' %result[0]
    
#----------------------------------------------------------------------
@route("/done")
def show_done():
    """
    Show all items that are done
    """
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE 0")
    result = c.fetchall()
    c.close()
    
    output = template("show_done", rows=result)
    return output
    
#----------------------------------------------------------------------
@route("/")
@route("/todo")
def todo_list():
    """
    Show the main page which is the current TODO list
    """
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    
    output = template("make_table", rows=result)
    return output

#----------------------------------------------------------------------
@route("/new", method="GET")
def new_item():
    """
    Add a new TODO item
    """
    if request.GET.get("save", "").strip():
        new = request.GET.get("task", "").strip()
    
        conn = sqlite3.connect("todo.db")
        c = conn.cursor()
        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid
    
        conn.commit()
        c.close()
    
        redirect("/")
    else:
        return template("new_task.tpl")
    

if __name__ == "__main__":
    debug(True)
    run()
    