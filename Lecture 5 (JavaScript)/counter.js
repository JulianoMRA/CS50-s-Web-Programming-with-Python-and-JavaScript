let counter = 0;

function count() {
    counter++;
    heading = document.querySelector('h1');
    heading.innerHTML = counter;

    if (counter % 10 == 0) {
        alert(`Count is now ${counter}`);
    }
}

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = count;
});