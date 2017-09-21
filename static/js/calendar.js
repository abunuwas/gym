var weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

function makeCalendar() {
  var calendar = getElementById('calendar');
  var today = new Date();
  var days_in_month = new Date(today.getFullYear(), today.getMonth(), 0).getDate();
  var first_weekday_month = new Date(today.getFullYear(), today.getMonth(), 1)

}