
function start()
{
var app = new Vue({
    el: '#myCoolApp',
    data: {
      whatVueSay: 'Мы смогли установить и запустить Vue'
    }
  });

  var app2 = new Vue({
    el: '#app-2',
    data: {
      message: 'Вы загрузили эту страницу в: ' + new Date().toLocaleString(),
      msg2: 'Другие данные.'
    }
  });

}