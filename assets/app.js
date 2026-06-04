// Shared behavior: language toggle, scroll reveal, contact form, mobile nav
(function () {
  var _lang = 'tj';
  function getLang() { return _lang; }
  function setLang(l) { _lang = l; applyLang(l); }

  function applyLang(lang) {
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-tj]').forEach(function (el) {
      var v = el.getAttribute('data-' + lang);
      if (v !== null) el.textContent = v;
    });
    document.querySelectorAll('[data-ph-tj]').forEach(function (el) {
      var v = el.getAttribute('data-ph-' + lang);
      if (v !== null) el.setAttribute('placeholder', v);
    });
    document.querySelectorAll('[data-lang-btn]').forEach(function (b) {
      b.classList.toggle('is-active', b.getAttribute('data-lang-btn') === lang);
      b.setAttribute('aria-pressed', b.getAttribute('data-lang-btn') === lang);
    });
  }

  window.RMK_init = function () {
    // language buttons
    document.querySelectorAll('[data-lang-btn]').forEach(function (b) {
      b.addEventListener('click', function () { setLang(b.getAttribute('data-lang-btn')); });
    });
    applyLang(getLang());

    // scroll reveal
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('revealed'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    document.querySelectorAll('.reveal').forEach(function (el, i) {
      el.style.transitionDelay = (Math.min(i % 6, 6) * 60) + 'ms';
      io.observe(el);
    });

    // smooth anchor + close mobile menu
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (ev) {
        var id = a.getAttribute('href');
        if (id.length > 1) {
          var t = document.querySelector(id);
          if (t) { ev.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
        }
        document.body.classList.remove('nav-open');
      });
    });

    // mobile nav toggle
    var burger = document.querySelector('[data-burger]');
    if (burger) burger.addEventListener('click', function () { document.body.classList.toggle('nav-open'); });

    // header shrink on scroll
    var hdr = document.querySelector('[data-header]');
    if (hdr) {
      var onScroll = function () { hdr.classList.toggle('scrolled', window.scrollY > 30); };
      window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
    }

    // contact form
    var form = document.querySelector('[data-form]');
    if (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var msg = form.querySelector('[data-form-msg]');
        var lang = getLang();
        if (msg) {
          msg.textContent = RMK.contact.form.thanks[lang];
          msg.classList.add('show');
        }
        form.reset();
        setTimeout(function () { if (msg) msg.classList.remove('show'); }, 6000);
      });
    }
  };
})();
