
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview
    var streetStr=$('#street').val();
    var cityStr=$('#city').val();
    var address = streetStr + ', ' + cityStr;
    $greeting.text('So, you want to live at '+ address + '?');

    var streetviewUrl='https://maps.googleapis.com/maps/api/streetview?size=400x400&location='+address+'';
    //alert(streetviewUrl)
    $body.append('<img class= "bgimg" src=" ' +streetviewUrl+ '">');

    //load NYTimes AJAX request

    // $.getJSON(URL, function (data){
    //   console.log(data);
    // });

    var nytimesUrl='http://api.nytimes.com/svc/search/v2/articlesearch.json?q=' +cityStr + '&sort=newest&api-key=ebe38e41d9634b22a19a103a9d4bee3e'
    //alert(nytimesUrl)
    $.getJSON(nytimesUrl, function(data) {
      $nytHeaderElem.text('New York Times Articles about ' + cityStr);
      articles=data.response.docs;
      for (var i=0; i<articles.length; i++) {
        var article=articles[i];
        $nytElem.append('<li class="article">'+
         '<a href="'+article.web_url+'">'+article.headline.main+'</a>' +
          '<p>'+article.snippet+'</p>'+ '</li>');
      };
    }).error(function(e){
      $nytHeaderElem.text('New York Times Articles Load Failed!');
    });

    

    return false;
};

$('#form-container').submit(loadData);