var DIRECT = "DIRECT";
var PROXY = "PROXY 165.22.105.204:8000"; //ip:port mitmproxy

var blocks = ["adguard", "googlevideo","mitm"]

function FindProxyForURL(url, host) {
  host = host.toLowerCase();
  for(var i = 0; i < blocks.length; i++){
    if(shExpMatch(host, "*" + blocks[i] + "*")){
      return PROXY;
    }
  }

  return DIRECT;
}
