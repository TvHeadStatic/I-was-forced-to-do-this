
var btn = document.querySelector("button");
var out = document.getElementById("output");


btn.addEventListener("click", grabWord);

function grabWord() {


  var TheShit = [
    'cat',
    'he shitted on the toilet',
    'black hole about to consume earth',
    'Meow meow',
    'Rock',
    'She shat her pants',
    'microwave',
    'proboscis',
    'Nicki Minaj',
    'WAS THAT THE BITE OF 87',
    'die',
    'that',
    'CHildren',
    'Happy tree friends',
    'Hippopotomonstrosesquippedaliophobia',
  ];
  var ShitThe = [
    'dog',
    'she sitted on the floor',
    'a star collapsing on its self',
    'Bork bork',
    'stone',
    'he shitted his trousers',
    'mmmmmmm',
    'femur',
    'Cupkkace',
    'BOAT DOG BOAT DOG BOAT DOG BOoOaAaT Dog',
    'respawn',
    'sunkissed',
    'vengence',
    'Smile Hd',
    'Pneumonoultramicroscopicsilicovolcanoconiosis',
  ];
 
   var wordNm = TheShit [Math.floor(Math.random() * TheShit.length)];
   var wordNum = ShitThe [Math.floor(Math.random() * ShitThe.length)];
   output.textContent = wordNm + ' gandalfed ' + wordNum; 
}

const x = 69;

function meth() {
    let y = parseFloat(document.getElementById("txt").value);
    let jphehe = [2* (x + y) ];
    document.getElementById("ansr").innerHTML = `${jphehe}`
}