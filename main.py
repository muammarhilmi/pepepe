from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    name = 'Syafaa'
    return render_template('index.html',name=name)

@app.route('/detail/<string:name>')
def detail(name):
    return render_template('form.html', name=name )

@app.route('/form')
def form():
    return render_template('form.html')

data = [
    {'id' : 0 , 'name' : 'agus haryo'},
    {'id' : 1 , 'name' : 'agis hartono'},
    {'id' : 2 , 'name' : 'agos hariadi'}
]

@app.route('/profil/<int:id>')
def profil(id):
    return data[id]

database =[
    {'name': 'sepatu compas', 'price': 15000,'stok':True ,'image_url': 'https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full//catalog-image/100/MTA-118564740/compass_sepatu_compass_gazelle_low_-_wafer_green_full01_c50196ea.jpg'},
    {'name': 'sepatu aerostreet', 'price': 50000,'stok':True ,'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2NN9NoBXlzTMT-CN6wjKZrDkVfvToY_n8Y-XCEVlekIh14jBiE-xW2nzqZmH2nc_P7ps&usqp=CAU'}
]

@app.route('/')
def poduct():
    return render_template('index.html', product=database)

@app.route('/simpan-data', methods=['post'])
def sumbit():
    name_product = request.form['name_product'].upper()
    category = request.form['category']
    price = request.form['price']
    data = {'name_product' : name_product, 'category' : category, 'price' : price}
    database.append(data)
    print(database)
    return redirect(url_for('home'))

@app.route('/about')
def about():
    name = 'Bro'
    age = 20
    buah = ['apel', 'duren', 'mendoan']

    product = [
        {'name' : 'sabun', 'price' : 1000, 'stok' : True},
        {'name' : 'molto', 'price' : 1000, 'stok' : False},
    ]
    return render_template('about.html', myname=name, myage=age, buah=buah, product=product)

@app.route('/home-page')
def homepage():
    return render_template('home-page.html')

@app.route('/about-page')
def aboutpage():
    return render_template('about-page.html')