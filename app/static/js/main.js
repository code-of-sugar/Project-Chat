$(function(){
  function userMessageBuild(message){
    var userMessageHTML = ` <div class="balloon1-right">
                              <p>${message}</p>
                            </div>
                          `
    return userMessageHTML
  } 

  function chatbotMessageBuild(message){
    var chatbotMessageHTML= ` <div class="balloon6">
                                <div class="chatting">
                                  <div class="says">
                                    <p>${message}</p>
                                  </div>
                                </div>
                              </div>
                            `
    return chatbotMessageHTML
  }

  function ajaxGetMessage(userMessage){
    if(userMessage != ""){
      $.ajax({
        url: "/",
        type: 'post',
        data: JSON.stringify(userMessage),
        contentType:'application/json',
        success: function(data){
          $('.main-contents').append(chatbotMessageBuild(data))
        }
      })
    }
  }

  function sendMyMessage(userMessage){    
    if (userMessage != ""){
      var HTML = userMessageBuild(userMessage)
      $('.main-contents').append(HTML)
    }
  }


  $('#ajax_submit').on('submit',function(e){
    e.preventDefault();
    var userMessage = $('#js-message').val();
    if (userMessage != ""){
      $('#js-message').val("") //送信後formの値を初期化する
      sendMyMessage(userMessage)
      ajaxGetMessage(userMessage)
    }
  })
  
})