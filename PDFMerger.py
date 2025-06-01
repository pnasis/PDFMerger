import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfReader, PdfWriter

def select_files():
    files = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF Files", "*.pdf")]
    )
    file_list.delete(0, tk.END)
    for f in files:
        file_list.insert(tk.END, f)

def merge_pdfs():
    files = file_list.get(0, tk.END)
    if not files or len(files) < 2:
        messagebox.showwarning("No files", "Please select at least two PDF files.")
        return

    output_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Save merged PDF as"
    )
    if not output_path:
        return

    try:
        writer = PdfWriter()
        for pdf in files:
            reader = PdfReader(pdf)
            for page in reader.pages:
                writer.add_page(page)

        with open(output_path, "wb") as f_out:
            writer.write(f_out)

        messagebox.showinfo("Success", f"Merged PDF saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def on_drag_start(event):
    widget = event.widget
    index = widget.nearest(event.y)
    widget._drag_data = {"index": index}

def on_drag_motion(event):
    widget = event.widget
    widget.select_clear(0, tk.END)
    widget.select_set(widget.nearest(event.y))

def on_drag_drop(event):
    widget = event.widget
    new_index = widget.nearest(event.y)
    old_index = widget._drag_data["index"]
    if old_index == new_index:
        return
    item = widget.get(old_index)
    widget.delete(old_index)
    widget.insert(new_index, item)
    widget.select_set(new_index)

if __name__ == "__main__":
    # GUI setup
    root = tk.Tk()
    root.title("PDF Merger")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    btn_select = tk.Button(frame, text="Select PDF Files", command=select_files)
    btn_select.pack(fill='x')

    file_list = tk.Listbox(frame, width=60, height=10, selectmode=tk.SINGLE)
    file_list.pack(pady=5)

    file_list.bind("<Button-1>", on_drag_start)
    file_list.bind("<B1-Motion>", on_drag_motion)
    file_list.bind("<ButtonRelease-1>", on_drag_drop)

    btn_merge = tk.Button(frame, text="Merge PDFs", command=merge_pdfs, bg="#4CAF50", fg="white")
    btn_merge.pack(fill='x', pady=10)

    root.mainloop()
