from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_bmi():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = calculate_bmi_value(weight, height)
        emoji = get_emoji(bmi)
        return render_template('index.html', bmi=bmi, emoji=emoji)
    return render_template('index.html')

def calculate_bmi_value(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_emoji(bmi):
    if bmi >= 18.5 and bmi <= 24.9:
        return "😊"  # Positive emoji
    else:
        return "😞"  # Negative emoji

if __name__ == '__main__':
    app.run(debug=True)
