$(document).ready(function(){

  // disable form submission on "enter" key
  // $(window).keydown(function(event){
  //     if(event.keyCode == 13) {
  //       event.preventDefault();
  //       return false;
  //     }
  //   });
  // hide all questions to start
  $('.question').hide()
  $('.btn-resume').hide();
  // $('.question').hide().each(function( i ) {
  //     $(this).delay( i * 400 ).fadeIn();
  // });

  // load first question
  // $('.question#1').show();
  $('.question#1').fadeIn(1500);
  $('.response#r1').focus();
  $('.question').each(function( i ) {
    $('.response#r' + i).delay(1300).focus();
    $('body').on('keypress', '.question#' + i, function(e) {
       if (e.keyCode == 13) {
          // alert("Hello " + e.keyCode);
          // e.preventDefault();
          if (i >= 12) {
            $('.btn-resume').delay(200);
            $('.btn-resume').show();
          }
          else {
            e.preventDefault();
          }
          $('.question#' + i).fadeOut(100);
          $('.question#' + ++i).delay(200).fadeIn(1000).focus();
          // $('.question#' + i).fadeIn(1000);
          // $('.response#r' + i).delay(200);
          $('.response#r' + i).delay(1301).focus();
       }
    });
  });
  // when user fills out data and presses enter, load next question
  // $('body').on('keypress', '.question#1', function(e) {
  //    if (e.keyCode == 13) {
  //     // alert("Hello " + e.keyCode);
  //     // e.preventDefault();
  //     $('.question#1').fadeOut(500);
  //     $('.question#2').delay(500);
  //     $('.question#2').fadeIn(1500);
  //     e.preventDefault();
  //    }
  // });

  // $('.question').on('click', function() {
  //   $(this).add();
  // });
  // $('#questions').addClass('headline');

});
