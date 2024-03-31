"use strict";

document.addEventListener("DOMContentLoaded", function () {
  window.addEventListener("scroll", function () {
    var header = document.querySelector(".header");
    if (window.scrollY > 0) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }
  });

  const mobileNav = document.querySelector(".mobile-navbar-btn");
  const navHeader = document.querySelector(".header");

  const toggleNavbar = () => {
    navHeader.classList.toggle("active");
  };

  mobileNav.addEventListener("click", toggleNavbar);

  const videoElement = document.querySelector(".video");

  if (videoElement) {
    videoElement.addEventListener("click", toggleHover);
    videoElement.addEventListener("touchstart", function () {
      videoElement.classList.add("hovered");
    });

    videoElement.addEventListener("touchend", function () {
      videoElement.classList.remove("hovered");
    });
  }
});

// for video hover effect
function toggleHover() {
  var videoElement = document.querySelector(".video");
  videoElement.classList.toggle("hovered");
}

// for about us learn more
document.getElementById("read-more").addEventListener("click", function () {
  var additionalContent = document.querySelector(".additional-content");
  additionalContent.classList.toggle("hidden");
  var buttonText = document.getElementById("read-more");
  if (additionalContent.classList.contains("hidden")) {
    buttonText.textContent = "Learn More...";
  } else {
    buttonText.textContent = "Show Less...";
  }
});

// for guidelines dropdown
document.addEventListener("DOMContentLoaded", function () {
  const dropdownBtns = document.querySelectorAll(".dropdown-btn");

  dropdownBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      const dropdownContent = this.nextElementSibling;
      const dropdown = this.parentElement; // Get the parent .dropdown element
      dropdown.classList.toggle("open"); // Toggle the class on the parent element
      dropdownContent.classList.toggle("open");
    });
  });
});

// for FAQ
document.querySelectorAll(".faq-question").forEach(function (question) {
  question.addEventListener("click", function () {
    const answer = this.nextElementSibling;
    if (answer.classList.contains("hidden")) {
      answer.classList.remove("hidden");
      answer.style.maxHeight = answer.scrollHeight + "px"; // Set max-height to auto
    } else {
      answer.style.maxHeight = null; // Clear max-height
      answer.addEventListener(
        "transitionend",
        function () {
          answer.classList.add("hidden");
        },
        { once: true }
      ); // Remove transitionend listener after it's triggered once
    }
  });
});

function toggleProfile() {
  var profileContainer = document.getElementById("profileContainer");
  profileContainer.classList.toggle("hide");
  // diamond = document.getElementById("diamond");
  // diamond.classList.toggle("hide");
}



