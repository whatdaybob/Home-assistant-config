const ICON = {
  virus: 'M22.5 10.7h-1c-2.3 0-3.5-2.8-1.9-4.5l.7-.7c.5-.5.5-1.4-.1-1.9-.5-.5-1.3-.5-1.8 0l-.7.7c-1.7 1.7-4.5.5-4.5-1.9v-1c0-.7-.6-1.3-1.3-1.3s-1.3.6-1.3 1.3v1c0 2.3-2.8 3.5-4.5 1.9l-.6-.7c-.5-.4-1.4-.4-1.9.1-.4.5-.4 1.3 0 1.8l.7.7c1.7 1.7.5 4.5-1.9 4.5h-1c-.7 0-1.3.6-1.3 1.3s.6 1.3 1.3 1.3h1c2.3 0 3.5 2.8 1.9 4.5l-.7.7c-.5.5-.5 1.4.1 1.9.5.5 1.3.5 1.8 0l.7-.7c1.7-1.7 4.5-.5 4.5 1.9v1c0 .7.6 1.3 1.3 1.3s1.3-.6 1.3-1.3v-1c0-2.3 2.8-3.5 4.5-1.9l.7.7c.5.5 1.4.5 1.9-.1.5-.5.5-1.3 0-1.8l-.7-.7c-1.7-1.7-.5-4.5 1.9-4.5h1c.7 0 1.3-.6 1.3-1.3s-.6-1.3-1.4-1.3h0zm-12 2a2.22 2.22 0 0 1-2.2-2.2 2.22 2.22 0 0 1 2.2-2.2 2.22 2.22 0 0 1 2.2 2.2 2.22 2.22 0 0 1-2.2 2.2zm3.7 2.6a1.11 1.11 0 0 1-1.1-1.1 1.11 1.11 0 0 1 1.1-1.1 1.11 1.11 0 0 1 1.1 1.1 1.11 1.11 0 0 1-1.1 1.1z',

  roborock: 'M13.3 5.3c-.1 0-.2 0-.3.1-.1 0-.2 0-.4-.1-.1-.2-.3-.3-.6-.3s-.5.2-.6.4c-.1 0-.2 0-.3.1-.1-.1-.2-.1-.3-.1a.47.47 0 0 0-.5.5.47.47 0 0 0 .5.5c.2 0 .4-.1.4-.3h.2c.1.2.3.3.6.3.2 0 .5-.1.6-.4h.2c.1.2.2.3.4.3a.47.47 0 0 0 .5-.5c0-.3-.2-.5-.4-.5zM12 6.9a3.33 3.33 0 0 1 3.3 3.3 3.33 3.33 0 0 1-3.3 3.3 3.33 3.33 0 0 1-3.3-3.3A3.33 3.33 0 0 1 12 6.9zM12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm7.4 13.1c-.4 1-1 1.8-1.7 2.6a7.82 7.82 0 0 1-2.6 1.7c-1 .4-2.1.6-3.1.6s-2.1-.2-3.1-.6-1.8-1-2.6-1.7-1.3-1.6-1.7-2.6S4 13 4 12c0-.4 0-.8.1-1.1h4.3c0-.2-.1-.4-.1-.6s0-.4.1-.6h-4c.1-.3.2-.5.3-.8.4-1 1-1.8 1.7-2.6C7 5.5 7.9 5 8.9 4.6S11 4 12 4s2.1.2 3.1.6 1.8 1 2.6 1.7 1.3 1.6 1.7 2.6c.1.2.2.5.3.8h-4c0 .2.1.4.1.6s0 .4-.1.6H20c.1.4.1.8.1 1.1 0 1.1-.2 2.1-.7 3.1z',
};

async function getIcon(name) {
  return {
    path: ICON[name]
  };
}

window.customIconsets = window.customIconsets || {};
window.customIconsets['custom'] = getIcon;
