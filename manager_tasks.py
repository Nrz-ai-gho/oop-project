
import sqlite3

db = sqlite3.connect('tasks.db')

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title text,
            done INTEGER
            
)""");

class Task:
    def __init__(self, title):
        self.title = title
        self.done = False
        
    def to_dict(self):
        return {
            "title": self.title,
            "done": self.done
        }
                
        
    def complete(self):
        self.done = True
        
    def info(self):
        mark = "x" if self.done else " "
        return f"[{mark}] {self.title}"
     
     
class TaskManager:
    def __init__(self):
        self.cursor = c
        
        
    def add(self, title):
        task = Task(title)
        
        c.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (title, 0))
        db.commit()
    def show(self):
        c.execute("SELECT id, title, done FROM tasks")
        items = c.fetchall()
        for el in items:
            task_id = el[0]
            title = el[1]
            done = el[2]
            
            mark = "x" if done else " "
            print(f"{task_id}. [{mark}] {title}")
        
            
    def complete(self, task_id):
        c.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
        db.commit()
        
        if c.rowcount == 0:
            print("No such task")
        
            
    def remove(self, task_id):
        c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        db.commit()
        
        if c.rowcount == 0:
            print("No such task")
       
if __name__ == "__main__":          
    manager = TaskManager()


    while True:
        print("\n1. Add task")
        print("2. Show tasks")
        print("3. Mark as completed")
        print("4. Delete task")
        print("0. Exit")
        
        choice = input("Choice : ").strip()
        
        if choice == "1":
            title = input("Enter task : ")
            manager.add(title)
        
            
        elif choice == "2":
            manager.show()
            
        elif choice == "3":
            try:
                number = int(input("Enter task number to complete :"))
                manager.complete(number)
            except ValueError:
                print ("Error 'abc' !! Enter task number to complete: ")
                
                
        elif choice == "4":
            try:
                number = int(input("Enter task number to delete: "))
                manager.remove(number)
            except ValueError:
                print("Error 'abc' !! Enter task number to remove: ")

                
        elif choice == "0":
            print("Exit")
            break
        
        else:
            print("Invalid option MAIN") #FINISH
            
    
        