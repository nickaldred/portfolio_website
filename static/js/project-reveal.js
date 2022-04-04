
//functions to hide and show the project slide on on the projects pages


function myFunction(id) {
    var delayInMilliseconds = 120; //1 second
    id = id.toString();
    console.log(id)

    document.getElementById("item" + id).style.height="80vh";
    setTimeout(function() {
    document.getElementById("item"+ id +"_picture").style.display="block";
    document.getElementById("item" + id + "_text").style.display="block";
    document.getElementById("cross"+ id).style.display="block";
    }, delayInMilliseconds);
    
  }



function myFunctionhide(id) {
    var delayInMilliseconds = 120; //1 second

    document.getElementById("item" + id).style.height="0vh";
    setTimeout(function() {
    document.getElementById("item"+ id +"_picture").style.display="none";
    document.getElementById("item" + id + "_text").style.display="none";
    document.getElementById("cross"+ id).style.display="none";
    }, delayInMilliseconds);
    
  }


