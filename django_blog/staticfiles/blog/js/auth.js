// auth.js - progressive enhancement for auth pages
document.addEventListener('DOMContentLoaded', function () {
  const pwdInputs = document.querySelectorAll('input[type="password"]');
  // small enhancement: show password toggle if present
  if (pwdInputs.length) {
    pwdInputs.forEach((input) => {
      const wrapper = input.closest('form');
      if (!wrapper) return;
      // create toggle once per form
      if (!wrapper.querySelector('.pwd-toggle')) {
        const toggle = document.createElement('button');
        toggle.type = 'button';
        toggle.className = 'pwd-toggle';
        toggle.innerText = 'Show';
        toggle.style.marginTop = '8px';
        toggle.style.padding = '6px 8px';
        toggle.style.fontSize = '0.9rem';
        toggle.style.cursor = 'pointer';
        toggle.addEventListener('click', function () {
          pwdInputs.forEach(p => {
            p.type = p.type === 'password' ? 'text' : 'password';
          });
          toggle.innerText = toggle.innerText === 'Show' ? 'Hide' : 'Show';
        });
        // append to form
        wrapper.appendChild(toggle);
      }
    });
  }
});
