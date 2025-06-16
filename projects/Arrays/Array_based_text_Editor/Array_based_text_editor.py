class TextEditor:
    """
    A simple array-based text editor.

    Features:
    - Insert text at the end.
    - Delete characters from a specific index.
    - Find and replace text.
    - Undo the last operation.
    - Display the current text.
    
    Data Structures:
    - `self.text`: List of characters (acts like an array of characters for mutable string handling).
    - `self.history`: Stack of previous states (to implement undo functionality).
    """

    def __init__(self):
        """
        Constructor to initialize the text editor with empty content
        and an empty history for undo operations.
        
        Why initialize here?
        - Every time we create a new TextEditor, it should start with an empty document.
        - The constructor ensures that **each instance** of the editor has its **own separate state**.
        """
        self.text = []       # Main text stored as an array of characters
        self.history = []    # Stack to keep track of previous versions for undo feature

    def insert_text(self, new_text):
        """
        Insert new text at the end of the current text.
        Before modifying, save the current state to the history for undo.

        Why array (list of chars) instead of string directly?
        - Strings in Python are **immutable**. Lists are mutable, allowing easy deletion and insertion.
        """
        self.history.append(self.text.copy())  # Save current state for undo
        self.text.extend(list(new_text))       # Add new characters to the text array

    def delete_text(self, index, length):
        """
        Delete 'length' number of characters starting from 'index'.

        Why save to history first?
        - To enable undo functionality.
        """
        self.history.append(self.text.copy())  # Save current state for undo
        del self.text[index:index + length]    # Delete characters using list slicing

    def find_and_replace(self, old, new):
        """
        Find all occurrences of 'old' substring and replace with 'new' substring.
        
        Why convert to string temporarily?
        - String replacement operations are simpler with string methods.
        - After replacing, convert back to list of characters.
        """
        self.history.append(self.text.copy())      # Save current state for undo
        text_str = ''.join(self.text)              # Convert list of characters to string
        text_str = text_str.replace(old, new)      # Perform the replacement
        self.text = list(text_str)                 # Convert back to list of characters

    def undo(self):
        """
        Undo the last modification by restoring the previous text state from history.
        """
        if self.history:
            self.text = self.history.pop()  # Pop last state from history stack
        else:
            print("No actions to undo.")

    def display_text(self):
        """
        Display the current text as a string.
        """
        print(''.join(self.text))


def main():
    """
    Main program loop for interacting with the text editor via CLI.
    """
    editor = TextEditor()  # Initialize a new TextEditor instance
    
    while True:
        print("\nOptions: [1] Insert [2] Delete [3] Find/Replace [4] Undo [5] Display [6] Exit")
        choice = input("Choose option: ")

        if choice == '1':
            new_text = input("Enter text to insert: ")
            editor.insert_text(new_text)

        elif choice == '2':
            index = int(input("Start index to delete from (0-based): "))
            length = int(input("Number of characters to delete: "))
            editor.delete_text(index, length)

        elif choice == '3':
            old = input("Find: ")
            new = input("Replace with: ")
            editor.find_and_replace(old, new)

        elif choice == '4':
            editor.undo()

        elif choice == '5':
            editor.display_text()

        elif choice == '6':
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
