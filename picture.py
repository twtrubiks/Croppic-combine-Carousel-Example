from API import *

app = Flask(__name__)
app.register_blueprint(API, url_prefix='/API')


@app.route('/')
@app.route('/index')
def index():
    data_PictureDate = PictureDate.query.all()
    PictureDate_dic = {}
    PictureDate_list = []
    for data in data_PictureDate:
        PictureDate_dic['filename'] = data.Uuid
        PictureDate_dic['Title'] = data.Title
        PictureDate_dic['Description'] = data.Description
        PictureDate_list.append(PictureDate_dic)
        PictureDate_dic = {}
    return render_template('picture.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
