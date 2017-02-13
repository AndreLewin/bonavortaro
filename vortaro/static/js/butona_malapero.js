$(document).ready( function() {

    $("#radikpanelo").children(".btn").click( function() {
        // TODO : Verŝajne nevideblaj antaŭ ol uzi AJAX por la butonoj 
        $("#radikpanelo").children(".btn").prop("disabled",true);
        $("#radikpanelo").children(".btn").addClass("animated fadeout");
    });
});