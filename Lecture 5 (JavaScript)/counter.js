let counter = 0;

function count() {
    counter++;
    heading = document.querySelector('h1');
    heading.innerHTML = counter;
}

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = count;

    setInterval(count, 1000);
});