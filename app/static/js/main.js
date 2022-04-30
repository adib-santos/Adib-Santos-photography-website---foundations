var icon = document.getElementById('icon'); 
var logo = document.getElementById('logo'); 

icon.addEventListener('click', function(event) {
    document.body.classList.toggle('dark-theme');
    if (document.body.classList.contains('dark-theme')) {
        icon.src = '/static/images/sun.png'; 
        logo.src = '/static/images/logo-white.png'; 
    } else {
        icon.src = '/static/images/moon.png'; 
        logo.src = '/static/images/logo-black.png'; 
    }
})
