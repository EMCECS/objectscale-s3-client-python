const nonResourceSubHeadings = [
	'client',
	'waiters',
	'paginators',
	'resources',
	'examples'
];
// Checks if an html doc name matches a service class name.
function isValidServiceName(serviceClassName) {
	const pageTitle = document.getElementsByTagName('h1')[0];
	const newDocName = pageTitle.getElementsByTagName('a')[0].innerHTML;
	return newDocName.toLowerCase() === serviceClassName;
}
// Checks if all elements of the split fragment are valid.
// Fragment items should only contain alphanumerics, hyphens, & underscores.
// A fragment should also only be redirected if it contain 3-5 items.
function isValidFragment(splitFragment) {
	const regex = /^[a-z0-9-_]+$/i;
	for (index in splitFragment) {
		if (!regex.test(splitFragment[index])) {
			return false;
		}
	}
	return splitFragment.length >= 1 && splitFragment.length < 5;
}
// Checks if a name is a possible resource name.
function isValidResource(name, serviceDocName) {
	return name.replaceAll('-', '') !== serviceDocName && !nonResourceSubHeadings.includes(name);
}
// Reroutes previously existing links to the new path.
// Old: <root_url>/reference/services/s3.html#S3.Client.delete_bucket
// New: <root_url>/reference/services/s3/client/delete_bucket.html
// This must be done client side since the fragment (#S3.Client.delete_bucket) is never
// passed to the server.
(function () {
	const currentPath = window.location.pathname.split('/');
	const fragment = window.location.hash.substring(1);
	const splitFragment = fragment.split('.').map(part => part.replace(/serviceresource/i, 'service-resource'));
	// Only redirect when viewing a top-level service page.
	if (isValidFragment(splitFragment) && currentPath[currentPath.length - 2] === 'services') {
		const serviceDocName = currentPath[currentPath.length - 1].replace('.html', '');
		if (splitFragment.length > 1) {
			splitFragment[0] = splitFragment[0].toLowerCase();
			splitFragment[1] = splitFragment[1].toLowerCase();
		}
		let newPath;
		if (splitFragment.length >= 3 && isValidServiceName(splitFragment[0])) {
			splitFragment[0] = serviceDocName;
			newPath = `${ splitFragment.slice(0, 3).join('/') }.html#${ splitFragment.length > 3 ? fragment : '' }`;
		} else if (splitFragment.length == 2 && isValidResource(splitFragment[1].toLowerCase(), serviceDocName)) {
			newPath = `${ splitFragment.join('/') }/index.html#${ fragment }`;
		} else if (splitFragment.length == 1 && isValidResource(splitFragment[0], serviceDocName)) {
			newPath = `${ serviceDocName }/${ splitFragment.join('/') }/index.html`;
		} else {
			return;
		}
		window.location.assign(newPath);
	}
}());