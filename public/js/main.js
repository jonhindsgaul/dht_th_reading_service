// DOM Elements
const time = document.getElementById('time');
const greeting = document.getElementById('greeting');
const greetingName = document.getElementById('greeting_name');

// Show Time
function showTime() {
    let today = new Date(),
    hour = today.getHours(),
    min = today.getMinutes(),
    sec = today.getSeconds();

    time.innerHTML = `${hour}<span>:</span>${addZero(min)}<span>:</span>${addZero(sec)}`;

    setTimeout(showTime, 1000);
}

//Add zero
function addZero(n) {
    return (parseInt(n, 10) < 10 ? '0' : '') + n;
}

//Set background and greeting
function setBgGreet() {
    let today = new Date(),
      hour = today.getHours();
    
    if(hour<12) {
        //Morning
        document.body.style.backgroundImage = "url('../img/sunrise.jpg')";
        greeting.textContent = 'Good Morning';
    } else if(hour < 18) {
        // Afternoon
        document.body.style.backgroundImage = "url('../img/noon_riceterraces.jpg')";
        document.body.style.backgroundSize = "cover";
        greeting.textContent = 'Good Afternoon';
    } else {
        // Evening
        document.body.style.backgroundImage = "url('../img/night_sky.jpg')";
        greeting.textContent = 'Good Evening';
    }
    

}

//Run
showTime();
setBgGreet();

