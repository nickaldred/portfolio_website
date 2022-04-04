
//A script which redirects the user if loaded in a mobile browser

if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    window.location = "http://m.example.com/";
 }