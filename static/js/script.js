console.log("Hello world!");


/**
 * @scrollToTop
 * This function shows the button when the user scrolls down 80px from top of document
 * @topPage
 * This function scrolls to the top of the page when the button is clicked
 */

let mybutton = document.getElementById("topBtn");

window.addEventListener('scroll', function(e) {
    scrollToTop()
});

function scrollToTop() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    mybutton.style.display = "block";
        } else {
    mybutton.style.display = "none";
        }
}

function topPage() {
    document.body.scrollTo({top: 0, behavior: 'smooth'});
    document.documentElement.scrollTo({top: 0, behavior: 'smooth'});
}

$(document).ready(function() {
    $('#topBtn').click(function(){
        topPage();
    });
});