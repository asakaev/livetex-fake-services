var options = {
  hostname: 'localhost',
  port: 30051,
  path: '/account:5832:site:10005638:visitor:0arvucc7sx9u23xr',
  method: 'get'
};

require('http').request(options, function(res){
	res.on('data', function(chunk) {
		console.log(chunk)
	})

	res.on('end', function() {
		console.log('end')
	})
}).end('http://127.0.0.1:10040/');