

var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.3.1.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);



var initialValue = 2012;

var sliderTooltip = function(event, ui) {
    var curValue = ui.value || initialValue;
    var tooltip = '<div class="tooltip"><div class="tooltip-inner">' + curValue + '</div><div class="tooltip-arrow"></div></div>';

    $('.ui-slider-handle').html(tooltip);

}

$("#slider").slider({
    value: initialValue,
    min: 1955,
    max: 2015,
    step: 1,
    create: sliderTooltip,
    slide: sliderTooltip
});
