def load_constitution(file_name="project-8-folder/constitution.txt"):
    """Read the constitution text from a file and return as a list of lines."""
    with open(file_name, 'r') as file:
         lines = [line.strip() for line in file.readlines()]
    return lines

def find_section(lines, start_idx):
    """Find the beginning and end of the section surrounding the line at start_idx."""
    start_section = start_idx
    while start_section > 0 and lines[start_section - 1] != "":
        start_section -= 1
        
    end_section = start_idx
    while end_section < len(lines) - 1 and lines[end_section + 1] != "":
        end_section += 1
    section = lines[start_section:end_section + 1]
    return section

def search_constitution(lines, search_term):
    """Search for the search term in the constitution and return the relevant sections."""
    found = False
    for idx, line in enumerate(lines):
        if search_term.lower() in line.lower():
            found = True
            section = find_section(lines, idx)
            
            print(f"\n--- Found search term '{search_term}' in section at line {idx + 1} ---")
            for line_idx, section_line in enumerate(section):
                print(f"Line {idx + line_idx + 1}: {section_line}")
    return found

def main():
    lines = load_constitution()
    
    while True:
        search_term = input("\nEnter search term: ").strip()
        if not search_term:
            print("Exiting program.")
            break
        
        found = search_constitution(lines, search_term)
        if not found:
            print(f"No sections found containing '{search_term}'.")
            
if __name__ == "__main__":
    main()