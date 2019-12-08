$(function(){
  function userMessageBuild(message){
    var userMessageHTML = ` <div class="balloon1-right">
                              <p>${message}</p>
                            </div>
                          `
    return userMessageHTML
  } 
  $('#js-btn').on('click',function(){
    var userMessage = $('#js-message').val();
    
    if (userMessage != ""){
      var HTML = userMessageBuild(userMessage)
      $('.main-contents').append(HTML)
    }
  })
})