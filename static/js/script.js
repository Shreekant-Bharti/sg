// Carousel functionality
let currentSlide = 0;
let slides = [];
let dots = [];

function initializeCarousel() {
  slides = document.querySelectorAll(".carousel-slide");
  dots = document.querySelectorAll(".dot");
  if (slides.length > 0) {
    showSlide(0);
  }
}

function showSlide(n) {
  if (slides.length === 0) return;

  // Wrap around to first slide if we go past the end
  if (n >= slides.length) {
    currentSlide = 0;
  }
  // Wrap around to last slide if we go before the start
  else if (n < 0) {
    currentSlide = slides.length - 1;
  } else {
    currentSlide = n;
  }

  // Remove active class from all slides and dots
  slides.forEach((slide) => slide.classList.remove("active"));
  dots.forEach((dot) => dot.classList.remove("active"));

  // Add active class to current slide and dot
  if (slides[currentSlide]) {
    slides[currentSlide].classList.add("active");
  }
  if (dots[currentSlide]) {
    dots[currentSlide].classList.add("active");
  }
}

function changeSlide(n) {
  // Calculate next slide with wrapping
  let nextSlide = currentSlide + n;

  // Handle wrapping around
  if (nextSlide >= slides.length) {
    nextSlide = 0;
  } else if (nextSlide < 0) {
    nextSlide = slides.length - 1;
  }

  showSlide(nextSlide);
}

function goToSlide(n) {
  currentSlide = n;
  showSlide(currentSlide);
}

// Auto-advance carousel
setInterval(() => {
  if (slides.length > 0) {
    changeSlide(1);
  }
}, 6000);

// Music Player
const musicToggle = document.getElementById("musicToggle");
const backgroundMusic = document.getElementById("backgroundMusic");
let isPlaying = false;

// Set volume to medium level (50%)
backgroundMusic.volume = 0.5;

musicToggle.addEventListener("click", () => {
  if (isPlaying) {
    backgroundMusic.pause();
    musicToggle.classList.remove("playing");
    musicToggle.innerHTML =
      '<i class="fas fa-music"></i><span>Play Music</span>';
  } else {
    backgroundMusic.play();
    musicToggle.classList.add("playing");
    musicToggle.innerHTML =
      '<i class="fas fa-pause"></i><span>Pause Music</span>';
  }
  isPlaying = !isPlaying;
});

// Get Surprise
function getSurprise(type) {
  fetch(`/get-surprise?type=${type}`)
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        const resultDiv = document.getElementById("surpriseResult");
        resultDiv.innerHTML = `<div class="surprise-message">${data.message}</div>`;
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

// Reveal Random Reason Why I Love You
let reasonsShown = new Set();

function revealReason() {
  fetch("/get-random-reason")
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        const reasonText = document.getElementById("currentReason");
        const reasonNumber = document.getElementById("reasonNumber");

        // Add animation
        reasonText.style.opacity = "0";
        reasonText.style.transform = "translateY(20px)";

        setTimeout(() => {
          reasonText.textContent = data.reason;
          reasonNumber.textContent = data.number;
          reasonsShown.add(data.number);

          reasonText.style.transition = "all 0.8s ease";
          reasonText.style.opacity = "1";
          reasonText.style.transform = "translateY(0)";

          // Add sparkle effect
          createHeartSparkles();
        }, 300);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

// Create heart sparkles animation
function createHeartSparkles() {
  const reasonDisplay = document.querySelector(".reason-display");

  for (let i = 0; i < 5; i++) {
    const sparkle = document.createElement("div");
    sparkle.textContent = "💖";
    sparkle.style.cssText = `
      position: absolute;
      font-size: 1.5rem;
      pointer-events: none;
      animation: sparkleFloat 2s ease-out forwards;
      left: ${Math.random() * 100}%;
      top: 50%;
    `;

    reasonDisplay.appendChild(sparkle);

    setTimeout(() => sparkle.remove(), 2000);
  }
}

// Add sparkle animation to CSS dynamically
const style = document.createElement("style");
style.textContent = `
  @keyframes sparkleFloat {
    0% {
      transform: translateY(0) scale(1);
      opacity: 1;
    }
    100% {
      transform: translateY(-100px) scale(0.5);
      opacity: 0;
    }
  }
`;
document.head.appendChild(style);

// Toggle Show All Reasons
let allReasonsVisible = false;

function toggleAllReasons() {
  const allReasonsList = document.getElementById("allReasonsList");
  const showAllText = document.getElementById("showAllText");

  allReasonsVisible = !allReasonsVisible;

  if (allReasonsVisible) {
    allReasonsList.style.display = "grid";
    showAllText.textContent = "Hide All Reasons";

    // Smooth scroll to the list
    setTimeout(() => {
      allReasonsList.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }, 100);
  } else {
    allReasonsList.style.display = "none";
    showAllText.textContent = "Show All 120 Reasons";
  }
}

// Add Message
function addMessage() {
  const messageInput = document.getElementById("newMessage");
  const message = messageInput.value.trim();

  if (!message) {
    alert("Please write a message first! 💕");
    return;
  }

  fetch("/add-message", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: message }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        messageInput.value = "";
        loadMessages();

        // Show success animation
        const form = document.querySelector(".add-message-form");
        const successMsg = document.createElement("div");
        successMsg.className = "success-notification";
        successMsg.textContent = "💕 Message added successfully!";
        successMsg.style.cssText = `
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: linear-gradient(135deg, #ff6b9d, #ffa4c1);
                color: white;
                padding: 20px 40px;
                border-radius: 50px;
                font-size: 1.2rem;
                box-shadow: 0 10px 30px rgba(255, 107, 157, 0.5);
                z-index: 10000;
                animation: popIn 0.5s ease;
            `;
        document.body.appendChild(successMsg);
        setTimeout(() => successMsg.remove(), 2000);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("Oops! Something went wrong. Please try again. 💔");
    });
}

// Load Messages
function loadMessages() {
  fetch("/get-all-messages")
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        const messagesList = document.getElementById("messagesList");

        if (data.messages.length === 0) {
          messagesList.innerHTML =
            '<p class="no-messages">No messages yet. Be the first to write one! ✨</p>';
        } else {
          messagesList.innerHTML = data.messages
            .map(
              (msg) => `
                        <div class="message-item">
                            <p class="message-text">${msg.text}</p>
                            <span class="message-date">${msg.date}</span>
                        </div>
                    `
            )
            .join("");
        }
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

// Image Lightbox
function openModal(imageSrc, caption, quote) {
  const modal = document.getElementById("imageModal");
  const modalImg = document.getElementById("modalImage");
  const captionText = document.getElementById("caption");

  modal.style.display = "block";
  modalImg.src = imageSrc;
  captionText.innerHTML = `<h3 style="color: #ff6b9d; font-family: 'Lora', serif;">${caption}</h3><p style="font-style: italic; margin-top: 15px; font-size: 1.1rem; color: #ccc;">"${quote}"</p>`;
}

function closeModal() {
  document.getElementById("imageModal").style.display = "none";
}

// Close modal on background click
document.getElementById("imageModal").addEventListener("click", function (e) {
  if (e.target === this) {
    closeModal();
  }
});

// Keyboard navigation for modal
document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") {
    closeModal();
  }
});

// Smooth scrolling for any future navigation
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
      });
    }
  });
});

// Add parallax effect to hearts
window.addEventListener("scroll", () => {
  const scrolled = window.pageYOffset;
  const hearts = document.querySelectorAll(".heart");
  hearts.forEach((heart, index) => {
    const speed = 0.5 + index * 0.1;
    heart.style.transform = `translateY(${scrolled * speed}px) rotate(45deg)`;
  });
});

// Initialize on load
window.addEventListener("load", () => {
  initializeCarousel();
  loadMessages();

  // Add welcome animation
  const welcomeContent = document.querySelector(".welcome-content");
  if (welcomeContent) {
    welcomeContent.style.opacity = "0";
    welcomeContent.style.transform = "translateY(30px)";

    setTimeout(() => {
      welcomeContent.style.transition = "all 1.5s ease";
      welcomeContent.style.opacity = "1";
      welcomeContent.style.transform = "translateY(0)";
    }, 300);
  }

  console.log("💕 Website loaded with love for Shristi! ✨");
});
