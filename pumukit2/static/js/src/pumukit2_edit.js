function Pumukit2Edit(runtime, element) {
    $(element).find('.pumukit-save-button').bind('click', function() {
	var data = {
	    'video_id': $('#video_id').val(),
	};
	var handlerUrl = runtime.handlerUrl(element, 'pumukit_submit');
	$('.xblock-editor-error-message', element).html();
	$('.xblock-editor-error-message', element).css('display', 'none');
	$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
	    if (response.result === 'success') {
		window.location.reload(false);
	    } else {
		$('.xblock-editor-error-message', element).html('Error: '+response.message);
		$('.xblock-editor-error-message', element).css('display', 'block');
	    }
	});
    });

    $(element).find('.pumukit-cancel-button').bind('click', function() {
	runtime.notify('cancel', {});
    });

    $(element).find('.tab-url').bind('click', function(event) {
	$('.component-tab-url').show();
	$('.component-tab-url').removeClass('is-inactive');
	$('.tab-url').addClass('current');

	$('.component-tab-manager').hide();
	$('.component-tab-manager').addClass('is-inactive');
	$('.tab-manager').removeClass('current');

	$('.component-tab-select').hide();
	$('.component-tab-select').addClass('is-inactive');
	$('.tab-select').removeClass('current');

	$('.component-tab-upload').hide();
	$('.component-tab-upload').addClass('is-inactive');
	$('.tab-upload').removeClass('current');

	$('.component-tab-recorder').hide();
	$('.component-tab-recorder').addClass('is-inactive');
	$('.tab-recorder').removeClass('current');

	$('.modal-lg').removeClass('modal-lg-pumukit2');
	$('.modal-content').removeClass('modal-content-pumukit2');
	$('.edit-xblock-modal').removeClass('edit-xblock-modal-pumukit2');
	$('.settings-list').removeClass('settings-list-pumukit2');
	$('.tabs-wrapper').removeClass('tabs-wrapper-pumukit2');
	$('.wrapper-comp-settings').removeClass('wrapper-comp-settings-pumukit2');
    });

    $(element).find('.tab-manager').bind('click', function(event) {
	$('.component-tab-url').hide();
	$('.component-tab-url').addClass('is-inactive');
	$('.tab-url').removeClass('current');

	$('.component-tab-manager').show();
	$('.component-tab-manager').removeClass('is-inactive');
	$('.tab-manager').addClass('current');

	$('.component-tab-select').hide();
	$('.component-tab-select').addClass('is-inactive');
	$('.tab-select').removeClass('current');

	$('.component-tab-upload').hide();
	$('.component-tab-upload').addClass('is-inactive');
	$('.tab-upload').removeClass('current');

	$('.component-tab-recorder').hide();
	$('.component-tab-recorder').addClass('is-inactive');
	$('.tab-recorder').removeClass('current');

	$('.modal-lg').addClass('modal-lg-pumukit2');
	$('.modal-content').addClass('modal-content-pumukit2');
	$('.edit-xblock-modal').addClass('edit-xblock-modal-pumukit2');
	$('.settings-list').addClass('settings-list-pumukit2');
	$('.tabs-wrapper').addClass('tabs-wrapper-pumukit2');
	$('.wrapper-comp-settings').addClass('wrapper-comp-settings-pumukit2');
    });

    $(element).find('.tab-upload').bind('click', function(event) {
	$('.component-tab-url').hide();
	$('.component-tab-url').addClass('is-inactive');
	$('.tab-url').removeClass('current');

	$('.component-tab-manager').hide();
	$('.component-tab-manager').addClass('is-inactive');
	$('.tab-manager').removeClass('current');

	$('.component-tab-select').hide();
	$('.component-tab-select').addClass('is-inactive');
	$('.tab-select').removeClass('current');

	$('.component-tab-upload').show();
	$('.component-tab-upload').removeClass('is-inactive');
	$('.tab-upload').addClass('current');

	$('.component-tab-recorder').hide();
	$('.component-tab-recorder').addClass('is-inactive');
	$('.tab-recorder').removeClass('current');

	$('.modal-lg').addClass('modal-lg-pumukit2');
	$('.modal-content').addClass('modal-content-pumukit2');
	$('.edit-xblock-modal').addClass('edit-xblock-modal-pumukit2');
	$('.settings-list').addClass('settings-list-pumukit2');
	$('.tabs-wrapper').addClass('tabs-wrapper-pumukit2');
	$('.wrapper-comp-settings').addClass('wrapper-comp-settings-pumukit2');
    });

    $(element).find('.tab-recorder').bind('click', function(event) {
	$('.component-tab-url').hide();
	$('.component-tab-url').addClass('is-inactive');
	$('.tab-url').removeClass('current');

	$('.component-tab-manager').hide();
	$('.component-tab-manager').addClass('is-inactive');
	$('.tab-manager').removeClass('current');

	$('.component-tab-select').hide();
	$('.component-tab-select').addClass('is-inactive');
	$('.tab-select').removeClass('current');

	$('.component-tab-upload').hide();
	$('.component-tab-upload').addClass('is-inactive');
	$('.tab-upload').removeClass('current');

	$('.component-tab-recorder').show();
	$('.component-tab-recorder').removeClass('is-inactive');
	$('.tab-recorder').addClass('current');

	$('.modal-lg').addClass('modal-lg-pumukit2');
	$('.modal-content').addClass('modal-content-pumukit2');
	$('.edit-xblock-modal').addClass('edit-xblock-modal-pumukit2');
	$('.settings-list').addClass('settings-list-pumukit2');
	$('.tabs-wrapper').addClass('tabs-wrapper-pumukit2');
	$('.wrapper-comp-settings').addClass('wrapper-comp-settings-pumukit2');
    });

    window.addEventListener('message', function (event) {
	if ('mmId' in event.data) {
	    $('#video_id').val(event.data.mmId);
	}
    }, false);

}

function show_hide_collection(id) {
    id = '#' + id;
    if ($(id).hasClass('pumukit2-list-collection-hide')) {
	$(id).hide();
	$(id).addClass('pumukit2-list-collection-show');
	$(id).removeClass('pumukit2-list-collection-hide');
    } else {
	$(id).show();
	$(id).removeClass('pumukit2-list-collection-show');
	$(id).addClass('pumukit2-list-collection-hide');
    }
    return false;
}

function show_hide_child(id) {
    id = '#' + id;
    if ($(id).hasClass('pumukit2-list-child-hide')) {
	$(id).hide();
	$(id).addClass('pumukit2-list-child-show');
	$(id).removeClass('pumukit2-list-child-hide');
    } else {
	$(id).show();
	$(id).removeClass('pumukit2-list-child-show');
	$(id).addClass('pumukit2-list-child-hide');
    }
    return false;
}

function show_hide_grandchild(id) {
    id = '#' + id;
    if ($(id).hasClass('pumukit2-list-grandchild-hide')) {
	$(id).hide();
	$(id).addClass('pumukit2-list-grandchild-show');
	$(id).removeClass('pumukit2-list-grandchild-hide');
    } else {
	$(id).show();
	$(id).removeClass('pumukit2-list-grandchild-show');
	$(id).addClass('pumukit2-list-grandchild-hide');
    }
    return false;
}
