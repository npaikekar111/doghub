from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])

def main():
    if request.method == "POST":
        resp = request.form

        if resp.get('opt') == 'Husky':
            result = "Price is 35k"
            return render_template("result1.html", resp = result)

        elif resp.get('opt') == "German shepherd":
            result = "Price is 25k"
            return render_template("result2.html", resp=result)

        elif resp.get('opt') == "Pamorelin":
            result = "Price is 15k"
            return render_template("result3.html", resp = result)

    else:
        return render_template("input.html")

if __name__ == '__main__':
    app.run(debug=True)
