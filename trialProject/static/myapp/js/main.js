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


