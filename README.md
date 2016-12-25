# Croppic combine Carousel Example - Python Flask 
Croppic 搭配 Carousel 簡單範例 ，使用 Python Flask 

* [Youtube Demo](https://youtu.be/fbZ0S659S_g)  

常看到別人的網站有上傳圖片(並且有截圖功能)，教你使用 Python [Flask](http://flask.pocoo.org/) 快速建立一個。

Croppic 搭配 Bootstrap Carousel 簡單範例 📝

## 特色
* 使用 [croppic](http://www.croppic.net/) 實現截圖功能。
* 搭配 Bootstrap Carousel 。
* 搭配 SQLite。


## 安裝套件 Pillow
請先確定電腦有安裝 [Python](https://www.python.org/)

接著請安裝[ Pillow ]( http://pillow.readthedocs.org/en/3.1.x/index.html ) 
```
pip install Pillow
```
更多資料可參考 [ http://pillow.readthedocs.org/en/3.1.x/index.html ]( http://pillow.readthedocs.org/en/3.1.x/index.html ) 

之前我也有稍微介紹過[ Pillow ]( http://pillow.readthedocs.org/en/3.1.x/index.html ) ，可參考 [pillow-examples ]( https://github.com/twtrubiks/pillow-examples ) 

### 使用 Croppic 

更多 croppic 資料 ，可參考  [croppic](http://www.croppic.net/)



## 執行畫面
首頁

![alt tag](http://i.imgur.com/AYxeOud.jpg)

按 上傳圖片 的按鈕

![alt tag](http://i.imgur.com/h4aSEFu.jpg)

上傳自己想要裁切的圖片

![alt tag](http://i.imgur.com/UK7e7HC.jpg)

輸入圖片的描述

![alt tag](http://i.imgur.com/XRclGOI.jpg)

接著你就會看到 Bootstrap Carousel 裡面有圖片了
![alt tag](http://i.imgur.com/6JLf0Iw.jpg)

當你上傳更多的圖片
![alt tag](http://i.imgur.com/chNXkOl.jpg)

裁切過的圖片放在 <b>croppic-flask/static/uploads</b>

![alt tag](http://i.imgur.com/75OImp6.jpg)

SQLite

![alt tag](http://i.imgur.com/UbqSqtx.jpg)

## 後記
因為要截圖，所以必須用到[ Pillow ]( http://pillow.readthedocs.org/en/3.1.x/index.html ) 這個套件，稍微麻煩一點點，如果你單純只是要傳檔案，

可以使用之前介紹過的 [ Dropzone.js ](http://www.dropzonejs.com/)，這個就是直接傳給你檔案，會比較方便，可參考我之

前寫的範例[ flask-dropzone-wavesurfer ](https://github.com/twtrubiks/flask-dropzone-wavesurfer )。


 
## 執行環境
* Python 3.4.3

## Reference 
* [croppic](http://www.croppic.net/)
* [ Pillow ]( http://pillow.readthedocs.org/en/3.1.x/index.html ) 

## License
MIT license
