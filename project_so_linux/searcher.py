import os

class search:
    def search_directories(self,base_path, target_path):
        """Search for directories matching the target_path in the specified base_path."""
        matches = []
        for root, dirnames, filenames in os.walk(base_path):
            # Check if the target_path is in the current directory
            if os.path.basename(target_path) in dirnames:
                matches.append(os.path.join(root, os.path.basename(target_path)))
        return matches

    def main(self):
        # Automatically set the base path to the user's home directory
        base_path = os.path.expanduser("~")  # This gets the home directory
        target_path = "project_so_linux"
        
        if not os.path.isdir(base_path):
            print(f"The base directory '{base_path}' does not exist.")
            return

        matches = self.search_directories(base_path, target_path)
        
        if matches:
            print(f"Found {len(matches)} directory/ies:")
            for match in matches:
                print(match)
        else:
            print("No directories found.")
            
        return match

if __name__ == "__main__":
    search().main()