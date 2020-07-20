$(document).ready(function() {

	$('#form1').on('submit', function(event) {

		event.preventDefault();

		var formData = new FormData($('form')[0]);

		$.ajax({
			xhr : function() {
				var xhr = new window.XMLHttpRequest();

				xhr.upload.addEventListener('progress', function(e) {

					if (e.lengthComputable) {

						console.log('Bytes Loaded: ' + e.loaded);
						console.log('Total Size: ' + e.total);
						console.log('Percentage Uploaded: ' + (e.loaded / e.total))

						var percent = Math.round((e.loaded / e.total) * 100);

						$('#bar>div').css('width', percent + '%').text(percent + '%');
                        if(percent==100){
							$('#bar>div').css('width', '0%').text('0%');
							$(".f").append("<h1>uploaded</h1>")
						}
					}

				});

				return xhr;
			},
			type : 'POST',
			url : `upload`,
			data : formData,
			processData : false,
			contentType : false,
			success : function() {
				alert('File uploaded!');
			}
		});

	});

    

});