
(function() {
	'use strict';

	var tinyslider = function() {
		var el = document.querySelectorAll('.testimonial-slider');

		if (el.length > 0) {
			var slider = tns({
				container: '.testimonial-slider',
				items: 1,
				axis: "horizontal",
				controlsContainer: "#testimonial-nav",
				swipeAngle: false,
				speed: 700,
				nav: true,
				controls: true,
				autoplay: true,
				autoplayHoverPause: true,
				autoplayTimeout: 3500,
				autoplayButtonOutput: false
			});
		}
	};
	tinyslider();

	


	var sitePlusMinus = function() {

		var value,
    		quantity = document.getElementsByClassName('quantity-container');

		function createBindings(quantityContainer) {
	      var quantityAmount = quantityContainer.getElementsByClassName('quantity-amount')[0];
	      var increase = quantityContainer.getElementsByClassName('increase')[0];
	      var decrease = quantityContainer.getElementsByClassName('decrease')[0];
	      increase.addEventListener('click', function (e) { increaseValue(e, quantityAmount); });
	      decrease.addEventListener('click', function (e) { decreaseValue(e, quantityAmount); });
	    }

	    function init() {
	        for (var i = 0; i < quantity.length; i++ ) {
						createBindings(quantity[i]);
	        }
	    };

	    function increaseValue(event, quantityAmount) {
	        value = parseInt(quantityAmount.value, 10);

	        console.log(quantityAmount, quantityAmount.value);

	        value = isNaN(value) ? 0 : value;
	        value++;
	        quantityAmount.value = value;
	    }

	    function decreaseValue(event, quantityAmount) {
	        value = parseInt(quantityAmount.value, 10);

	        value = isNaN(value) ? 0 : value;
	        if (value > 0) value--;

	        quantityAmount.value = value;
	    }
	    
	    init();
		
	};
	sitePlusMinus();
	
})()

// Use for show address on contact page -----------------------


// document.addEventListener("DOMContentLoaded", function () {
//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(showPosition, showError);
//     } else {
//         document.getElementById("current-location").innerText = "Geolocation is not supported by this browser.";
//     }
// });

// function showPosition(position) {
//     var latitude = position.coords.latitude;
//     var longitude = position.coords.longitude;
    
// 	// /eshop_app/ add this if you want corret address, otherwise it will show error
//     var geocodeUrl = `/eshop_app/api/get-address/?lat=${latitude}&lng=${longitude}`;            

//     fetch(geocodeUrl)
//         .then(response => response.json())
//         .then(data => {
//             if (data.address) {
//                 document.getElementById("current-location").innerText = data.address;
//             } else {
//                 document.getElementById("current-location").innerText = "Unable to retrieve address.";
//             }
//         })
//         .catch(error => {
//             console.error('Error fetching the address:', error);
//             document.getElementById("current-location").innerText = "An error occurred while retrieving the address.";
//         });
// }

// function showError(error) {
//     switch (error.code) {
//         case error.PERMISSION_DENIED:
//             document.getElementById("current-location").innerText = "User denied the request for Geolocation.";
//             break;
//         case error.POSITION_UNAVAILABLE:
//             document.getElementById("current-location").innerText = "Location information is unavailable.";
//             break;
//         case error.TIMEOUT:
//             document.getElementById("current-location").innerText = "The request to get user location timed out.";
//             break;
//         case error.UNKNOWN_ERROR:
//             document.getElementById("current-location").innerText = "An unknown error occurred.";
//             break;
//     }
// }


// use for location on map
document.getElementById('map-icon').addEventListener('click', function() {
	
	var latitude = 28.45783;  // New Delhi ka latitude
	var longitude = 77.69042; // New Delhi ka longitude
  
	var url = `https://www.google.com/maps/@${latitude},${longitude},15z`;
  
	// Map open on new tab
	window.open(url, '_blank');
  });