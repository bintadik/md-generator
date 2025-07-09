from google import genai
import os
import dotenv
import subprocess
from pathlib import Path
import pathspec

dotenv.load_dotenv()

def read_file(file_path):
    # The name of the Python file you want to read
    filename = file_path

    print(f"--- Reading '{filename}' as a single string ---")

    try:
        # 'with' ensures the file is closed automatically
        # 'r' mode is for reading
        # 'encoding="utf-8"' is crucial for handling all characters correctly
        with open(filename, 'r', encoding='utf-8') as f:
            # .read() reads the entire file content into one string
            content_as_string = f.read()

        # Now you can work with the content
        print("File content:")
        print(content_as_string)
        
        print("\nType of the content variable:")
        print(type(content_as_string))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return content_as_string

def save_to_markdown(content: str, filename: str):
    """
    Saves the given content to a file with the specified filename.
    
    Args:
        content: The text content to save.
        filename: The name of the file (e.g., 'output.md').
    """
    try:
        # Use 'with' to ensure the file is properly closed
        # 'w' mode overwrites the file if it exists
        # 'encoding='utf-8'' is crucial for handling special characters
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Successfully saved content to '{filename}'")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

# --- Main ---
if __name__=='__main__':
    # Read the file content
    # filepath = input("Enter the path to the file you want to generate a README for: ")
    import os
    folder_path = input("Enter the path to the folder you want to generate a README for: ")
    
    # 1. Define the root folder
    folder_path = Path(folder_path)

    # 2. Load .gitignore patterns
    gitignore_path = folder_path / ".gitignore"
    if gitignore_path.exists():
        with open(gitignore_path) as f:
            ignore_patterns = f.read().splitlines()
        spec = pathspec.PathSpec.from_lines('gitwildmatch', ignore_patterns)
    else:
        spec = None

    # 3. Walk and filter
    list_of_files = []

    for root, dirs, files in os.walk(folder_path):
        for name in files + dirs:
            rel_path = Path(root).joinpath(name).relative_to(folder_path)
            if spec and spec.match_file(str(rel_path)):
                continue  # Skip ignored files/folders
            list_of_files.append(str(Path(root).joinpath(name)))

    print(list_of_files)

    code_resume = ''
    for file in list_of_files:
        try:
            code= read_file(file)
        except:
            pass
        code_resume= f"{code_resume}\n{file}\n{code}\n"

    contents =f"""
        You are markdown file generator for github. create markdown readme file the request. do not include explanations etc.Do not rewrite File Content.
        Request:
        {code_resume}
        """ 
    print(contents)

    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents = contents
        )
    print(response.text)

    # Save the content to a file
    save_to_markdown(response.text, filename=folder_path/"README.md")

