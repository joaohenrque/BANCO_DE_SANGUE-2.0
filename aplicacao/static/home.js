


$(document).ready(function() {
  var vHeight = $(window).height();
  var home = document.getElementById("home"); //getBoundingClientRect doesn't work on $('#home') therefore using pure js to retrieve it



  $(".btn-menu").click(function() {
    $("#nav").toggleClass("visible");
    $("#nav ul li").toggleClass("animated-nav-items");
  });

  $(window).scroll(function() {
    //change background color of menu button when user scrolls to #work or bottom
    var homePosY = home.getBoundingClientRect().top - 40;

    if (homePosY <= -vHeight) {
      $(".btn-menu .wrapper").addClass("with-bg");
    } else {
      $(".btn-menu .wrapper").removeClass("with-bg");
    }
  });

  $('#nav ul a').click(function() {
    $('html, body').animate({
      scrollTop: $($.attr(this, 'href')).offset().top
    }, 500);
    $('#nav ul li').removeClass('active');
    $(this).parent().addClass('active');
  });

  // Open links in the same tab
  $('.btn').click(function() {
    var href = $(this).attr('href');
    if (href && href !== "#") {
      window.location.href = href;
    }
  });
});
