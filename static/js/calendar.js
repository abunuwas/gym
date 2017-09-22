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
  var calendar = document.getElementById('calendar');
  var today = new Date();
  var days_in_month = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate();
  var first_weekday_month = new Date(today.getFullYear(), today.getMont(), 1).getDay();
}


function drawCalendar() {
  var table = document.createElement("table");
  table.setAttribute("id", "test");
  table.style.backgroundColor = "black";
  var calendar_holder = document.getElementById("calendar");
  calendar_holder.appendChild(table);
  var newRow = table.insertRow();
  for (var i=0; i<7; i++) {
    var newCell = newRow.insertCell();
    newCell.style.backgroundColor = 'green';
    var newDiv = document.createElement("div");
    var newText = document.createTextNode(i);
    newDiv.appendChild(newText);
    newCell.appendChild(newDiv);
    newCell.addEventListener("click", function() { alert("Hello World!")})
  }
}


function sendDayData() {

}

drawCalendar();

