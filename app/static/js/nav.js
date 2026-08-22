document.addEventListener('DOMContentLoaded', () => {
  const navToggle = document.querySelector('[data-nav-toggle]');
  const navLinks = document.querySelector('[data-nav-links]');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => navLinks.classList.toggle('is-open'));
  }

  const accountToggle = document.querySelector('[data-account-toggle]');
  const accountMenu = document.querySelector('[data-account-menu]');
  if (accountToggle && accountMenu) {
    accountToggle.addEventListener('click', (event) => {
      event.stopPropagation();
      accountMenu.classList.toggle('is-open');
    });
    document.addEventListener('click', (event) => {
      if (!accountMenu.contains(event.target)) accountMenu.classList.remove('is-open');
    });
  }
});
