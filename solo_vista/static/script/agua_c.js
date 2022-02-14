if(typeof(EventSource) !== "") {
    var source = new EventSource("/agua");
  
    source.onmessage = function(event) {
      document.getElementById("aguaDIV").innerHTML = event.data ;
    };
  
  } else {
    document.getElementById("aguaDIV").innerHTML = "no soportado para tu navegador...";
  }