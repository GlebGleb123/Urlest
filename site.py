from flask import Flask, redirect, url_for, render_template, request, flash, Markup, abort
from datab import url_in_db, key_in_db, genNewURL
import re
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
base_url = "localhost:5000"


@app.route("/", methods=["POST", "GET"])
def index():
	if request.method == "POST":
		mydata = request.form["link"]
		l = re.findall(r"(?P<url>https?://[^\s]+)", mydata)

		if l == []:
			flash("Некорректный URL", category="error")
		else:
			if not url_in_db(l[0]):
				genNewURL(l[0])
				
			url = f'{base_url}/{url_in_db(l[0])}'
			flash(Markup(f'Ссылка успешно сгенерирована: <a href="http://{url}" target="_blank">{url}</a>'), category="success")



	return render_template('index.html')

@app.route("/<key>")
def redirecter(key):
	if key_in_db(key):
		return redirect(f"{key_in_db(key)}")
	else:
		abort(404)

@app.errorhandler(404)
def pageNotFount(error):
	return redirect(url_for('index'))



if __name__ == "__main__":
	app.run(debug=True)