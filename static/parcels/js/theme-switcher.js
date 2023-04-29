$(function() {
  var themes = {
    light: '/static/parcels/css/light.css',
    dark: '/static/parcels/css/dark.css'
  };

  var currentTheme = localStorage.getItem('theme') || 'light';
  $('link#theme-style').attr('href', themes[currentTheme]);
  $('#themeSwitch').prop('checked', currentTheme === 'dark');

  $('#themeSwitch').change(function() {
    var newTheme = this.checked ? 'dark' : 'light';
    $('link#theme-style').attr('href', themes[newTheme]);
    localStorage.setItem('theme', newTheme);
  });
});
