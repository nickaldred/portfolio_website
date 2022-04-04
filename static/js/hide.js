
//A script which hides an element

document.onscroll = function() {
    if (window.innerHeight + window.scrollY > document.body.clientHeight-300) {
        document.getElementById('social__link__container').style.display='none';
    }
}


