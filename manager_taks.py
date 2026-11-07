import json

class Task:
    def __init__(self, title):
        self.title = title
        self.done = False
        
    def to_dict(self):
        return {"title": self.title, "done": self.done}
                
        
    def complete(self):
        self.done = True
        
    def info(self):
        mark = "x" if self.done else " "
        return f"[{mark}] {self.title}"
     
     
class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def save_to_json(self):
        data = [{"title": t.title, "done": t.done } for t in self.tasks]
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            
    def load_from_json(self):
            try:
                with open("tasks.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
                for item in data:
                    task = Task(item["title"])
                    task.done = item["done"]
                    self.tasks.append(task)
            except FileNotFoundError:
                pass
        
    def add(self, title):
        task = Task(title)
        self.tasks.append(task)
        
    def show(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.info()}")
            
    def complete(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].complete()
        else:
            print("No such task")
            
    def remove(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks.pop(index - 1) 
        else:
            print("No such task")
 
def main():           
    manager = TaskManager()
    manager.load_from_json()

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
            manager.save_to_json()
        
            
        elif choice == "2":
            manager.show()
            
        elif choice == "3":
            try:
                number = int(input("Enter task number to complete :"))
                manager.complete(number)
            except ValueError:
                print ("Please enter a number. ")
                manager.save_to_json()
                
        elif choice == "4":
            try:
                number = int(input("Enter task number to delete: "))
                manager.remove(number)
            except ValueError:
                print("Please enter a number. ")
                manager.save_to_json()
                
        elif choice == "0":
            print("Exit")
            manager.save_to_json()
            break
        
        else:
            print("Invalid option")
            
if __name__== "__main__":
    main()