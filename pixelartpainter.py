import tkinter as tk
from tkinter import colorchooser

class PixelArtPainter:
    def __init__(self, master, rows=16, cols=16, cell_size=30):
        self.master = master
        self.master.title("🎨 Pixel Art Painter")
        self.master.configure(bg="#f0f0f0")
        
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.current_color = "#000000"  # default black

        # Color picker button
        tk.Button(master, text="🎨 Choose Color", font=("Helvetica", 12, "bold"),
                  command=self.choose_color, bg="#3498db", fg="white").pack(pady=10)

        # Clear button
        tk.Button(master, text="🧹 Clear Canvas", font=("Helvetica", 12, "bold"),
                  command=self.clear_canvas, bg="#e74c3c", fg="white").pack(pady=5)

        # Canvas for pixel art
        self.canvas = tk.Canvas(master, width=self.cols * self.cell_size,
                                height=self.rows * self.cell_size, bg="white")
        self.canvas.pack(pady=10)

        # Draw grid
        self.cells = {}
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                cell = self.canvas.create_rectangle(
                    x1, y1, x2, y2, outline="lightgray", fill="white"
                )
                self.cells[cell] = "white"

        # Bind click events
        self.canvas.bind("<Button-1>", self.paint_cell)  # Left click to paint
        self.canvas.bind("<Button-3>", self.erase_cell)  # Right click to erase

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose a color")[1]
        if color:
            self.current_color = color

    def paint_cell(self, event):
        clicked = self.canvas.find_closest(event.x, event.y)[0]
        self.canvas.itemconfig(clicked, fill=self.current_color)
        self.cells[clicked] = self.current_color

    def erase_cell(self, event):
        clicked = self.canvas.find_closest(event.x, event.y)[0]
        self.canvas.itemconfig(clicked, fill="white")
        self.cells[clicked] = "white"

    def clear_canvas(self):
        for cell in self.cells:
            self.canvas.itemconfig(cell, fill="white")
            self.cells[cell] = "white"

def main():
    root = tk.Tk()
    app = PixelArtPainter(root)
    root.mainloop()

if __name__ == "__main__":
    main()


