from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)
# __name__은 본인의 이름(파일의 이름) : ex) 이 파일의 __name__은 app.py
# python app.py를 직접 실행하면 __main__이 담겨 있음

# @ : 데코레이터 함수
# --> 함수를 인자로 받아서 함수를 리턴하는 타입의 함수
# 쉽게 서버 주소 뒤에 /를 붙이면 hello 함수가 실행됨
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

# 서버 주소 뒤에 /mulcam 붙이면 mulcam 함수 실행됨
@app.route('/mulcam')
def mulcam():
    return 'This is Mulcam!!!'

# Path Variable / Variable Routing
@app.route('/greeting/<string:name>')
def greeting(name):
    return f'Hi, {name}'    # 'Hi, {}'.format(name)과 동일

@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return f'{num}의 세제곱은 {result}입니다.'

# 사람 수를 Path를 통해 받아, 사람 수만큼 메뉴 추천
@app.route('/menu/<int:person>')
def menu(person):
    caffe = ['아메리카노', '카페라떼', '카푸치노', '카라멜마끼아또', '초코라떼', '루이보스차', '히비스커스차', '레몬에이드', '딸기주스', '오렌지주스']
    result = random.sample(caffe, person)
    return str(result)

@app.route('/html')
def html():
    multiline = """
        <h1>Hi, Hello</h1>
        <p>만나서 반갑습니다!</p>
    """
    return multiline

@app.route('/html_file')
def html_file():
    return render_template('file.html')

# Template Variable
@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', your_name = name)

@app.route('/list')
def list():
    caffe = ['아메리카노', '카페라떼', '카푸치노', '카라멜마끼아또', '초코라떼', '루이보스차', '히비스커스차', '레몬에이드', '딸기주스', '오렌지주스']
    return render_template('list.html', menu = caffe)




# 서버를 껐다 켰다 하는 수고를 줄이기 위해 설정!!
# 이 코드들은 코드의 가장 마지막에 있어야함
if __name__ == '__main__':
    app.run(debug=True)

