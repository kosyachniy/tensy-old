// Менять отображение хедера

$(function() {
	$(window).resize(hideHeader);
});

var x = document.body.clientWidth;

function hideHeader() {
	var y = document.body.clientWidth;

	if (x <= 700 && y > 700) {
		$('.u-expand').css('display', 'inline-block');
	} else if (y <= 700 && x > 700) {
		$('.u-expand').css('display', 'none');
	}

	x = y;
}

// Хедер при нажатии

function change(min_width=700) {
	if (document.body.clientWidth <= min_width) {
		if ($('.u-expand').css('display') == 'block')
			$('.u-expand').css('display', 'none');
		else
			$('.u-expand').css('display', 'inline-block');
	} else {
		document.location.href = '/';
	}
}

// Автоматическое изменение ширины в зависимости от контента

var d = {};

$('textarea').each(function() {
	if (!(this.className in d)) {
		d[this.className] = this.clientHeight + 2;
	}

	this.setAttribute('style', 'height:' + (Math.max(this.scrollHeight, d[this.className])) + 'px; overflow-y:hidden;');
	}).on('input', function() {
		//this.style.height = 'auto';
		this.style.height = (Math.max(this.scrollHeight, d[this.className])) + 'px';
});

// Анимация поисковой строки

changeSearch();

$(function() {
	$(window).resize(changeSearch);
});

function getTextWidth(text, font) {
	var canvas = getTextWidth.canvas || (getTextWidth.canvas = document.createElement("canvas"));
	var context = canvas.getContext("2d");
	context.font = font;
	var metrics = context.measureText(text);
	return metrics.width;
}

function changeSearch() {
	$('.u-search input').css('text-align', 'left');

	var y = document.body.clientWidth;

	var text = $('.u-search input').val();
	if (!text) text = $('.u-search input').attr('placeholder');

	var width_text = getTextWidth(text, $('body').css('font')) + 15; // !15
	var width_input = $('.u-search input').outerWidth();

	var padding = (width_input - width_text) / 2;

	// Попробовать через head style + transition
	$('.u-search input').css('padding-left', padding);
	$('.u-search input').focus(function() {
		$(this).animate({'padding-left': '10px'}, {'duration': 520, 'easing': 'swing'});
	});
	$('.u-search input').focusout(function() {
		$(this).animate({'padding-left': padding + 'px'}, {'duration': 300, 'easing': 'swing'});
	});
}