from flask import Flask , url_for , render_template
from markupsafe import escape

app = Flask(__name__)
name_dict = { "Faker" : "Lee Sang-hyeok	" , "Zeus" : "Choi Woo-je" , "Oner" : "Mun Hyeon-jun" , "Gumayusi" : "Lee Min-hyeong" , "Keria" : "Ryu Min-seok"}
@app.route('/')
def index():
    return 'This is the root page'

@app.route('/home/')
def home(): 
    return render_template('index.html' , pathImg = url_for('static' , filename = 'imgs/') ,   pathStyle =  url_for('static' , filename = 'css/'))

@app.route('/home/<aboutname>')
def aboutHandle(aboutname) : 
    return render_template( 'about_base.html' , player_nickname = aboutname , player_realname = idName(aboutname) , copyright = "Cá Ngừ 1 Nắng")

def idName(player_nickname) : 
    return name_dict[player_nickname]
 
# with app.test_request_context() : 
#     testUrlBuild()
