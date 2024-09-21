import google.generativeai as genai
import PIL.Image
import os
import tkinter as tk
from PIL import Image, ImageDraw
import os

genai.configure(api_key=os.environ.get("API_KEY", "your api key")) 

class DrawingBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Drip 🎨")

        self.canvas = tk.Canvas(self.root, bg='black', width=500, height=500, bd=0, highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)

        self.last_x, self.last_y = None, None
        self.draw_active = False
        self.current_color = "white"  
        self.image = Image.new("RGB", (500, 500), "black")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind('<Button-1>', self.on_button_press)
        self.canvas.bind('<B1-Motion>', self.on_paint)
        self.canvas.bind('<ButtonRelease-1>', self.on_button_release)

        self.control_frame = tk.Frame(self.root, bg='black')
        self.control_frame.pack(pady=10)

        colors = ['white', 'red', 'green', 'blue', 'yellow']
        for color in colors:
            self.create_round_button(self.control_frame, color, command=lambda c=color: self.set_color(c))

        self.create_round_button(self.control_frame, "black", text="✖", command=self.use_eraser)

        self.create_round_button(self.root, "gray", text="🔍", command=self.save_image)

    def create_round_button(self, parent, bg_color, text=None, command=None):
        """Creates a circular button"""
        button_canvas = tk.Canvas(parent, width=50, height=50, bg='black', bd=0, highlightthickness=0)
        button_canvas.pack(side=tk.LEFT, padx=5)
        
        button_canvas.create_oval(5, 5, 45, 45, fill=bg_color, outline="white")

        if text:
            button_canvas.create_text(25, 25, text=text, fill="white")

       
        if command:
            button_canvas.bind("<Button-1>", lambda e: command())

    def create_pill_button(self, parent, bg_color, text, command=None):
        """Creates a pill-shaped button"""
        button_canvas = tk.Canvas(parent, width=100, height=50, bg='black', bd=0, highlightthickness=0)
        button_canvas.pack(pady=10)

        button_canvas.create_oval(0, 0, 100, 50, fill=bg_color, outline=bg_color)

       
        button_canvas.create_text(50, 25, text=text, fill="white")

     
        if command:
            button_canvas.bind("<Button-1>", lambda e: command())

    def set_color(self, color):
        """Set the current color for drawing."""
        self.current_color = color

    def use_eraser(self):
        """Set the current color to the background color (black) to simulate an eraser."""
        self.current_color = 'black'
        self.eraser_thickness = 10
    def on_button_press(self, event):
        """Handles the mouse click event."""
        self.last_x, self.last_y = event.x, event.y
        self.draw_active = True

    def on_paint(self, event):
        """Handles the drawing event when the mouse is dragged."""
        if self.draw_active:
            line_width = 20 if self.current_color == 'black' else 3 

            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.current_color, width=line_width, capstyle=tk.ROUND, smooth=True)

         
            self.draw.line((self.last_x, self.last_y, event.x, event.y), fill=self.current_color, width=line_width)

            self.last_x, self.last_y = event.x, event.y


    def on_button_release(self, event):
        """Stops the drawing action."""
        self.draw_active = False

    def save_image(self):
        """Saves the current canvas as an image file in the home directory."""
       
        home_directory = os.path.expanduser("~")
      
        file_path = os.path.join(home_directory, "Documents/Python/image.png")
     
        self.image.save(file_path)
        print(f"Image saved to {file_path}")

        img = PIL.Image.open('image.png')
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(["What is the answer ?", img])
        print(response.text)



root = tk.Tk()
root.configure(bg='black')
board = DrawingBoard(root)
root.mainloop()


