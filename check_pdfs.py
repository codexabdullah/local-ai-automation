import os

# Path jahan PDFs dhoondni hain
directory_path = r'C:\Users\abdul\Downloads'

try:
    # Files ki list nikaalo
    files = os.listdir(directory_path)
    
    # Check karo PDF hain ya nahi
    pdf_files = [file for file in files if file.endswith('.pdf')]
    
    if not pdf_files:
        print("Downloads folder mein koi PDF nahi mili.")
    else:
        print(f"Total {len(pdf_files)} PDFs mili hain:\n")
        for pdf_file in pdf_files:
            print(f"- {pdf_file}")

except Exception as e:
    print(f"Error: {e}")

input("\nKhail khatam! Enter dabao band karne ke liye...")