var thrift = require('livetex-shtani');
var http = require('http');

var options = {
  //hostname: 'localhost',
  //hostname: '192.168.78.14',
  //hostname: 'sdk.livetex.ru',
  hostname: 'sdk-prerelease.livetex.ru',
  port: 30051,
  //path: '/account:5832:site:10005638:visitor:psuq6erx8brwl8fr',
  //path: '/account:5832:site:10005638:visitor:edww0pjo8pno2yb9',
  //path: '/account:123445:site:89200:visitor:ggrh5reh2cutmx6r',
  path: '/account:126927:site:91605:visitor:46ltgloqk0y919k9',
  method: 'GET'
};



/**
 * @implements {thrift.ISchema}
 * @constructor
 */
Schema = function() {

  /**
   * @type {!Object}
   */
  this.__structures = {
    'Employee': new thrift.definition.Structure({
      'employeeId': new thrift.definition.Field('employeeId', 1,
          thrift.definition.Type.STRING),
      'status': new thrift.definition.Field('status', 2,
          thrift.definition.Type.STRING),
      'firstname': new thrift.definition.Field('firstname', 3,
          thrift.definition.Type.STRING),
      'lastname': new thrift.definition.Field('lastname', 4,
          thrift.definition.Type.STRING),
      'avatar': new thrift.definition.Field('avatar', 5,
          thrift.definition.Type.STRING),
      'phone': new thrift.definition.Field('phone', 6,
          thrift.definition.Type.STRING),
      'email': new thrift.definition.Field('email', 7,
          thrift.definition.Type.STRING),
      'options': new thrift.definition.Field('options', 8,
          thrift.definition.Type.MAP,
          thrift.definition.Type.STRING,
          thrift.definition.Type.STRING)
    }),

    'Department': new thrift.definition.Structure({
      'departmentId': new thrift.definition.Field('departmentId', 1,
          thrift.definition.Type.STRING),
      'name': new thrift.definition.Field('name', 2,
          thrift.definition.Type.STRING),
      'options': new thrift.definition.Field('options', 3,
          thrift.definition.Type.MAP,
          thrift.definition.Type.STRING,
          thrift.definition.Type.STRING)
    }),

    'TypingMessage': new thrift.definition.Structure({
      'text': new thrift.definition.Field('text', 1,
          thrift.definition.Type.STRING)
    }),

    'HoldMessage': new thrift.definition.Structure({
      'text': new thrift.definition.Field('text', 1,
          thrift.definition.Type.STRING),
      'timestamp': new thrift.definition.Field('timestamp', 2,
          thrift.definition.Type.STRING)
    }),

    'TextMessage': new thrift.definition.Structure({
      'id': new thrift.definition.Field('id', 1,
          thrift.definition.Type.STRING),
      'text': new thrift.definition.Field('text', 2,
          thrift.definition.Type.STRING),
      'timestamp': new thrift.definition.Field('timestamp', 3,
          thrift.definition.Type.STRING),
      'sender': new thrift.definition.Field('sender', 4,
          thrift.definition.Type.STRING)
    }),

    'FileMessage': new thrift.definition.Structure({
      'id': new thrift.definition.Field('id', 1,
          thrift.definition.Type.STRING),
      'text': new thrift.definition.Field('text', 2,
          thrift.definition.Type.STRING),
      'timestamp': new thrift.definition.Field('timestamp', 3,
          thrift.definition.Type.STRING),
      'url': new thrift.definition.Field('url', 4,
          thrift.definition.Type.STRING),
      'sender': new thrift.definition.Field('sender', 5,
          thrift.definition.Type.STRING)
    }),

    'Conversation': new thrift.definition.Structure({
      'employeeId': new thrift.definition.Field('employeeId', 1,
          thrift.definition.Type.STRING),
      'departmentId': new thrift.definition.Field('departmentId', 2,
          thrift.definition.Type.STRING)
    }),

    'DialogState': new thrift.definition.Structure({
      'conversation': new thrift.definition.Field('conversation', 1,
          'Conversation'),
      'employee': new thrift.definition.Field('employee', 2,
          'Employee')
    })
  };

  /**
   * @type {!Object}
   */
  this.__methods = {
    'ban': new thrift.definition.Method({
      '1': new thrift.definition.Field('message', 1,
          thrift.definition.Type.STRING)
    }),

    'updateDialogState': new thrift.definition.Method({
      '1': new thrift.definition.Field('dialogState', 1,
          'DialogState')
    }),

    'receiveFileMessage': new thrift.definition.Method({
      '1': new thrift.definition.Field('message', 1,
          'FileMessage')
    }),

    'receiveTextMessage': new thrift.definition.Method({
      '1': new thrift.definition.Field('message', 1,
          'TextMessage')
    }),

    'confirmTextMessage': new thrift.definition.Method({
      '1': new thrift.definition.Field('messageId', 1,
          thrift.definition.Type.STRING)
    }),

    'receiveHoldMessage': new thrift.definition.Method({
      '1': new thrift.definition.Field('message', 1,
          'HoldMessage')
    }),

    'receiveTypingMessage': new thrift.definition.Method({
      '1': new thrift.definition.Field('message', 1,
          'TypingMessage')
    })
  };
};


/**
 * @inheritDoc
 */
Schema.prototype.getStructureDefinition = function(
    name) {
  return this.__structures[name] || null;
};


/**
 * @inheritDoc
 */
Schema.prototype.getMethodDefinition = function(
    name) {
  return this.__methods[name] || null;
};


/**
 * @inheritDoc
 */
Schema.prototype.createStructure = function(name,
    str) {
  return str;
};



function doRequest() {
  var time = Date.now();

	var req = http.request(options, function(res) {
		var parser = new thrift.Parser(new thrift.protocol.Binary(new Schema()));
    console.log('Status: ',res.statusCode);

		res.on('data', function(chunk) {
			console.log(require('util').inspect(parser.process(chunk), {depth: 15}));
		});

		res.on('end', function(){
      console.log('time is', Date.now() - time);
      doRequest();
    });
	});

	req.on('error', function(e) {
		console.log('problem with request:', e);
	});

	req.end();
}


doRequest();
