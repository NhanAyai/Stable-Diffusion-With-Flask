from flask import Flask, request, render_template
from text2image import create_pipeline, text2img, model_list  # Import model_list
import os

# Create a Flask app
app = Flask(__name__)

# Parameters
image_path = 'static/output.jpg'  # The output file shown to users.

# Global variables
history = []
selected_model = "dreamlike-art/dreamlike-photoreal-2.0"  # Default model

@app.route("/", methods=["GET", "POST"])
def index():
    global history, selected_model

    if request.method == "GET":
        return render_template("index.html", history=history, model_list=model_list, selected_model=selected_model)
    else:
        # Get user input
        prompt = request.form.get("prompt")
        selected_model = request.form.get("model")

        # Create pipeline with the selected model
        pipeline = create_pipeline(selected_model)

        # Generate image
        image = text2img(prompt, pipeline)

        # Save the image
        image.save(image_path)

        # Add prompt to history
        history.append(prompt)

        return render_template("index.html", image_url=image_path, history=history, model_list=model_list, selected_model=selected_model)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8888, use_reloader=False)