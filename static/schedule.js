"use strict";

$(input).on('keyup', dbLookup);

function dbLookup() {
	$.get('/lookup.json', {'activity': activity}, function(result) {
		
	})
}

