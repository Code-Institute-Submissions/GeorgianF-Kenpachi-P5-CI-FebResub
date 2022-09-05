let video = document.getElementById("background-video");
let icon = document.getElementById("play-icon");

icon.addEventListener('click', () => {
    video.style.display = 'block';
    if (video.paused) {
        video.play();
        icon.src = "/media/images/pause.png";
        // video.style.zIndex = '1';
    } else {
        video.pause();
        icon.src = "/media/images/play.png";
        // video.style.zIndex = '-1';
    }
})