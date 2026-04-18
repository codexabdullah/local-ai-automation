import os

# Path where PDFs should be searched
directory_path = r'C:\Users\abdul\Downloads'

try:
    # Get the list of files
    files = os.listdir(directory_path)
    
    # Check for PDF files
    pdf_files = [file for file in files if file.endswith('.pdf')]
    
    if not pdf_files:
        print("No PDFs found in the Downloads folder.")
    else:
        print(f"Total {len(pdf_files)} PDFs found:\n")
        for pdf_file in pdf_files:
            print(f"- {pdf_file}")

except Exception as e:
    print(f"Error: {e}")

input("\nExecution finished! Press Enter to close...")
