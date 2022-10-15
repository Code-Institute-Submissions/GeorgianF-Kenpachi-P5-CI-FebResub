let video = document.getElementById("background-video");
let icon = document.getElementById("play-icon");

icon.addEventListener('click', () => {
    video.style.display = 'block';
    if (video.paused) {
        video.play();
        icon.src = "media/pause.png" || "https://kenpachi-estore.s3.amazonaws.com/media/pause.png";
    } else {
        video.pause();
        icon.src = "media/play.png" || "https://kenpachi-estore.s3.amazonaws.com/media/play.png";
        
    }
})