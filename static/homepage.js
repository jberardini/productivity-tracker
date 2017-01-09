'use strict';

var today = new Date();

function getTimes() {
	var starttime = $('#starttime > option:selected').val();
	var endtime = $('#endtime > option:selected').val();
	$.get('/schedule.json', {'start_time_id': starttime, 'end_time_id': endtime}, function(results) {
		var len = results.times.length;
		for (var i = 0; i < len; i++) {
			if (i > 20 && i < 48 ) {
				$('<label></label>').html(results.times[i][0]).appendTo('#morning');
				$('<input/>').attr({type: 'text', class: 'activities', name: 'activities', id: results.times[i][1]}).appendTo('#morning');
				$('<br>').appendTo('#morning');
			} else if (i > 47 && i < 76) {
				$('<label></label>').html(results.times[i][0]).appendTo('#afternoon');
				$('<input/>').attr({type: 'text', class: 'activities', name: 'activities', id: results.times[i][1]}).appendTo('#afternoon');
				$('<br>').appendTo('#afternoon');
			} else {
				$('<label></label>').html(results.times[i][0]).appendTo('#evening');
				$('<input/>').attr({type: 'text', class: 'activities', name: 'activities', id: results.times[i][1]}).appendTo('#evening');
				$('<br>').appendTo('#evening');
			}
		}
		$('.timedivs').show()
		$('#habitdiv').show()
		$('.habits').draggable()
		$('#submitsched').show()
	})
}

function sendSchedule() {
	var activities = [];
	var times = [];
	$('.activities').each(function() {
		activities.push($(this).val());
		times.push($(this).attr('id'));
	});
	console.log(times);
	$.get('/save.json', {'activities': activities, 'times': times, 'date': today}, function() {
		console.log('success');
	});
}

$(document).ready(function () {
	$('#submittime').on('click', getTimes);
	$('#submitsched').on('click', sendSchedule);
	$('#day').html(today)

});
