var geocoder;

function initialize() {
    geocoder = new google.maps.Geocoder();
    var default_latlng = new google.maps.LatLng(0,0);
    var myOptions = {
        zoom: 2,
        center: default_latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map"), myOptions);
    
    if (navigator.geolocation) navigator.geolocation.getCurrentPosition(function(position) {
        var my_latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
        map.setCenter(my_latlng);
        map.setZoom(6);
    });
    
    $.ajax({
        'url': '/locations.json',
        'type': 'GET',
        'dataType': 'json',
        'success': function(data) {
            $.each(data, function(i) {
                var location = this;
                if (!location.latitude || !location.longitude) {
                    geocoder.geocode({
                        'address': location.address
                    }, function(results, status) {
                        if (results[0]) addMarker(results[0].geometry.location.a, results[0].geometry.location.b, location);
                    });
                } else {
                    addMarker(location.latitude, location.longitude, location);
                }
            });
        }
    });
    
    function addMarker(lat,lng,location) {
        var marker_latlng = new google.maps.LatLng(lat, lng);
        var marker = new google.maps.Marker({
            position: marker_latlng,
            map: map, 
            title: location.location_name
        });
        var info = '<div class="info">';
        if (location.location_name) info += '<strong>' + location.location_name + '</strong><br/>' + location.contact_name;
        else info += '<strong>' + location.contact_name + '</strong>';
        info += '<div class="type">' + location.type_display + '</div>';
        info += '<div class="address">' + location.address + '</div>';
        if (location.website) info += '<div class="website"><a href="' + location.website + '" target="_blank">' + location.website + '</a></div>';
        if (location.twitter) info += '<div class="twitter"><a href="http://twitter.com/' + location.twitter + '" target="_blank">@' + location.twitter + '</a></div>';
        info += '</div>';
        var infowindow = new google.maps.InfoWindow({
            content: info
        });
        google.maps.event.addListener(marker, 'click', function() {
            infowindow.open(map, marker);
        });
    }
}


$(window).load(initialize);

$(document).ready(function() {
    $('a[href="#add"]').click(function(e) {
        e.preventDefault();
        $('#add').toggle('slow');
    });
    $('#id_address').bind('blur', function() {
        var field = this;
        geocoder.geocode({
            'address': $(this).val()
        }, function(results, status) {
            if (results[0]) {
                $('#id_latitude').val(results[0].geometry.location.a);
                $('#id_longitude').val(results[0].geometry.location.b);
                $(field).addClass('geocode-ok');
            } else {
                $(field).addClass('geocode-fail');
            }
        });
        
    });
    $('#add form').submit(function(e) {
        e.preventDefault();
        $.ajax({
            'url': $(this).attr('action'),
            'type': 'POST',
            'data': $.param($('input,select,textarea', this)),
            'success': function(data) {
                if (data.status == 'INVALID') {
                    alert('Some data did not validate. Please double-check.');
                } else if (data.status == 'OK') {
                    $('#add').hide('slow');
                }
            },
            'dataType': 'json'
        });
    });
});