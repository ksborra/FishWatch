from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def home_route() -> tuple[dict[str, any], int]:
    fish: str = request.args.get('q')
    fishies = ["atlantic-sturgeon", "blackbanded-sunfish", "blackside-dace","candy-darter","carolina-darter", "clinch-dace", "duskytail-darter", "emerald-shiner", "golden-darter", "greenfin-darter", "orangefin-madtom", "paddlefish", "roanoke-logperch", "sharphead-darter", "shortnose-sturgeon", "sickle-darter", "slender-chub", "spotfin-chub", "steelcolor-shiner", "tennessee-dace", "variegate-darter", "western-sand-darter", "whitemouth-shiner", "yellowfin-madtom"]
    if fish in fishies:
            return render_template(fish + ".html")
    return render_template("main.html")


if __name__ == '__main__':
    app.run()
