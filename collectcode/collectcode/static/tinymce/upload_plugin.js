tinymce.PluginManager.add('upload', function(editor, url) {
    // Add a button that opens a window
	editor.addButton('upload', {
		text: '上传',
		icon: false,
		onclick: function() {
			// Open window
			editor.windowManager.open({
				title: '上传图片',
				body: [
					{type: 'textbox', name: 'title', label: 'Title'}
				],
				onsubmit: function(e) {
					// Insert content when the window form is submitted
					editor.insertContent('Title: ' + e.data.title);
				}
			});
		}
	});

// Adds a menu item to the tools menu
//	editor.addMenuItem('example', {
//		text: 'Example plugin',
//		context: 'tools',
//		onclick: function() {
//			// Open window with a specific url
//			editor.windowManager.open({
//				title: 'TinyMCE site',
//				url: 'http://www.tinymce.com',
//				width: 400,
//				height: 300,
//				buttons: [{
//					text: 'Close',
//					onclick: 'close'
//				}]
//			});
//		}
//	});
});