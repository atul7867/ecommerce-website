
// (function() {
// 	'use strict';

// 	var tinyslider = function() {
// 		var el = document.querySelectorAll('.testimonial-slider');

// 		if (el.length > 0) {
// 			var slider = tns({
// 				container: '.testimonial-slider',
// 				items: 1,
// 				axis: "horizontal",
// 				controlsContainer: "#testimonial-nav",
// 				swipeAngle: false,
// 				speed: 700,
// 				nav: true,
// 				controls: true,
// 				autoplay: true,
// 				autoplayHoverPause: true,
// 				autoplayTimeout: 3500,
// 				autoplayButtonOutput: false
// 			});
// 		}
// 	};
// 	tinyslider();

	


// 	var sitePlusMinus = function() {

// 		var value,
//     		quantity = document.getElementsByClassName('quantity-container');

// 		function createBindings(quantityContainer) {
// 	      var quantityAmount = quantityContainer.getElementsByClassName('quantity-amount')[0];
// 	      var increase = quantityContainer.getElementsByClassName('increase')[0];
// 	      var decrease = quantityContainer.getElementsByClassName('decrease')[0];
// 	      increase.addEventListener('click', function (e) { increaseValue(e, quantityAmount); });
// 	      decrease.addEventListener('click', function (e) { decreaseValue(e, quantityAmount); });
// 	    }

// 	    function init() {
// 	        for (var i = 0; i < quantity.length; i++ ) {
// 						createBindings(quantity[i]);
// 	        }
// 	    };

// 	    function increaseValue(event, quantityAmount) {
// 	        value = parseInt(quantityAmount.value, 10);

// 	        console.log(quantityAmount, quantityAmount.value);

// 	        value = isNaN(value) ? 0 : value;
// 	        value++;
// 	        quantityAmount.value = value;
// 	    }

// 	    function decreaseValue(event, quantityAmount) {
// 	        value = parseInt(quantityAmount.value, 10);

// 	        value = isNaN(value) ? 0 : value;
// 	        if (value > 0) value--;

// 	        quantityAmount.value = value;
// 	    }
	    
// 	    init();
		
// 	};
// 	sitePlusMinus();
	
// })()

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



// Use to update code for cart.html , total------------
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
		  var productRow = quantityContainer.closest('tr'); // New: Get the product row
	      var productPrice = parseFloat(productRow.querySelector('.product-name + td').innerText.replace('Rs. ', '')); // New: Get the product price
	      var totalPriceCell = productRow.querySelector('td:nth-child(5)'); // New: Get the cell for the total price

	      increase.addEventListener('click', function (e) { increaseValue(e, quantityAmount, productPrice, totalPriceCell); }); // Updated
	      decrease.addEventListener('click', function (e) { decreaseValue(e, quantityAmount, productPrice, totalPriceCell); }); // Updated
	    }

	    function init() {
	        for (var i = 0; i < quantity.length; i++ ) {
				createBindings(quantity[i]);
	        }
	    };

	    function increaseValue(event, quantityAmount, productPrice, totalPriceCell) { // Updated
	        value = parseInt(quantityAmount.value, 10);

	        value = isNaN(value) ? 0 : value;
	        value++;
	        quantityAmount.value = value;
	        updateTotalPrice(value, productPrice, totalPriceCell); // New: Update the total price
	    }

	    function decreaseValue(event, quantityAmount, productPrice, totalPriceCell) { // Updated
	        value = parseInt(quantityAmount.value, 10);

	        value = isNaN(value) ? 0 : value;
	        if (value > 0) value--;
	        quantityAmount.value = value;
	        updateTotalPrice(value, productPrice, totalPriceCell); // New: Update the total price
	    }

	    function updateTotalPrice(quantity, price, totalPriceCell) { // New: Function to update the total price
	    	const newTotalPrice = price * quantity;
	    	totalPriceCell.innerText = `Rs. ${newTotalPrice.toFixed(2)}`;
	    }
	    
	    init();
		
	};
	sitePlusMinus();
	
})()

// Use for show address on contact page -----------------------

<<<<<<< HEAD

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
=======
document.addEventListener('DOMContentLoaded', function() {
    var mapIcon = document.getElementById('map-icon');

    if (mapIcon) {  // Check if map-icon exists on the page
        mapIcon.addEventListener('click', function() {
            var latitude = 28.45783;  // New Delhi ka latitude
            var longitude = 77.69042; // New Delhi ka longitude

            var url = `https://www.google.com/maps/@${latitude},${longitude},15z`;

            // Map ko nayi tab mein kholna
            window.open(url, '_blank');
        });
    } else {
        console.warn('Map icon element not found on this page.');
    }
});


//   use js for shop product-------------
document.addEventListener('DOMContentLoaded', function() {
    var prevButton = document.getElementById('chair-prev-button');
    var nextButton = document.getElementById('chair-next-button');
    var productRow = document.getElementById('chair-row');

    if (prevButton && nextButton && productRow) {
        prevButton.addEventListener('click', function() {
            productRow.scrollBy({
                left: -600, // Adjust this value as needed
                behavior: 'smooth'
            });
        });

        nextButton.addEventListener('click', function() {
            productRow.scrollBy({
                left: 600, // Adjust this value as needed
                behavior: 'smooth'
            });
        });
    } else {
        console.warn('Elements for scroll functionality are not found on this page.');
    }
});

//   Use for second row in shop.html

document.addEventListener('DOMContentLoaded', function() {
    var prevButton = document.getElementById('sofa-prev-button');
    var nextButton = document.getElementById('sofa-next-button');
    var productRow = document.getElementById('sofa-row');

    if (prevButton && nextButton && productRow) {
        prevButton.addEventListener('click', function() {
            productRow.scrollBy({
                left: -600, // Adjust this value as needed
                behavior: 'smooth'
            });
        });

        nextButton.addEventListener('click', function() {
            productRow.scrollBy({
                left: 600, // Adjust this value as needed
                behavior: 'smooth'
            });
        });
    } else {
        console.warn('Elements for scroll functionality are not found on this page.');
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var prevButton = document.getElementById('table-prev-button');
    var nextButton = document.getElementById('table-next-button');
    var productRow = document.getElementById('table-row');

    if (prevButton && nextButton && productRow) {
        prevButton.addEventListener('click', function() {
            productRow.scrollBy({
                left: -600, // Adjust this value as needed
                behavior: 'smooth'
            });
        });

        nextButton.addEventListener('click', function() {
            productRow.scrollBy({
                left: 600, // Adjust this value as needed
                behavior: 'smooth'
            });
        });
    } else {
        console.warn('Elements for scroll functionality are not found on this page.');
    }
});

// Use of Checkout.html on radio button , whenever user click any radio button , automatically fill the 
function clickfun(cust) {
    console.log(cust.id);
    document.getElementById('c_fname').value = cust.first_name;
    document.getElementById('c_lname').value = cust.last_name;
    document.getElementById('c_companyname').value = cust.company_name;
    document.getElementById('c_address').value = cust.address;
    document.getElementById('c_state_country').value = cust.state;
    document.getElementById('c_postal_zip').value = cust.postal_zip;
    document.getElementById('c_email_address').value = cust.email_address;
    document.getElementById('c_phone').value = cust.phone;
    document.getElementById('c_order_notes').value = cust.order_notes;
}
>>>>>>> 1f2cbb7 (add payment gateway)
