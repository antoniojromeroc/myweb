document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
    var elemsParallax = document.querySelectorAll('.parallax');
    var instancesParallax = M.Parallax.init(elemsParallax);
  });

  // Or with jQuery

  $(document).ready(function(){
    $('.sidenav').sidenav();
    $('.parallax').parallax();
  });