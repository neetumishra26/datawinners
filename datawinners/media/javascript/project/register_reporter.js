$(document).ready(function() {
    $(document).ajaxStop($.unblockUI);
    $("#id_register_button").unbind().live('click', function() {
        $.blockUI({
            message: '<h1><img src="/media/images/ajax-loader.gif"/><span class="loading">' + gettext("Just a moment") + '...</span></h1>',
            css: { width:'275px',top: '400px', left: '800px'}
        });
        $.ajax({
            type: 'POST',
            url: '/entity/datasender/create',
            data: $("#registration_form").serialize(),
            success:function(response) {
                $("#add_data_sender_form").html(response);
                $("#id_location").catcomplete({
                    source: "/places"});
            },
            error: function(e) {
                $("#message-label").show().html("<label class='error_message'>" + e.responseText + "</label>");
            }

        });
    });
    $.widget("custom.catcomplete", $.ui.autocomplete, {
        _renderMenu: function(ul, items) {
            var self = this,
                    currentCategory = "";
            $.each(items, function(index, item) {
                if (item.category != currentCategory) {
                    ul.append("<li class='ui-autocomplete-category'>" + item.category + "</li>");
                    currentCategory = item.category;
                }
                self._renderItem(ul, item);
            });
        }
    });

    $("#id_location").catcomplete({
        source: "/places"
    });

});
