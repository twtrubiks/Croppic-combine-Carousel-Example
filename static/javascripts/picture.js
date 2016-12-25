
$(document).ready(function() {
    //Croppic
    var cropperOptions = {
            cropUrl: '/API/croppic',
            // customUploadButtonId: 'uploadImgBtn',
            //modal: false,
            processInline: true,
            doubleZoomControls: true,
            rotateControls: true,
            loaderHtml: '<div class="loader bubblingG"><span id="bubblingG_1"></span><span id="bubblingG_2"></span><span id="bubblingG_3"></span></div>',
            onBeforeImgUpload: function() {},
            onAfterImgUpload: function() {},
            onImgDrag: function() {},
            onImgZoom: function() {},
            onBeforeImgCrop: function() {},
            onAfterImgCrop: function(response) {
                console.log("onAfterImgCrop response.filename :" + response.filename);
                $("#filename").val(response.filename);
                $("#myModal").modal();
            },
            onReset: function() {
            },
            onError: function(errormessage) {
                 console.log("onError errormessage :" + errormessage)
            }
        }
    var cropperHeader  = new Croppic('imgID', cropperOptions);

    //CroppicButton
    $( "#croppic_button" ).on( "click", function() {
        $("#CroppicModal").modal();
    });
});



