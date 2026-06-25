# Importing libraries
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)  # It tells where to look for templets and files.

# creates a link betwween the web page and code using URL.
@app.route("/")
def home():
    return render_template("index.html")  # Loads an existing HTML file and sends it to the browser.

# Calculate route - processes form data
@app.route("/calculate", methods=["POST"])
def calculate():
    # Get values from form
    operation = request.form["operation"]
    rows_a = int(request.form["rows_a"])
    cols_a = int(request.form["cols_a"])
    try:
         A = np.array(list(map(float, request.form["matrix_a"].split()))).reshape(rows_a, cols_a)

   

         if operation == "transpose":
          result = str(np.transpose(A))
         elif operation == "determinant":
          result = str(np.linalg.det(A))
         elif operation == "inverse":
          result = str(np.linalg.inv(A))
    
         else:
        # Get Matrix B for add/subtract/multiply
            try:
             rows_b = int(request.form["rows_b"])
             cols_b = int(request.form["cols_b"])
             B = np.array(list(map(float, request.form["matrix_b"].split()))).reshape(rows_b, cols_b)
             if operation == "add":
                result = str(A + B)
             elif operation == "subtract":
              result = str(A - B)
             elif operation == "multiply":
              result = str(np.dot(A, B))
            except ValueError:
             result = "Error: Matrix B rows and columns are Mismatched."
    except ValueError:
      result = "Error: The numbers you entered do not match rows*col."
    return render_template("index.html", result=result)  
if __name__ == "__main__":
    app.run(debug=True)