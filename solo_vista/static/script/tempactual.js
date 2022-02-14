if(typeof(EventSource) !== "") {
  var source = new EventSource("/data");

  source.onmessage = function(event) {
    document.getElementById("myDIV").innerHTML = event.data ;
  };

} else {
  document.getElementById("myDIV").innerHTML = "no soportado para tu navegador...";
}
