# Drip
Drip is an AI calculator with the ability to understand images
Here's a README file for your drawing application that integrates Google Generative AI for processing an image:

---

# Drawing Board Application

## Overview

The Drawing Board is a simple drawing application built with Python's `tkinter` library. Users can draw on a canvas, choose colors, use an eraser, and save their artwork. Additionally, the application integrates with Google Generative AI to analyze the drawn image and provide insights.

## Features

- **Drawing Tools**: Choose from multiple colors or use an eraser.
- **Canvas**: A 500x500 pixel drawing area.
- **Image Saving**: Save your drawings as PNG files.
- **AI Integration**: Automatically analyze saved images using Google Generative AI.

## Requirements

- Python 3.x
- Pillow (`PIL`) library
- Google Generative AI SDK
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository or download the code.
2. Install required libraries:
   ```bash
   pip install pillow google-generativeai
   ```
3. Set up your Google API key:
   - Ensure your API key is set as an environment variable named `API_KEY`. You can do this in your terminal:
     ```bash
     export API_KEY="your_google_api_key_here"
     ```

## Usage

1. Run the application:
   ```bash
   python drawing_board.py
   ```
2. Use the mouse to draw on the canvas.
3. Select colors or use the eraser by clicking the corresponding buttons.
4. Save your drawing by clicking the save button. The image will be saved to your Documents directory.
5. After saving, the application will use Google Generative AI to analyze the image and provide responses in the console.

## Code Overview

### Key Components

- **DrawingBoard Class**: Manages the drawing canvas, controls, and interactions.
- **create_round_button Method**: Creates circular buttons for color selection and eraser.
- **on_paint Method**: Handles drawing on the canvas based on mouse movements.
- **save_image Method**: Saves the current canvas as a PNG file and interacts with the Google Generative AI model to analyze the image.

### Example Code

```python
class DrawingBoard:
    # Initialization and setup methods...

    def save_image(self):
        """Saves the current canvas as an image file in the home directory."""
        home_directory = os.path.expanduser("~")
        file_path = os.path.join(home_directory, "Documents/Python/image.png")
        self.image.save(file_path)
        print(f"Image saved to {file_path}")

        img = PIL.Image.open(file_path)
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(["What is the answer?", img])
        print(response.text)
```

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

