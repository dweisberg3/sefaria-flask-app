from flask import Flask, render_template, request
from get import get_text
from get_commentaries import get_commentary_names, get_gemara_sections, get_commentary_text



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
    print(f'the gemara part   {request.args.get("gemara")}')
    names = get_commentary_names(request.args.get("gemara"))
    return render_template('names.html',names=names)

@app.route('/texts', methods=['GET'])
def get_text():
    text =get_commentary_text(request.args.get("name"))
    return render_template('text.html',text=text)

if __name__ == '__main__':
    # app.run(debug=True) ## for dev
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    # app.run(host='0.0.0.0', port=80) ## for prod