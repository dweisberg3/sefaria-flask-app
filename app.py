from flask import Flask, render_template, request
from get import get_text
from get_commentaries import get_commentary, get_gemara_sections



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # content = get_text()
    parts = get_gemara_sections()
    # fruit = None
    # if(request.method == "POST"):
    #     return f"""
    #     <h1> You selected </h2>
    #     <h2> {request.form.get('fruit')}
    #     """
    # return render_template('index.html', fruit=fruit)
    return render_template('index.html', parts=parts)


@app.route('/names', methods=['GET'])
def get_names():
    print(f"the gemara part   {request.args.get("gemara")}")
    names = get_commentary(request.args.get("gemara"))
    return render_template('names.html',names=names)
    # return f"""
    # <h1> These are the names of commentaries</h1>
    # <p> {names} <\p>
    # """
# def index():
#     fruit = None
#     article_text = None

#     if request.method == 'POST':
#         fruit = request.form.get('fruit')
#         page = wiki_wiki.page(fruit)
#         if page.exists():
#             article_text = page.text
#         else:
#             article_text = "Sorry, the Wikipedia page for this fruit does not exist."

#     return render_template('index.html', fruit=fruit, article_text=article_text)

if __name__ == '__main__':
    app.run(debug=True)