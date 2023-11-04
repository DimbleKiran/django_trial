// myapp/static/myapp/js/main.js

//let videoStream;
//
//document.getElementById('startButton').addEventListener('click', function() {
//    const videoElement = document.getElementById('videoElement');
//
//    navigator.mediaDevices.getUserMedia({ video: true })
//        .then(stream => {
//            videoElement.srcObject = stream;
//            videoStream = stream;
//        })
//        .catch(error => console.error('Error accessing camera:', error));
//});
//
//document.addEventListener('keydown', function(event) {
//    if (event.key === 'c') {  // Capture image when 'c' key is pressed
//        const canvas = document.createElement('canvas');
//        const videoElement = document.getElementById('videoElement');
//        const context = canvas.getContext('2d');
//        canvas.width = videoElement.videoWidth;
//        canvas.height = videoElement.videoHeight;
//        context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
//
//        const imageDataURL = canvas.toDataURL('image/png');
//        const link = document.createElement('a');
//        link.href = imageDataURL;
//        link.download = 'captured_image.png';
//        link.click();
//
//        const form = document.getElementById('captureForm');
//        const imageInput = document.getElementById('imageInput');
//        const blob = dataURItoBlob(imageDataURL);
//        const imageFile = new File([blob], 'captured_image.png', { type: 'image/png' });
//        const formData = new FormData();
//        formData.append('image', imageFile);
//        imageInput.files = formData;
//        form.submit();
//    } else if (event.key === 's') {  // Stop video feed when 's' key is pressed
//        videoStream.getTracks().forEach(track => track.stop());
//        document.getElementById('videoElement').srcObject = null;
//    }
//});
//
//function dataURItoBlob(dataURI) {
//    const byteString = atob(dataURI.split(',')[1]);
//    const ab = new ArrayBuffer(byteString.length);
//    const ia = new Uint8Array(ab);
//    for (let i = 0; i < byteString.length; i++) {
//        ia[i] = byteString.charCodeAt(i);
//    }
//    return new Blob([ab], { type: 'image/png' });
//}


// myapp/static/myapp/js/main.js

// myapp/static/myapp/js/main.js

// myapp/static/myapp/js/main.js

// myapp/static/myapp/js/main.js

// myapp/static/myapp/js/main.js

let videoStream;
let isCameraActive = false;

document.getElementById('startButton').addEventListener('click', function() {
    const videoElement = document.getElementById('videoElement');

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            videoElement.srcObject = stream;
            videoStream = stream;
            isCameraActive = true;
        })
        .catch(error => console.error('Error accessing camera:', error));
});

document.addEventListener('click', function() {
    if (isCameraActive) {
        const canvas = document.createElement('canvas');
        const videoElement = document.getElementById('videoElement');
        const context = canvas.getContext('2d');
        canvas.width = videoElement.videoWidth;
        canvas.height = videoElement.videoHeight;
        context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

        const imageDataURL = canvas.toDataURL('image/png');
        const link = document.createElement('a');
        link.href = imageDataURL;
        link.download = 'captured_image.png';
        link.click();

        videoStream.getTracks().forEach(track => track.stop());
        document.getElementById('videoElement').srcObject = null;
        isCameraActive = false;
    }
});


