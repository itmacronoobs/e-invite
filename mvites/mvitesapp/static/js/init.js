(function($){
    $(function(){
      $('.sidenav').sidenav();
      $('.parallax').parallax();
      $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
      });
      $('.tabs').tabs();
      $('.collapsible').collapsible();
      $('select').formSelect();
      $('.datepicker').datepicker();
      autoplay();
      function autoplay() {
          $('.carousel').carousel('next');
          setTimeout(autoplay, 4500);
      };
      
    }); // end of document ready
  })(jQuery); // end of jQuery name space
  