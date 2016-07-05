var page = require('webpage').create(),
    system = require('system'),
    address;

page.open(system.args[1], function(status) {
    if (status !== 'success') {
    	console.log('Unable to access network');
  	} else {
		console.log(page.content);
  	}
  	phantom.exit();
});
