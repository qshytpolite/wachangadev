// Cursor dot
const dot = document.getElementById('cursor-dot');
if (dot) {
  document.addEventListener('mousemove', e => {
    dot.style.opacity = '1';
    dot.style.left = e.clientX - 2.5 + 'px';
    dot.style.top  = e.clientY - 2.5 + 'px';
  });
  document.addEventListener('mouseleave', () => { dot.style.opacity = '0'; });
}

// Mobile nav toggle
const toggle = document.querySelector('.sw-nav-toggle');
const navLinks = document.querySelector('.sw-nav-links');
if (toggle && navLinks) {
  toggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });
}
