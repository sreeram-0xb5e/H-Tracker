var x = 0;
chrome.webRequest.onBeforeSendHeaders.addListener(function(details){

    chrome.tabs.getSelected(null,function(tab) {
        
        document.getElementById("url").value  = tab.url;
        document.getElementById("tabid").value = tab.id;
        document.getElementById("time").value = Date();
        if (x < 1)
        {
        document.getElementById('submit').click();
        x = x+1;
    	}
    });

    //document.getElementById("submit").click();
},{urls: [ "<all_urls>" ]},['requestHeaders','blocking']);
