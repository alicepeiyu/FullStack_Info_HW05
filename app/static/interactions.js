$("#submit-survey").on("click", function submitSurvey() {
	// console.log(test);
	var color = $("input[name=color]").val();
	var food = $("input[name=food]").val();
	var vacation = $("input[name=vacation]").val();
	var feBefore = $("input[name=front-end-before]").val();
	var feAfter = $("input[name=front-end-after]").val();

	// console.log(test);

	$.post("/submit-survey",
		{ "color": color,
		"food": food,
		"vacation": vacation,
		"feBefore": feBefore,
		"feAfter": feAfter },
		function(user-input) {
			// console.log(test);
			$(.result-item).html(user-input);
		});
        
});

$("#site-title-wrapper").on('click', function goHome() {
	window.location.href = '/';
});

$(document).ready(function applySliderLabels() {
	var currentValue = $("#fe-before").val();
	$("#fe-before").next().html(currentValue);

	currentValue = $("#fe-after").val();
	$("#fe-after").next().html(currentValue);
});

$("input[type='range']").on('change', function updateLabel() {
	var currentValue = $(this).val();
	$(this).next().html(currentValue);
});
