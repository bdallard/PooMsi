from flask import Flask
app = Flask(__name__)

@app.route('/')
def accueil():
    mots = ["bonjour", "à", "toi,", "visiteur."]
    return render_template('accueil.html', titre="Bienvenue !", mots=mots)

if __name__ == '__main__':
    app.run(debug=False)


