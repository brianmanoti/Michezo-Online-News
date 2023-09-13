let currentPage = 1;

function loveImage(imageNumber) {
    alert(`You loved Image ${imageNumber}`);
}

function commentImage(imageNumber) {
    alert(`You commented on Image ${imageNumber}`);
}

function shareImage(imageNumber) {
    alert(`You shared Image ${imageNumber}`);
}

function nextPage() {
    // You can load the next page of images here.
    currentPage++;
    // For example, you can load new images dynamically or display a message.
    alert(`Loading Page ${currentPage}`);
}
