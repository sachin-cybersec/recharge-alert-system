
// let isCountingDown = false; 
// let isCountingDo =false;
// function startCountdown()
//  {
//     if (isCountingDown)
//      {
//         alert("Your current plan is active");
//         return;
//      }
//     isCountingDown = true; 
//     let countdownValue = 10;
//     let countdownDisplay = document.getElementById("countdown-display");
//     let startButton = document.getElementById("start-button");          
//     startButton.disabled = true;           
//     let countdownInterval = setInterval(function() 
//     {
//         countdownDisplay.innerHTML = countdownValue;
//         countdownValue--;             
//         if (countdownValue < 0) 
//         {
//             clearInterval(countdownInterval);
//             alert("Alert! Your basic plan has been completed");                   
//             isCountingDown = false;
//             startButton.disabled = false;
//             countdownDisplay.innerHTML = "10";
//         }
//     }, 1000); 
// }

// //second

// function startCountdo()
//  {
//     if (isCountingDo,isCountingDown)
//      {
//         alert("Your current plan is active");
//         return;
//      }
//     isCountingDo = true; 
//     let countdownValue = 2419200;
//     let countdownDisplay = document.getElementById("countdown-displ");
//     let startButton = document.getElementById("start-butt");          
//     startButton.disabled = true;           
//     let countdownInterval = setInterval(function() 
//     {
//         countdownDisplay.innerHTML = countdownValue;
//         countdownValue--;             
//         if (countdownValue < 0) 
//         {
//             clearInterval(countdownInterval);
//             alert("Alert!Your premium plan has been ended");                   
//             isCountingDown = false;
//             startButton.disabled = false;
//             countdownDisplay.innerHTML = "2419200";
//         }
//     }, 1000); 
// }


// Function to show the popup
function showPopup() {
const popup = document.getElementById('popup');
popup.style.visibility = 'visible';
popup.style.opacity = '1';

// Automatically hide the popup after 2 seconds
setTimeout(() => {
popup.style.visibility = 'hidden';
popup.style.opacity = '0';
}, 2000);
}

