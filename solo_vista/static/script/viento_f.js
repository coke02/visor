if(typeof(EventSource) !== "") {
    var source = new EventSource("/viento");
  
    source.onmessage = function(event) {
      document.getElementById("vientoDIV").innerHTML = event.data ;
    };
  
  } else {
    document.getElementById("vientoDIV").innerHTML = "no soportado para tu navegador...";
  }