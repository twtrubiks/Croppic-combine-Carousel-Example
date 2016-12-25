from flask import *
from Entity.Entity import *
from PIL import Image
import base64, io, os, uuid

API = Blueprint('API', __name__)

UPLOAD_PATH = 'static/uploads'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_PATH)


@API.route('/croppic', methods=['GET', 'POST'])
def croppic():
    try:
        # imgUrl 		// your image path (the one we recieved after successfull upload)
        imgUrl = request.form['imgUrl']
        # imgInitW  	// your image original width (the one we recieved after upload)
        imgInitW = request.form['imgInitW']
        # imgInitH 	    // your image original height (the one we recieved after upload)
        imgInitH = request.form['imgInitH']
        # imgW 		    // your new scaled image width
        imgW = request.form['imgW']
        # imgH 		    // your new scaled image height
        imgH = request.form['imgH']
        # imgX1 		// top left corner of the cropped image in relation to scaled image
        imgX1 = request.form['imgX1']
        # imgY1 		// top left corner of the cropped image in relation to scaled image
        imgY1 = request.form['imgY1']
        # cropW 		// cropped image width
        cropW = request.form['cropW']
        # cropH 		// cropped image height
        cropH = request.form['cropH']
        angle = request.form['rotation']

        # original size
        imgInitW, imgInitH = int(imgInitW), int(imgInitH)

        # Adjusted size
        imgW, imgH = int(float(imgW)), int(float(imgH))
        imgY1, imgX1 = int(float(imgY1)), int(float(imgX1))
        cropW, cropH = int(float(cropW)), int(float(cropH))
        angle = int(angle)

        # image_format = imgUrl.split(';base64,')[0].split('/')[1]
        title_head = imgUrl.split(',')[0]
        img_data = imgUrl.split('base64,')[1]
        imgData = base64.b64decode(img_data)

        source_image = Image.open(io.BytesIO(imgData))
        image_format = source_image.format.lower()
        # create new crop image
        source_image = source_image.resize((imgW, imgH), Image.ANTIALIAS)

        # 可參考 http://www.cnblogs.com/tonghounb/p/5074024.html
        #  https://pillow.readthedocs.io/en/3.0.0/reference/Image.html   Image.rotate(angle, resample=0, expand=0)
        rotated_image = source_image.rotate(-float(angle), Image.BICUBIC)
        rotated_width, rotated_height = rotated_image.size
        dx = rotated_width - imgW
        dy = rotated_height - imgH
        # PIL.Image.new(mode, size, color=0)
        # size – A 2-tuple, containing (width, height) in pixels.
        cropped_rotated_image = Image.new('RGBA', (imgW, imgH))
        cropped_rotated_image.paste(rotated_image.crop((dx / 2, dy / 2, dx / 2 + imgW, dy / 2 + imgH)),
                                    (0, 0, imgW, imgH))

        final_image = Image.new('RGBA', (cropW, cropH), 0)
        final_image.paste(cropped_rotated_image.crop((imgX1, imgY1, imgX1 + cropW, imgY1 + cropH)),
                          (0, 0, cropW, cropH))

        uuid_name = str(uuid.uuid1())
        fName = '{}.{}'.format(uuid_name, image_format)
        data_PictureDate = PictureDate(
            Uuid=fName,
            Title="",
            Description=""
        )
        db.session.add(data_PictureDate)
        db.session.commit()
        savePath = '{}/{}'.format(UPLOAD_FOLDER, fName)
        final_image.save(savePath)

        #  The crop rectangle, as a (left, upper, right, lower)-tuple.
        box = (imgX1, imgY1, imgX1 + cropW, imgY1 + cropH)
        newImg = source_image.crop(box)
        imgByteArr = io.BytesIO()
        newImg.save(imgByteArr, format=image_format)
        imgByteArr = imgByteArr.getvalue()
        imgbase = base64.b64encode(imgByteArr).decode('utf-8')
        img_base64 = '{},{}'.format(title_head, imgbase)

        data = {
            'status': 'success',
            'url': '/{}/{}'.format(UPLOAD_PATH, fName),
            'filename': fName,
            'img_base64': img_base64
        }
        return json.dumps(data)
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e),
        }


@API.route('/add_data', methods=['POST'])
def add_data():
    title = request.form['title']
    desp = request.form['desp']
    filename = request.form['filename']
    data_PictureDate = PictureDate.query.filter_by(Uuid=filename).first()
    data_PictureDate.Title = title
    data_PictureDate.Description = desp
    db.session.commit()
    return redirect("/index")
