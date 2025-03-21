class StoryNode:
    """Represents a node in the decision tree."""
    def __init__(self, event_number, description, left=None, right=None):

        self.event_number = event_number
        self.description = description
        self.left = left
        self.right = right

class GameDecisionTree:
    """Binary decision tree for the RPG."""
    def __init__(self):

        self.story = {}
        self.root = None

    def insert(self, event_number, description, left_event, right_event):
        """Insert a new story node into the tree."""
        if event_number not in self.story:
            self.story[event_number] = StoryNode(event_number, description)

        new_node = self.story[event_number]
        new_node.description = description

        if left_event:
            if left_event not in self.story:
                self.story[left_event] = StoryNode(left_event, "")
            new_node.left = self.story[left_event]

        if right_event:
            if right_event not in self.story:
                self.story[right_event] = StoryNode(right_event, "")
            new_node.right = self.story[right_event]

        if self.root is None:
            self.root = new_node

    def play_game(self):
        """Interactive function that plays the RPG."""
        current_node = self.root

        while current_node:
            print("\n" + current_node.description)

            if current_node.left is None and current_node.right is None:
                print("Your story ends here.")  
                break

            decision = input("Enter 1 or 2: ").strip()
            
            if decision == "1" and current_node.left:
                current_node = current_node.left
                
            elif decision == "2" and current_node.right:
                current_node = current_node.right
                
            else:
                print("Invalid decision. Please enter 1 or 2.")

def load_story(filename, game_tree):
    """Load story from a file and construct the decision tree."""
    try:
        with open(filename, "r") as file:
            for line in file:
                
                parts = line.strip().split(" | ")
                
                if len(parts) != 4:
                    print(f"Skipping invalid line: {line}")
                    continue

                game_tree.insert(int(parts[0]), parts[1], int(parts[2]), int(parts[3]))
                
    except ValueError:
        print("Error: Invalid Data Format in File.")
        exit(1)
        
    except FileNotFoundError:
        print(f"Error: File not found.")
        exit(1)

# Main program
if __name__ == "__main__":
    game_tree = GameDecisionTree()
    load_story("story.txt", game_tree)
    game_tree.play_game()
