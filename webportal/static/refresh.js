function updateTemp(gauge_id, selector) {
  $.getJSON('/gauge/' + gauge_id, function(data){
    $(selector).text = response.temp;
  })
}

setInterval('updateTemp(1, "#gauge-1")', 1000 * 60);
setInterval('updateTemp(2, "#gauge-2")', 1000 * 60);