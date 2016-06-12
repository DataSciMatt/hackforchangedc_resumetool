$('questions').hide().fadeIn(1500);
$('questions').on('click', function() {
  $(this).remove();
});
$('questions').addClass('headline');
