import tkinter as tk

def create_widget_frame(parent, title):
    frame = tk.Frame(parent, bd=2, relief=tk.GROOVE)
    frame.pack(padx=10, pady=10)

    title_label = tk.Label(frame, text=title, font=("Helvetica", 14, "bold"))
    title_label.pack(padx=5, pady=5)

    return frame

# Create the main window
root = tk.Tk()
root.title("Widget Frame Example")

# Create a frame to contain widgets
widget_frame = create_widget_frame(root, "My Widgets")

# Add widgets to the frame
label = tk.Label(widget_frame, text="This is a label")
label.pack(padx=5, pady=5)

button = tk.Button(widget_frame, text="Click Me")
button.pack(padx=5, pady=5)

entry = tk.Entry(widget_frame)
entry.pack(padx=5, pady=5)

# Start the main event loop
root.mainloop()
