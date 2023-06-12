from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello():
    a = []
    
    for e in range(1, 101):
        if e % 2 == 0:
            a.append(e)
    
    return str(a)

if _name_ == '_main_':
    app.run(host='127.0.0.1', port=8080, debug=True)