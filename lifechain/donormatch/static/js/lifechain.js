// Facebook buttons
jQuery(document).ready(function() {
    jQuery(".facebook_button").click(function(btn) {
        jQuery.ajax({
            url: "https://api.facebook.com/method/stream.publish",
            data : {
                "message": jQuery(btn).attr("data-text"),
                "acccess_token": window.LifechainContext.facebook_access_token,
                "format": "json"
            },
            success: function(data){
                window.console && console.log(data);
            }
        });
    });
});
