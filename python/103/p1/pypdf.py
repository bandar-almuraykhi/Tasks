from pypdf import PdfReader, PdfWriter

# Task 1
reader = PdfReader("file1.pdf")

# Task 2
print(len(reader.pages))

# Task 3
print(reader.pages[0].extract_text())

# Task 4
metadata = reader.metadata
print(metadata.title)
print(metadata.author)

# Task 5
def merge_pdfs():
    writer = PdfWriter()
    writer.append("file1.pdf")
    writer.append("file2.pdf")
    writer.write("merged.pdf")

merge_pdfs()
