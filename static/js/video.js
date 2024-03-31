document.addEventListener("DOMContentLoaded", function () {
  const video = document.getElementById("video");
  const overlay = document.getElementById("overlay");
  const playVideo = document.getElementById("my-video"); // Use correct ID

  video.addEventListener("click", function () {
    overlay.style.display = "block";
    playVideo.play();
  });

  overlay.addEventListener("click", function () {
    overlay.style.display = "none";
    playVideo.pause();
  });
});