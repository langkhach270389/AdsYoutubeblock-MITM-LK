var DIRECT = "DIRECT";
var PROXY = "PROXY 127.0.01:6969"; //ip:port mitmproxy

var blocks = ["googlevideo",
		"mitm",
		];

function FindProxyForURL(url, host) {
  host = host.toLowerCase();
  for(var i = 0; i < blocks.length; i++){
    if(shExpMatch(host, "*" + blocks[i] + "*")){
      return PROXY;
    }
  }

  return DIRECT;
}