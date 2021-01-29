chrome.storage.sync.get({"blacklist": "", "filterOn": true}, function(items){
  var blacklist = items.blacklist.split(",");
  var titles = new Array();
  var authors = new Array();
  var author, title;
  $("[class='thread ']").each(function(){
    author = $("span.author-name", this).html();
    title = $("a", this).html();
    authors.push(author);
    titles.push(title);
  });
  authors = authors.filter(item => item !== undefined);
  titles = titles.filter(item => item !== undefined);

  var body = JSON.stringify({'titles': titles, 'authors': authors});
  var url = 'http://127.0.0.1:5000/running_related';
  var threadcount = 0;
  fetch(url, {method: 'POST', body: body}).then(
        response => response.json())
        .then(function(data){
          $("[class='thread ']").each(function() {
            var author = $("span.author-name", this).html();
            if (blacklist.includes(author) | data[threadcount]== 1){
              $(this).hide();
              console.log($("a",this).html());
            }
            threadcount = threadcount + 1;
          });
        });
      
    }
);


