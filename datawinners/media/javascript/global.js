// DW is the global name space on which all the function/methods will be attached through out the site
// This is to avoid introducing global functions/methods/variables in each page
// which could pollute the global namespace and make path for conflicting between the variable/function/method names, which would make debugging tough.
var DW = {};

$(document).ready(function() {

    DW.flash_message = function() {
        $('.success-message-box').delay(10000).fadeOut();
    };
    var shoudlShowAjaxError = ($('#debug').val()=="True");
    if(shoudlShowAjaxError){
        $("#global_error").ajaxError(function(event, request, settings) {
            $("#global_error").addClass("message-box");
            $("#global_error").html("<p>Error requesting page " + settings.url + "</p>");
        });
    }

    $("#global_error").ajaxSuccess(function() {
        DW.flash_message();
    });

    $.addwatermarks();
    $(".help_icon").tooltip({
        position: "top right",
        relative: true,
        opacity:0.8,
        events: {
            def:     "mouseover,mouseout",
            input:   "focus,blur",
            widget:  "focus mouseover,blur mouseout",
            tooltip: "click,click"
        }

    }).dynamic({ bottom: { direction: 'down', bounce: true } });

    DW.flash_message();
})
