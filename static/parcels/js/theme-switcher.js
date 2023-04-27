$(function() {
    var themes = {
      light: {
        'background-color': '#ffffff',
        'color': '#000000'
      },
      dark: {
        'background-color': '#343a40',
        'color': '#ffffff'
      }
    };
  
    var currentTheme = 'light';
    var themeSwitcher = $('#theme-switcher-btn');
  
    themeSwitcher.click(function() {
      var newTheme = currentTheme === 'light' ? 'dark' : 'light';
      $('body').css(themes[newTheme]);
      currentTheme = newTheme;
    });
  });
  