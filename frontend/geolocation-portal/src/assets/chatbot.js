(function(d, m){
    var kommunicateSettings = {
        "appId":"1647c4f916134918e167408dd9f8a6e4f",
        "popupWidget":true,
        "automaticChatOpenOnNavigation":true,
        "sessionTimeout": 0
      };
    var s = document.createElement("script"); s.type = "text/javascript"; s.async = true;
    s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
    var h = document.getElementsByTagName("head")[0]; h.appendChild(s);
    window.kommunicate = m; m._globals = kommunicateSettings;
  })(document, window.kommunicate || {});