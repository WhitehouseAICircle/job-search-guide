'use strict';
document.querySelectorAll('.prose pre, .prose blockquote').forEach((block) => {
  const text = block.innerText.trim();
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'copy-button';
  button.textContent = block.tagName === 'PRE' ? 'Copy text' : 'Copy prompt';
  button.setAttribute('aria-label', block.tagName === 'PRE' ? 'Copy this example text' : 'Copy this prompt');
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(text);
      button.textContent = 'Copied ✓';
      document.getElementById('copy-status').textContent = 'Text copied. Paste it into your ChatGPT chat.';
      setTimeout(() => { button.textContent = block.tagName === 'PRE' ? 'Copy text' : 'Copy prompt'; }, 2500);
    } catch {
      let field = block.querySelector('textarea');
      if (!field) {
        field = document.createElement('textarea');
        field.className = 'copy-fallback';
        field.readOnly = true;
        field.setAttribute('aria-label', 'Select and copy this text manually');
        field.value = text;
        block.appendChild(field);
      }
      field.focus();
      field.select();
      document.getElementById('copy-status').textContent = 'Automatic copying is unavailable. The text is selected; use your device’s Copy command.';
      button.textContent = 'Select & copy below';
    }
  });
  block.appendChild(button);
});
