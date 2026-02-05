import fitz  # PyMuPDF
import os

# Define directory and ensure it exists
images_dir = os.path.join("static", "images")
if not os.path.exists(images_dir):
    print(f"Directory not found: {images_dir}")
    exit(1)

# List all PDF files
files = [f for f in os.listdir(images_dir) if f.lower().endswith(".pdf")]

if not files:
    print("No PDF files found in static/images.")
    exit()

print(f"Found {len(files)} PDF files. Starting conversion...")

for pdf_file in files:
    full_path = os.path.join(images_dir, pdf_file)
    png_name = os.path.splitext(pdf_file)[0] + ".png"
    png_path = os.path.join(images_dir, png_name)
    
    try:
        print(f"Converting {pdf_file} -> {png_name} ...")
        doc = fitz.open(full_path)
        page = doc.load_page(0)  # load first page
        # Matrix(2, 2) scales by 2x for better quality (roughly 144 DPI if base is 72)
        # You can adjust this for higher resolution
        mat = fitz.Matrix(2, 2) 
        pix = page.get_pixmap(matrix=mat)
        pix.save(png_path)
        print("  Success.")
    except Exception as e:
        print(f"  Failed to convert {pdf_file}: {e}")

print("All done.")
