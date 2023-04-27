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
  
    var currentTheme = localStorage.getItem('theme') || 'light';
    $('body').css(themes[currentTheme]);
    $('#themeSwitch').prop('checked', currentTheme === 'dark');
  
    $('#themeSwitch').change(function() {
      var newTheme = this.checked ? 'dark' : 'light';
      $('body').css(themes[newTheme]);
      localStorage.setItem('theme', newTheme);
    });
  });
  