  const terminal = document.getElementById("terminal__body")
        setInterval(function() {
        var ws  = new WebSocket("ws://localhost:5000/echo")
          ws.onopen = function() {
           ws.send("warning");
       };
       ws.onmessage = function(evt) {
       var object = JSON.parse(evt.data);
            data = object.log
            var i;
            for (i = 0; i < data.length; i++) {
              terminal.innerHTML=data[i];
              terminal.style.color = 'white';
              console.log(data[i])
            }

          ws.close()

       };
       ws.onerror = function(evt) {
          console.log(evt)
          ws.close()
       };
        }, 1000)