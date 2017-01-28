$('a.toggle').on('click', function(){
  $('section').scrollTop(0);
  $('.contain').toggleClass('active');
  return false;
})

$('section').on('click', function(){
//  $(this).closest('section').prependTo('.contain');
  $('section').removeClass('active');
  $(this).addClass('active');
  $('.contain').removeClass('active');
})
