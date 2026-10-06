document.addEventListener("DOMContentLoaded", function () {

    detectUserLocation();

});


function detectUserLocation() {

    const statusElement =
        document.getElementById("location-status");

    const searchStatusElement =
        document.getElementById(
            "search-location-status"
        );

    const hospitalStatusElement =
        document.getElementById(
            "hospital-location-status"
        );


    if (!navigator.geolocation) {

        updateLocationMessage(
            "Location is not supported by this browser."
        );

        return;
    }


    updateLocationMessage(
        "Requesting your current location..."
    );


    navigator.geolocation.getCurrentPosition(

        function (position) {

            const latitude =
                position.coords.latitude;

            const longitude =
                position.coords.longitude;


            console.log(
                "Latitude:",
                latitude
            );

            console.log(
                "Longitude:",
                longitude
            );


            const searchLatitude =
                document.getElementById(
                    "search-latitude"
                );

            const searchLongitude =
                document.getElementById(
                    "search-longitude"
                );


            if (searchLatitude) {

                searchLatitude.value =
                    latitude;
            }


            if (searchLongitude) {

                searchLongitude.value =
                    longitude;
            }


            const hospitalLatitude =
                document.getElementById(
                    "hospital-latitude"
                );

            const hospitalLongitude =
                document.getElementById(
                    "hospital-longitude"
                );


            if (hospitalLatitude) {

                hospitalLatitude.value =
                    latitude;
            }


            if (hospitalLongitude) {

                hospitalLongitude.value =
                    longitude;
            }


            updateLocationMessage(
                "Location detected successfully."
            );


            if (searchStatusElement) {

                searchStatusElement.innerHTML =
                    "Location detected successfully.";
            }


            if (hospitalStatusElement) {

                hospitalStatusElement.innerHTML =
                    "Hospital location detected successfully.";
            }

        },


        function (error) {

            let message =
                "Unable to get your location.";


            if (error.code === 1) {

                message =
                    "Location permission was denied. Please allow location access in your browser.";

            } else if (error.code === 2) {

                message =
                    "Your location is currently unavailable.";

            } else if (error.code === 3) {

                message =
                    "Location request timed out.";
            }


            updateLocationMessage(message);


            if (searchStatusElement) {

                searchStatusElement.innerHTML =
                    message;
            }


            if (hospitalStatusElement) {

                hospitalStatusElement.innerHTML =
                    message;
            }

        },

        {
            enableHighAccuracy: true,

            timeout: 10000,

            maximumAge: 0
        }

    );

}


function updateLocationMessage(message) {

    const statusElement =
        document.getElementById(
            "location-status"
        );

    if (statusElement) {

        statusElement.innerHTML =
            message;
    }

}