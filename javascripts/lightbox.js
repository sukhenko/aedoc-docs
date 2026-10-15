// Клік по скріну — відкрити на весь екран; клік або Esc — закрити
document$.subscribe(function () {
  var lb = document.querySelector('.lb');
  if (!lb) {
    lb = document.createElement('div');
    lb.className = 'lb';
    lb.innerHTML = '<img alt="">';
    document.body.appendChild(lb);
    lb.addEventListener('click', function () { lb.classList.remove('open'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') lb.classList.remove('open'); });
  }
  document.querySelectorAll('.md-typeset img.shot').forEach(function (img) {
    img.onclick = function () { lb.querySelector('img').src = img.src; lb.classList.add('open'); };
  });
});
