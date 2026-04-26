import fitz

doc = fitz.open("document.pdf")

for i, page in enumerate(doc):
    print(f"Page {i+1}")
    print(page.get_text()[:200])