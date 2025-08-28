# File Handling and Error Handling Assignment
# Author: [Your Name]
# Date: [Today's Date]

# -------------------------------
# Part 1: File Read & Write Challenge
# -------------------------------

def read_and_modify_file(input_file, output_file):
    """
    Reads the content of input_file, modifies it, 
    and writes the result into output_file.
    """
    try:
        with open(input_file, "r") as f:
            content = f.read()

        # Example modification: convert text to uppercase
        modified_content = content.upper()

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ Successfully created '{output_file}' with modified content.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# -------------------------------
# Part 2: Error Handling Lab
# -------------------------------

def file_reader():
    """
    Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
    """
    filename = input("📂 Enter the filename you want to read: ")

    try:
        with open(filename, "r") as f:
            print("\n📄 File content:")
            print(f.read())

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"🚫 Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# -------------------------------
# Main Program
# -------------------------------

if __name__ == "__main__":
    # Part 1
    read_and_modify_file("input.txt", "output.txt")

    # Part 2
    file_reader()
