# Define a to-do item class
class TodoItem:
  def __init__(self, title, description="", completed=False):
    self.title = title
    self.description = description
    self.completed = completed

  def mark_complete(self):
    self.completed = True

  def __str__(self):
    status = "Completed" if self.completed else "Pending"
    return f"{status}: {self.title} ({self.description})"

# Define the main to-do list application
class TodoList:
  def __init__(self):
    self.items = []

  def add_item(self, title, description=""):
    new_item = TodoItem(title, description)
    self.items.append(new_item)

  def list_items(self):
    for item in self.items:
      print(item)

  def mark_item_complete(self, index):
    if 0 <= index < len(self.items):
      self.items[index].mark_complete()
    else:
      print("Invalid item index")

  def remove_item(self, index):
    if 0 <= index < len(self.items):
      del self.items[index]
    else:
      print("Invalid item index")

# Main program loop
def main():
  todo_list = TodoList()

  while True:
    print("\n--- To-Do List ---")
    print("1. Add Item")
    print("2. List Items")
    print("3. Mark Item Complete")
    print("4. Remove Item")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      title = input("Enter item title: ")
      description = input("Enter item description (optional): ")
      todo_list.add_item(title, description)
      print("Item added successfully!")
    elif choice == '2':
      todo_list.list_items()
    elif choice == '3':
      todo_list.list_items()
      index = int(input("Enter the index of the item to mark complete: ")) - 1
      todo_list.mark_item_complete(index)
    elif choice == '4':
      todo_list.list_items()
      index = int(input("Enter the index of the item to remove: ")) - 1
      todo_list.remove_item(index)
    elif choice == '5':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
