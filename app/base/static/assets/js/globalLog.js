        const terminal = document.getElementById("terminal__body")
        setInterval(function() {
        var ws  = new WebSocket("ws://localhost:5000/echo")
          ws.onopen = function() {
           ws.send("global");
       };
       ws.onmessage = function(evt) {
       var object = JSON.parse(evt.data);
            data = object.log

            var i
            for (i = 0; i < data.length; i++) {
              console.log(data[i])
             var para = document.createElement("p");
              var node = document.createTextNode(data[i]);

                para.appendChild(node);
                para.style.color = "white";
                terminal.appendChild(para);

            }

          ws.close()

       };
       ws.onerror = function(evt) {
          console.log(evt)
          ws.close()
       };
        }, 5000)

