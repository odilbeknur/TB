$(document).ready(function () {
    $('#calendar').fullCalendar({
        locale:'ru',
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month'
        },
        locale: 'ru',  // Set the locale to Russian
        events: function(start, end, timezone, callback) {
            $.ajax({
                url: '/all_events',
                dataType: 'json',
                success: function(data) {
                    var events = data.map(function(event) {
                        var color = event.status === 'outdated' ? '#fcc603' : '#03fc7b'; // Set color based on status
                        return {
                            title: event.title,
                            start: event.start,
                            end: event.end,
                            color: color,  // Set event color
                        };
                    });
                    callback(events);
                }
            });
        },
        selectable: true,
        selectHelper: true,
        editable: true,
        eventLimit: true,
    });
});