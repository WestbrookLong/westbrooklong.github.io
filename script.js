const filters = document.querySelector('.filters');
const buttons = [...document.querySelectorAll('[data-filter]')];
const projects = [...document.querySelectorAll('[data-category]')];
if (filters) filters.hidden = false;
buttons.forEach(button => button.addEventListener('click', () => {
  const category = button.dataset.filter;
  buttons.forEach(item => {
    const selected = item === button;
    item.classList.toggle('active', selected);
    item.setAttribute('aria-pressed', String(selected));
  });
  projects.forEach(project => {
    project.hidden = category !== 'All' && project.dataset.category !== category;
  });
  const count = projects.filter(project => !project.hidden).length;
  document.querySelector('#filter-status').textContent = `${count} projects shown`;
}));
document.querySelector('#year').textContent = new Date().getFullYear();
