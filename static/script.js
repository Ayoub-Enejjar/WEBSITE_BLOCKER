window.onload = function () {
  const bg = document.querySelector(".background");

  for (let i = 0; i < 60; i++) {
    let bubble = document.createElement("div");
    bubble.classList.add("bubble");
    bubble.style.left = Math.random() * 100 + "vw";
    bubble.style.width = bubble.style.height = Math.random() * 20 + 10 + "px";
    bubble.style.animationDuration = Math.random() * 5 + 5 + "s";
    bubble.style.animationDelay = Math.random() * 5 + "s";
    bg.appendChild(bubble);
  }
};
