name = input('what would you like to name the Web GL File? ')

myoSwitch = input('Is the Web GL for a Myocardium or a regular heart? type yes for Myocardium or no if not ')

if myoSwitch == "yes":

    f = open(name, 'w')
    message = """<!DOCTYPE html>
<html lang="en">

<head>
	<title>2018001 Myocardium</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
	<!--<link type="text/css" rel="stylesheet" href="index.css">-->
	<style>
		body {
			/*background-color: #ccc;*/
			background-color: black;
			color: #000;
		}

		a {
			color: #f00;
		}

		.fontanMyo{
			background-color: pink;
			border: 1px orange solid;
			color: white;
			padding: 10px 24px; 
			cursor: pointer;
		}

		.highRes {
			background-color: blue; 
			border: 1px blue solid; 
			color: white; 
			padding: 10px 24px;
			cursor: pointer;
		}

	</style>
</head>

<body>


	<!--<div class="dropdown">
  <button class="dropbtn">2018001 FONTAN 1 Heart</button>
  <div class="dropdown-content">


    <a type="button" id="hideShow2">Hide / Show Pulmonary Artery</a>
    <a type="button" id="hideShow3">Hide / Show Left Atrium</a>
    <a type="button" id="hideShow4">Hide / Show Right Atrium</a>
    <a type="button" id="hideShow5">Hide / Show Left Ventricle</a>
    <a type="button" id="hideShow6">Hide / Show 2018001</a>
		<a type="button" id="hideShow7" >Delete 2018001</a>
  </div>
</div>-->

	<!--<button class="aorta" id="hideShow">Hide / Show Aorta</button>
	<button class="pulmonaryArtery" id="hideShow2">Hide / Show Pulmonary Artery</button>
	<button class="leftAtrium" id="hideShow3">Hide / Show Left Atrium</button>
	<button class="rightAtrium" id="hideShow4">Hide / Show Right Atrium</button>
	<button class="leftVentricle" id="hideShow5">Hide / Show Left Ventricle</button>
	<button class="rightVentricle" id = "hideShow6">Hide / Show Right Ventricle</button>-->

	<!--<button type="button" id="hideShow9" onclick="hide2018001()">Hide buttons</button>
		<form> <input type="checkbox" id="myCheck" onclick="hide2018002"> Toggle 2018002 </form>
		<form> <input type = "checkbox" id = "myCheck2" onclick="alert('you clicked')"> Toggle 2018003 </form>-->

		<button class = "fontanMyo" id = "hideShow">Hide / Show 2018001-01 Myocardium</button>
		<button class = "highRes" onclick="document.location = 'https://github.com/sachx1/TorontoHeartAtlas/blob/master/2018001MYO/2018001Myocard.obj'"> High Resolution Myocardium Download</button>

	<script src="three.js"></script>
	<script src="OrbitControls.js"></script>
	
	<script src="OBJLoader.js"></script>
	<script src="WebGL.js"></script>


	<script>
		//<script src="GLTFLoader.js">
		if (WEBGL.isWebGLAvailable() === false) {

			document.body.appendChild(WEBGL.getWebGLErrorMessage());

		}

		function hide2018001() {
			var x = document.getElementById("info2");
			if (x.style.display === "none") {
				x.style.display = "block";
			} else {
				x.style.display = "none";
			}
		}

		function hide2018002() {
			var y = document.getElementById("2018002");
			if (y.style.display === "block") {
				y.style.display = "none";
			} else {
				y.style.display = "block";
			}
		}


		var camera, controls, scene, renderer, object, object2, object3, object4, object5;
		var objhidden = false;
		init();
		//render(); // remove when using next line for animation loop (requestAnimationFrame)
		animate();

		function init() {

			scene = new THREE.Scene();
			scene.background = new THREE.Color(0x000000);
			// scene.fog = new THREE.FogExp2( 0xcccccc, 0 );

			renderer = new THREE.WebGLRenderer({
				antialias: true
			});
			renderer.setPixelRatio(window.devicePixelRatio);
			renderer.setSize(window.innerWidth, window.innerHeight);
			document.body.appendChild(renderer.domElement);

			camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);
			camera.position.set(0, 0, -400);

			// controls

			controls = new THREE.OrbitControls(camera, renderer.domElement);

			//controls.addEventListener( 'change', render ); // call this only in static scenes (i.e., if there is no animation loop)

			controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
			controls.dampingFactor = 0.25;

			controls.screenSpacePanning = false;

			controls.minDistance = 100;
			controls.maxDistance = 500;

			controls.maxPolarAngle = Math.PI;

			// world

			// var geometry = new THREE.CylinderBufferGeometry( 0, 10, 30, 4, 1 );
			// var material = new THREE.MeshPhongMaterial( { color: 0xffffff, flatShading: true } );
			//
			// for ( var i = 0; i < 500; i ++ ) {
			//
			// 	var mesh = new THREE.Mesh( geometry, material );
			// 	mesh.position.x = Math.random() * 1600 - 800;
			// 	mesh.position.y = 0;
			// 	mesh.position.z = Math.random() * 1600 - 800;
			// 	mesh.updateMatrix();
			// 	mesh.matrixAutoUpdate = false;
			// 	scene.add( mesh );
			//
			// }

			var oLoader = new THREE.OBJLoader();

			oLoader.load('2018001Myocard.obj', function(object, materials) {

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0xFFC0CB
				});

				object.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object.position.x = 0;
				object.position.y = 0;
				object.position.z = 0;

				object.scale.set(1, 1, 1);
				scene.add(object);

				document.getElementById('hideShow').addEventListener('click', function() {
					object.visible = !object.visible;
				});
			});

			// lights

			var light = new THREE.DirectionalLight(0xffffff, 1);
			light.position.set(1, 1, 1);
			scene.add(light);

			var light = new THREE.DirectionalLight(0x002288, 1);
			light.position.set(-1, -1, -1);
			scene.add(light);

			var light = new THREE.DirectionalLight(0xffffff, 1);
			light.position.set(-1, -1, -90);
			scene.add(light);

			// var light = new THREE.DirectionalLight(0xffffff, 2);
			// light.position.set(-1, -90, -90);
			// scene.add(light);
			//
			var light = new THREE.DirectionalLight(0xffffff, 1);
			light.position.set(-50, -30, 40);
			scene.add(light);

			// mesh4.position.z = -50;
			// mesh4.position.y = -30;
			// mesh4.position.x = -50;

			// var light = new THREE.AmbientLight(0x222222, 2);
			// scene.add(light);

			//

			window.addEventListener('resize', onWindowResize, false);

		}

		function onWindowResize() {

			camera.aspect = window.innerWidth / window.innerHeight;
			camera.updateProjectionMatrix();

			renderer.setSize(window.innerWidth, window.innerHeight);

		}

		function animate() {

			requestAnimationFrame(animate);

			controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true

			render();

		}

		function render() {

			renderer.render(scene, camera);

		}
	</script>

</body>

</html>

 """
    f.write(message)
    f.close()
    exit()

choice = input('How many objs or stls are there for the model? ')

f = open(name,'w')

if choice =='3':
    message= """<!DOCTYPE html>
<html lang="en">

<head>
	<title>*Insert title here*</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
	<!--<link type="text/css" rel="stylesheet" href="index.css">-->
	<style>
		body {
			/*background-color: #ccc;*/
			background-color: black;
			color: #000;
		}

		a {
			color: #f00;
		}

		.aorta {
			background-color: #FFFF00;
			/* Yellow background */
			border: 1px solid yellow;
			/* yellow border */
			color: black;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */

		}

		.atriaVentricle {
			background-color: red;
			/* Green background */
			border: 1px solid red;
			/* Green border */
			color: white;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */

		}

		.venaCava {
			background-color:  blue;
			/* Orange background */
			border: 1px solid blue;
			/* Orange border */
			color: white;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */
		}

	</style>
</head>

<body>


	<!--<div class="dropdown">
  <button class="dropbtn">2018001 FONTAN 1 Heart</button>
  <div class="dropdown-content">


    <a type="button" id="hideShow2">Hide / Show Pulmonary Artery</a>
    <a type="button" id="hideShow3">Hide / Show Left Atrium</a>
    <a type="button" id="hideShow4">Hide / Show Right Atrium</a>
    <a type="button" id="hideShow5">Hide / Show Left Ventricle</a>
    <a type="button" id="hideShow6">Hide / Show 2018001</a>
		<a type="button" id="hideShow7" >Delete 2018001</a>
  </div>
</div>-->

	<button class="aorta" id="hideShow">Hide / Show Aorta</button>
	<button class="atriaVentricle" id="hideShow2">Hide / Show Atria Ventricle</button>
	<button class="venaCava" id="hideShow3">Hide / Show Vena Cava</button>
	

	<!--<button type="button" id="hideShow9" onclick="hide2018001()">Hide buttons</button>
		<form> <input type="checkbox" id="myCheck" onclick="hide2018002"> Toggle 2018002 </form>
		<form> <input type = "checkbox" id = "myCheck2" onclick="alert('you clicked')"> Toggle 2018003 </form>-->

	<script src="three.js"></script>
	<script src="OrbitControls.js"></script>
	<script src="GLTFLoader.js"></script>
	<script src="OBJLoader.js"></script>
	<script src="WebGL.js"></script>


	<script>
		if (WEBGL.isWebGLAvailable() === false) {

			document.body.appendChild(WEBGL.getWebGLErrorMessage());

		}

		function hide2018001() {
			var x = document.getElementById("info2");
			if (x.style.display === "none") {
				x.style.display = "block";
			} else {
				x.style.display = "none";
			}
		}

		function hide2018002() {
			var y = document.getElementById("2018002");
			if (y.style.display === "block") {
				y.style.display = "none";
			} else {
				y.style.display = "block";
			}
		}


		var camera, controls, scene, renderer, object, object2, object3, object4, object5;
		var objhidden = false;
		init();
		//render(); // remove when using next line for animation loop (requestAnimationFrame)
		animate();

		function init() {

			scene = new THREE.Scene();
			scene.background = new THREE.Color(0x000000);
			// scene.fog = new THREE.FogExp2( 0xcccccc, 0 );

			renderer = new THREE.WebGLRenderer({
				antialias: true
			});
			renderer.setPixelRatio(window.devicePixelRatio);
			renderer.setSize(window.innerWidth, window.innerHeight);
			document.body.appendChild(renderer.domElement);

			camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);
			camera.position.set(0, 0, -400);

			// controls

			controls = new THREE.OrbitControls(camera, renderer.domElement);

			//controls.addEventListener( 'change', render ); // call this only in static scenes (i.e., if there is no animation loop)

			controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
			controls.dampingFactor = 0.25;

			controls.screenSpacePanning = false;

			controls.minDistance = 100;
			controls.maxDistance = 500;

			controls.maxPolarAngle = Math.PI;

			// world

			// var geometry = new THREE.CylinderBufferGeometry( 0, 10, 30, 4, 1 );
			// var material = new THREE.MeshPhongMaterial( { color: 0xffffff, flatShading: true } );
			//
			// for ( var i = 0; i < 500; i ++ ) {
			//
			// 	var mesh = new THREE.Mesh( geometry, material );
			// 	mesh.position.x = Math.random() * 1600 - 800;
			// 	mesh.position.y = 0;
			// 	mesh.position.z = Math.random() * 1600 - 800;
			// 	mesh.updateMatrix();
			// 	mesh.matrixAutoUpdate = false;
			// 	scene.add( mesh );
			//
			// }

			var oLoader = new THREE.OBJLoader();

			var oLoader2 = new THREE.OBJLoader();

			var oLoader3 = new THREE.OBJLoader();

			oLoader.load('extra_ao.obj', function(object, materials) {

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0xa65e00
				});

				object.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object.position.x = 0;
				object.position.y = 0;
				object.position.z = 0;

				object.scale.set(1, 1, 1);
				scene.add(object);

				document.getElementById('hideShow').addEventListener('click', function() {
					object.visible = !object.visible;
				});
			});

			oLoader2.load('extra_av.obj', function(object2, materials) {

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0xff0000
				});

				object2.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object2.position.x = 0;
				object2.position.y = 0;
				object2.position.z = 0;
				object2.scale.set(1, 1, 1);
				scene.add(object2);

				document.getElementById('hideShow2').addEventListener('click', function() {
					object2.visible = !object2.visible;
				});

			});

			oLoader3.load('extra_vc.obj', function(object3, materials) {

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0x0000ff
				});

				object3.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object3.position.x = 0;
				object3.position.y = 0;
				object3.position.z = 0;
				object3.scale.set(1, 1, 1);
				scene.add(object3);

				document.getElementById('hideShow3').addEventListener('click', function() {
					object3.visible = !object3.visible;
				});
			});

		

			// lights

			var light = new THREE.DirectionalLight(0xffffff, 2);
			light.position.set(1, 1, 1);
			scene.add(light);

			var light = new THREE.DirectionalLight(0x002288, 1);
			light.position.set(-1, -1, -1);
			scene.add(light);

			var light = new THREE.DirectionalLight(0xffffff, 1);
			light.position.set(-1, -1, -90);
			scene.add(light);

			// var light = new THREE.DirectionalLight(0xffffff, 2);
			// light.position.set(-1, -90, -90);
			// scene.add(light);
			//
			var light = new THREE.DirectionalLight(0xffffff, 1);
			light.position.set(-50, -30, 40);
			scene.add(light);

			// mesh4.position.z = -50;
			// mesh4.position.y = -30;
			// mesh4.position.x = -50;

			// var light = new THREE.AmbientLight(0x222222, 2);
			// scene.add(light);

			//

			window.addEventListener('resize', onWindowResize, false);

		}

		function onWindowResize() {

			camera.aspect = window.innerWidth / window.innerHeight;
			camera.updateProjectionMatrix();

			renderer.setSize(window.innerWidth, window.innerHeight);

		}

		function animate() {

			requestAnimationFrame(animate);

			controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true

			render();

		}

		function render() {

			renderer.render(scene, camera);

		}
	</script>

</body>

</html>
 """
    
if choice == '4':
    message = """<!DOCTYPE html>
<html lang="en">

<head>
	<title>*Insert Title Here*</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
	<!--<link type="text/css" rel="stylesheet" href="index.css">-->
	<style>
		body {
			/*background-color: #ccc;*/
			background-color: black;
			color: rgba(20, 228, 99, 0.993);
		}

		a {
			color: #f00;
		}

		.aorta {
			background-color: #FFFF00;
			/* Yellow background */
			border: 1px solid yellow;
			/* yellow border */
			color: black;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */

		}

		.pulmonaryArtery {
			background-color: #4CAF50;
			/* Green background */
			border: 1px solid green;
			/* Green border */
			color: white;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */

		}

		.leftAtrium {
			background-color: #FFA500;
			/* Orange background */
			border: 1px solid orange;
			/* Orange border */
			color: white;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */
		}

		.rightAtrium {
			background-color: #add8e6;
			/* Light Blue background */
			border: 1px solid lightBlue;
			/* Light Blue border */
			color: white;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */
		}

		.leftVentricle {
			background-color: #ff0000;
			/* Red background */
			border: 1px solid red;
			/* Red border */
			color: white;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */
		}

		.rightVentricle{
			background-color: #0000ff; /* Blue background */
			border: 1px solid Blue; /* Red border */
			color: white; /* White text */
			padding: 10px 24px; /* Some padding */
			cursor: pointer; /* Pointer/hand icon */
		}

	</style>
</head>

<body>


	<!--<div class="dropdown">
  <button class="dropbtn">2018001 FONTAN 1 Heart</button>
  <div class="dropdown-content">


    <a type="button" id="hideShow2">Hide / Show Pulmonary Artery</a>
    <a type="button" id="hideShow3">Hide / Show Left Atrium</a>
    <a type="button" id="hideShow4">Hide / Show Right Atrium</a>
    <a type="button" id="hideShow5">Hide / Show Left Ventricle</a>
    <a type="button" id="hideShow6">Hide / Show 2018001</a>
		<a type="button" id="hideShow7" >Delete 2018001</a>
  </div>
</div>-->

	<button class="aorta" id="hideShow">Hide / Show Aorta</button>
	<button class="pulmonaryArtery" id="hideShow2">Hide / Show Pulmonary Artery</button>
	<button class="leftAtrium" id="hideShow3">Hide / Show Left Atrium & Left Ventricle</button>
	<button class="rightAtrium" id="hideShow4">Hide / Show Right Atrium & Right Ventricle</button>
	

	<!--<button type="button" id="hideShow9" onclick="hide2018001()">Hide buttons</button>
		<form> <input type="checkbox" id="myCheck" onclick="hide2018002"> Toggle 2018002 </form>
		<form> <input type = "checkbox" id = "myCheck2" onclick="alert('you clicked')"> Toggle 2018003 </form>-->

	<script src="three.js"></script>
	<script src="OrbitControls.js"></script>
	<script src="GLTFLoader.js"></script>
	<script src="OBJLoader.js"></script>
	<script src="WebGL.js"></script>


	<script>
		if (WEBGL.isWebGLAvailable() === false) {

			document.body.appendChild(WEBGL.getWebGLErrorMessage());

		}

		function hide2018001() {
			var x = document.getElementById("info2");
			if (x.style.display === "none") {
				x.style.display = "block";
			} else {
				x.style.display = "none";
			}
		}

		function hide2018002() {
			var y = document.getElementById("2018002");
			if (y.style.display === "block") {
				y.style.display = "none";
			} else {
				y.style.display = "block";
			}
		}


		var camera, controls, scene, renderer, object, object2, object3, object4, object5;
		var objhidden = false;
		init();
		//render(); // remove when using next line for animation loop (requestAnimationFrame)
		animate();

		function init() {

			scene = new THREE.Scene();
			scene.background = new THREE.Color(0x000000);
			// scene.fog = new THREE.FogExp2( 0xcccccc, 0 );

			renderer = new THREE.WebGLRenderer({
				antialias: true
			});
			renderer.setPixelRatio(window.devicePixelRatio);
			renderer.setSize(window.innerWidth, window.innerHeight);
			document.body.appendChild(renderer.domElement);

			camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);
			camera.position.set(0, 0, -400);

			// controls

			controls = new THREE.OrbitControls(camera, renderer.domElement);

			//controls.addEventListener( 'change', render ); // call this only in static scenes (i.e., if there is no animation loop)

			controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
			controls.dampingFactor = 0.25;

			controls.screenSpacePanning = false;

			controls.minDistance = 100;
			controls.maxDistance = 500;

			controls.maxPolarAngle = Math.PI;

			// world

			// var geometry = new THREE.CylinderBufferGeometry( 0, 10, 30, 4, 1 );
			// var material = new THREE.MeshPhongMaterial( { color: 0xffffff, flatShading: true } );
			//
			// for ( var i = 0; i < 500; i ++ ) {
			//
			// 	var mesh = new THREE.Mesh( geometry, material );
			// 	mesh.position.x = Math.random() * 1600 - 800;
			// 	mesh.position.y = 0;
			// 	mesh.position.z = Math.random() * 1600 - 800;
			// 	mesh.updateMatrix();
			// 	mesh.matrixAutoUpdate = false;
			// 	scene.add( mesh );
			//
			// }

			var oLoader = new THREE.OBJLoader();

			var oLoader2 = new THREE.OBJLoader();

			var oLoader3 = new THREE.OBJLoader();

			var oLoader4 = new THREE.OBJLoader();

			

			oLoader.load('2018018_AO_Aligned.obj', function(object, materials) { //ao

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0xa65e00
				});

				object.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object.position.x = 0;
				object.position.y = 0;
				object.position.z = 0;

				object.scale.set(1, 1, 1);
				scene.add(object);

				document.getElementById('hideShow').addEventListener('click', function() {
					object.visible = !object.visible;
				});
			});

			oLoader2.load('2018018_PA_Aligned.obj', function(object2, materials) { //pa

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0x008000
				});

				object2.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object2.position.x = 0;
				object2.position.y = 0;
				object2.position.z = 0;
				object2.scale.set(1, 1, 1);
				scene.add(object2);

				document.getElementById('hideShow2').addEventListener('click', function() {
					object2.visible = !object2.visible;
				});

			});

			oLoader3.load('2018018_LALV_Aligned.obj', function(object3, materials) { //la

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0xFF4500
				});

				object3.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object3.position.x = 0;
				object3.position.y = 0;
				object3.position.z = 0;
				object3.scale.set(1, 1, 1);
				scene.add(object3);

				document.getElementById('hideShow3').addEventListener('click', function() {
					object3.visible = !object3.visible;
				});
			});

			oLoader4.load('2018018_RARV_Aligned.obj', function(object4, materials) { //ra

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0x1e90ff
				});

				object4.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object4.position.x = 0;
				object4.position.y = 0;
				object4.position.z = 0;
				object4.scale.set(1, 1, 1);
				scene.add(object4);

				document.getElementById('hideShow4').addEventListener('click', function() {
					object4.visible = !object4.visible;
				});
			});
			

			// lights

			var light = new THREE.DirectionalLight(0xffffff, 2);
			light.position.set(1, 1, 1);
			scene.add(light);

			var light = new THREE.DirectionalLight(0x002288, 1);
			light.position.set(-1, -1, -1);
			scene.add(light);

			var light = new THREE.DirectionalLight(0xffffff, 1);
			light.position.set(-1, -1, -90);
			scene.add(light);

			// var light = new THREE.DirectionalLight(0xffffff, 2);
			// light.position.set(-1, -90, -90);
			// scene.add(light);
			//
			var light = new THREE.DirectionalLight(0xffffff, 1);
			light.position.set(-50, -30, 40);
			scene.add(light);

			// mesh4.position.z = -50;
			// mesh4.position.y = -30;
			// mesh4.position.x = -50;

			var light = new THREE.AmbientLight(0x222222, 1);
			scene.add(light);

			//

			window.addEventListener('resize', onWindowResize, false);

		}

		function onWindowResize() {

			camera.aspect = window.innerWidth / window.innerHeight;
			camera.updateProjectionMatrix();

			renderer.setSize(window.innerWidth, window.innerHeight);

		}

		function animate() {

			requestAnimationFrame(animate);

			controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true

			render();

		}

		function render() {

			renderer.render(scene, camera);

		}
	</script>

</body>

</html>
 """

if choice == '5':

    message = """<!DOCTYPE html>
<html lang="en">

<head>
	<title>*Insert Title Here*</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
	<!--<link type="text/css" rel="stylesheet" href="index.css">-->
	<style>
		body {
			/*background-color: #ccc;*/
			background-color: black;
			color: #000;
		}

		a {
			color: #f00;
		}

		.aorta {
			background-color: #FFFF00;
			/* Yellow background */
			border: 1px solid yellow;
			/* yellow border */
			color: black;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */

		}

		.pulmonaryArtery {
			background-color: #4CAF50;
			/* Green background */
			border: 1px solid green;
			/* Green border */
			color: white;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */

		}

		.leftAtrium {
			background-color: #FFA500;
			/* Orange background */
			border: 1px solid orange;
			/* Orange border */
			color: white;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */
		}

		.rightAtrium {
			background-color: #add8e6;
			/* Light Blue background */
			border: 1px solid lightBlue;
			/* Light Blue border */
			color: white;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */
		}

		.leftVentricle {
			background-color: #ff0000;
			/* Red background */
			border: 1px solid red;
			/* Red border */
			color: white;
			/* White text */
			padding: 10px 24px;
			/* Some padding */
			cursor: pointer;
			/* Pointer/hand icon */
		}

	</style>
</head>

<body>


	<!--<div class="dropdown">
  <button class="dropbtn">2018001 FONTAN 1 Heart</button>
  <div class="dropdown-content">


    <a type="button" id="hideShow2">Hide / Show Pulmonary Artery</a>
    <a type="button" id="hideShow3">Hide / Show Left Atrium</a>
    <a type="button" id="hideShow4">Hide / Show Right Atrium</a>
    <a type="button" id="hideShow5">Hide / Show Left Ventricle</a>
    <a type="button" id="hideShow6">Hide / Show 2018001</a>
		<a type="button" id="hideShow7" >Delete 2018001</a>
  </div>
</div>-->

	<button class="aorta" id="hideShow">Hide / Show Aorta</button>
	<button class="pulmonaryArtery" id="hideShow2">Hide / Show Pulmonary Artery</button>
	<button class="leftAtrium" id="hideShow3">Hide / Show Left Atrium</button>
	<button class="rightAtrium" id="hideShow4">Hide / Show Right Atrium</button>
	<button class="leftVentricle" id="hideShow5">Hide / Show Left Ventricle</button>

	<!--<button type="button" id="hideShow9" onclick="hide2018001()">Hide buttons</button>
		<form> <input type="checkbox" id="myCheck" onclick="hide2018002"> Toggle 2018002 </form>
		<form> <input type = "checkbox" id = "myCheck2" onclick="alert('you clicked')"> Toggle 2018003 </form>-->

	<script src="three.js"></script>
	<script src="OrbitControls.js"></script>
	<script src="GLTFLoader.js"></script>
	<script src="OBJLoader.js"></script>
	<script src="WebGL.js"></script>


	<script>
		if (WEBGL.isWebGLAvailable() === false) {

			document.body.appendChild(WEBGL.getWebGLErrorMessage());

		}

		function hide2018001() {
			var x = document.getElementById("info2");
			if (x.style.display === "none") {
				x.style.display = "block";
			} else {
				x.style.display = "none";
			}
		}

		function hide2018002() {
			var y = document.getElementById("2018002");
			if (y.style.display === "block") {
				y.style.display = "none";
			} else {
				y.style.display = "block";
			}
		}


		var camera, controls, scene, renderer, object, object2, object3, object4, object5;
		var objhidden = false;
		init();
		//render(); // remove when using next line for animation loop (requestAnimationFrame)
		animate();

		function init() {

			scene = new THREE.Scene();
			scene.background = new THREE.Color(0x000000);
			// scene.fog = new THREE.FogExp2( 0xcccccc, 0 );

			renderer = new THREE.WebGLRenderer({
				antialias: true
			});
			renderer.setPixelRatio(window.devicePixelRatio);
			renderer.setSize(window.innerWidth, window.innerHeight);
			document.body.appendChild(renderer.domElement);

			camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);
			camera.position.set(0, 0, -400);

			// controls

			controls = new THREE.OrbitControls(camera, renderer.domElement);

			//controls.addEventListener( 'change', render ); // call this only in static scenes (i.e., if there is no animation loop)

			controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
			controls.dampingFactor = 0.25;

			controls.screenSpacePanning = false;

			controls.minDistance = 100;
			controls.maxDistance = 500;

			controls.maxPolarAngle = Math.PI;

			// world

			// var geometry = new THREE.CylinderBufferGeometry( 0, 10, 30, 4, 1 );
			// var material = new THREE.MeshPhongMaterial( { color: 0xffffff, flatShading: true } );
			//
			// for ( var i = 0; i < 500; i ++ ) {
			//
			// 	var mesh = new THREE.Mesh( geometry, material );
			// 	mesh.position.x = Math.random() * 1600 - 800;
			// 	mesh.position.y = 0;
			// 	mesh.position.z = Math.random() * 1600 - 800;
			// 	mesh.updateMatrix();
			// 	mesh.matrixAutoUpdate = false;
			// 	scene.add( mesh );
			//
			// }

			var oLoader = new THREE.OBJLoader();

			var oLoader2 = new THREE.OBJLoader();

			var oLoader3 = new THREE.OBJLoader();

			var oLoader4 = new THREE.OBJLoader();

			var oLoader5 = new THREE.OBJLoader();

			oLoader.load('aligned_aorta.obj', function(object, materials) {

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0xa65e00
				});

				object.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object.position.x = 0;
				object.position.y = 0;
				object.position.z = 0;

				object.scale.set(1, 1, 1);
				scene.add(object);

				document.getElementById('hideShow').addEventListener('click', function() {
					object.visible = !object.visible;
				});
			});

			oLoader2.load('aligned_pa.obj', function(object2, materials) {

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0x008000
				});

				object2.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object2.position.x = 0;
				object2.position.y = 0;
				object2.position.z = 0;
				object2.scale.set(1, 1, 1);
				scene.add(object2);

				document.getElementById('hideShow2').addEventListener('click', function() {
					object2.visible = !object2.visible;
				});

			});

			oLoader3.load('aligned_la.obj', function(object3, materials) {

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0xFF4500
				});

				object3.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object3.position.x = 0;
				object3.position.y = 0;
				object3.position.z = 0;
				object3.scale.set(1, 1, 1);
				scene.add(object3);

				document.getElementById('hideShow3').addEventListener('click', function() {
					object3.visible = !object3.visible;
				});
			});

			oLoader4.load('aligned_ra.obj', function(object4, materials) {

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0x1e90ff
				});

				object4.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object4.position.x = 0;
				object4.position.y = 0;
				object4.position.z = 0;
				object4.scale.set(1, 1, 1);
				scene.add(object4);

				document.getElementById('hideShow4').addEventListener('click', function() {
					object4.visible = !object4.visible;
				});
			});

			oLoader5.load('aligned_lv.obj', function(object5, materials) {

				// var material = new THREE.MeshFaceMaterial(materials);
				var material2 = new THREE.MeshLambertMaterial({
					color: 0xFF0000
				});

				object5.traverse(function(child) {
					if (child instanceof THREE.Mesh) {

						// apply custom material
						child.material = material2;

						// enable casting shadows
						child.castShadow = true;
						child.receiveShadow = true;
					}
				});

				object5.position.x = 0;
				object5.position.y = 0;
				object5.position.z = 0;
				object5.scale.set(1, 1, 1);
				scene.add(object5);

				document.getElementById('hideShow5').addEventListener('click', function() {
					object5.visible = !object5.visible;
				});
			});

			// lights

			var light = new THREE.DirectionalLight(0xffffff, 2);
			light.position.set(1, 1, 1);
			scene.add(light);

			var light = new THREE.DirectionalLight(0x002288, 1);
			light.position.set(-1, -1, -1);
			scene.add(light);

			var light = new THREE.DirectionalLight(0xffffff, 1);
			light.position.set(-1, -1, -90);
			scene.add(light);

			// var light = new THREE.DirectionalLight(0xffffff, 2);
			// light.position.set(-1, -90, -90);
			// scene.add(light);
			//
			var light = new THREE.DirectionalLight(0xffffff, 1);
			light.position.set(-50, -30, 40);
			scene.add(light);

			// mesh4.position.z = -50;
			// mesh4.position.y = -30;
			// mesh4.position.x = -50;

			// var light = new THREE.AmbientLight(0x222222, 2);
			// scene.add(light);

			//

			window.addEventListener('resize', onWindowResize, false);

		}

		function onWindowResize() {

			camera.aspect = window.innerWidth / window.innerHeight;
			camera.updateProjectionMatrix();

			renderer.setSize(window.innerWidth, window.innerHeight);

		}

		function animate() {

			requestAnimationFrame(animate);

			controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true

			render();

		}

		function render() {

			renderer.render(scene, camera);

		}
	</script>

</body>

</html>
>"""

if choice == '6':
    message = """<!DOCTYPE html>
<html lang="en">
	<head>
		<title>*Insert Title Here*</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">

		<style>
			body {
				background-color:  black;
				color: #000;
			}

			a {
				color: #f00;
			}

			.aorta{
				background-color: #FFFF00; /* Yellow background */
				border: 1px solid yellow; /* yellow border */
				color: black; /* White text */
				padding: 10px 24px; /* Some padding */
				cursor: pointer; /* Pointer/hand icon */

			}

			.pulmonaryArtery{
				background-color: #4CAF50; /* Green background */
				border: 1px solid green; /* Green border */
				color: white; /* White text */
				padding: 10px 24px; /* Some padding */
				cursor: pointer; /* Pointer/hand icon */

			}

			.leftAtrium{
				background-color: #FFA500; /* Orange background */
				border: 1px solid orange; /* Orange border */
				color: white; /* White text */
				padding: 10px 24px; /* Some padding */
				cursor: pointer; /* Pointer/hand icon */
			}

			.rightAtrium{
				background-color: #add8e6; /* Light Blue background */
				border: 1px solid lightBlue; /* Light Blue border */
				color: white; /* White text */
				padding: 10px 24px; /* Some padding */
				cursor: pointer; /* Pointer/hand icon */
			}

			.rightVentricle{
				
				background-color: #0000ff; /* Blue background */
				border: 1px solid Blue; /* Red border */
				color: white; /* White text */
				padding: 10px 24px; /* Some padding */
				cursor: pointer; /* Pointer/hand icon */
			}

			.leftVentricle {
				background-color: #ff0000; /* Red background */
				border: 1px solid red; /* Blue border */
				color: white; /* White text */
				padding: 10px 24px; /* Some padding */
				cursor: pointer; /* Pointer/hand icon */
			}

		</style>
	</head>

	<body>


<button class = "aorta" id="hideShow">Hide / Show Aorta</button>
<button class = "pulmonaryArtery" id="hideShow2">Hide / Show Pulmonary Artery</button>
<button class = "leftAtrium" id="hideShow3">Hide / Show Left Atrium</button>
<button class = "rightAtrium" id="hideShow4">Hide / Show Right Atrium</button>
<button class = "rightVentricle" id="hideShow5">Hide / Show Right Ventricle</button>
<button class = "leftVentricle" id="hideShow6">Hide / Show Left Ventricle</button>



		<!--<button type="button" id="hideShow9" onclick="hide2018001()">Hide buttons</button>
		<form> <input type="checkbox" id="myCheck" onclick="hide2018002"> Toggle 2018002 </form>
		<form> <input type = "checkbox" id = "myCheck2" onclick="alert('you clicked')"> Toggle 2018003 </form>-->

		<script src="three.js"></script>
		<script src="OrbitControls.js"></script>
		<script src="OBJLoader.js"></script>
		<script src="WebGL.js"></script>


		<script>

			if ( WEBGL.isWebGLAvailable() === false ) {

				document.body.appendChild( WEBGL.getWebGLErrorMessage() );

			}

			var camera, controls, scene, renderer;

			init();
			//render(); // remove when using next line for animation loop (requestAnimationFrame)
			animate();

			function init() {

				scene = new THREE.Scene();
				 scene.background = new THREE.Color( 0x000000 );
				// scene.fog = new THREE.FogExp2( 0xcccccc, 0 );

				renderer = new THREE.WebGLRenderer( { antialias: true } );
				renderer.setPixelRatio( window.devicePixelRatio );
				renderer.setSize( window.innerWidth, window.innerHeight );
				document.body.appendChild( renderer.domElement );

				camera = new THREE.PerspectiveCamera( 60, window.innerWidth / window.innerHeight, 1, 1000 );
				camera.position.set( 0, 0, -400 );

				// controls

				controls = new THREE.OrbitControls( camera, renderer.domElement );

				//controls.addEventListener( 'change', render ); // call this only in static scenes (i.e., if there is no animation loop)

				controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
				controls.dampingFactor = 0.25;

				controls.screenSpacePanning = false;

				controls.minDistance = 100;
				controls.maxDistance = 500;

				controls.maxPolarAngle = Math.PI;

				// world

				// var geometry = new THREE.CylinderBufferGeometry( 0, 10, 30, 4, 1 );
				// var material = new THREE.MeshPhongMaterial( { color: 0xffffff, flatShading: true } );
				//
				// for ( var i = 0; i < 500; i ++ ) {
				//
				// 	var mesh = new THREE.Mesh( geometry, material );
				// 	mesh.position.x = Math.random() * 1600 - 800;
				// 	mesh.position.y = 0;
				// 	mesh.position.z = Math.random() * 1600 - 800;
				// 	mesh.updateMatrix();
				// 	mesh.matrixAutoUpdate = false;
				// 	scene.add( mesh );
				//
				// }





				var oLoader = new THREE.OBJLoader();

				var oLoader2 = new THREE.OBJLoader();

				var oLoader3 = new THREE.OBJLoader();

				var oLoader4 = new THREE.OBJLoader();

				var oLoader5 = new THREE.OBJLoader();

				var oLoader6 = new THREE.OBJLoader();

				oLoader.load('aligned_aorta_TOF.obj', function(object, materials) {

					// var material = new THREE.MeshFaceMaterial(materials);
					var material2 = new THREE.MeshLambertMaterial({
						color: 0xa65e00
					});

					object.traverse(function(child) {
						if (child instanceof THREE.Mesh) {

							// apply custom material
							child.material = material2;

							// enable casting shadows
							child.castShadow = true;
							child.receiveShadow = true;
						}
					});

					object.position.x = 0;
					object.position.y = 0;
					object.position.z = 0;

					object.scale.set(1, 1, 1);
					scene.add(object);

					document.getElementById('hideShow').addEventListener('click', function() {
						object.visible = !object.visible;
					});
				});

				oLoader2.load('aligned_pa_TOF.obj', function(object2, materials) {

					// var material = new THREE.MeshFaceMaterial(materials);
					var material2 = new THREE.MeshLambertMaterial({
						color: 0x008000
					});

					object2.traverse(function(child) {
						if (child instanceof THREE.Mesh) {

							// apply custom material
							child.material = material2;

							// enable casting shadows
							child.castShadow = true;
							child.receiveShadow = true;
						}
					});

					object2.position.x = 0;
					object2.position.y = 0;
					object2.position.z = 0;
					object2.scale.set(1, 1, 1);
					scene.add(object2);

					document.getElementById('hideShow2').addEventListener('click', function() {
						object2.visible = !object2.visible;
					});

				});

				oLoader3.load('aligned_la_TOF.obj', function(object3, materials) {

					// var material = new THREE.MeshFaceMaterial(materials);
					var material2 = new THREE.MeshLambertMaterial({
						color: 0xFF4500
					});

					object3.traverse(function(child) {
						if (child instanceof THREE.Mesh) {

							// apply custom material
							child.material = material2;

							// enable casting shadows
							child.castShadow = true;
							child.receiveShadow = true;
						}
					});

					object3.position.x = 0;
					object3.position.y = 0;
					object3.position.z = 0;
					object3.scale.set(1, 1, 1);
					scene.add(object3);

					document.getElementById('hideShow3').addEventListener('click', function() {
						object3.visible = !object3.visible;
					});
				});

				oLoader4.load('aligned_ra_TOF.obj', function(object4, materials) {

					// var material = new THREE.MeshFaceMaterial(materials);
					var material2 = new THREE.MeshLambertMaterial({
						color: 0x1e90ff
					});

					object4.traverse(function(child) {
						if (child instanceof THREE.Mesh) {

							// apply custom material
							child.material = material2;

							// enable casting shadows
							child.castShadow = true;
							child.receiveShadow = true;
						}
					});

					object4.position.x = 0;
					object4.position.y = 0;
					object4.position.z = 0;
					object4.scale.set(1, 1, 1);
					scene.add(object4);

					document.getElementById('hideShow4').addEventListener('click', function() {
						object4.visible = !object4.visible;
					});
				});

				oLoader5.load('aligned_rv_TOF.obj', function(object5, materials) {

					// var material = new THREE.MeshFaceMaterial(materials);
					var material2 = new THREE.MeshLambertMaterial({
						color: 0x0000ff
					});

					object5.traverse(function(child) {
						if (child instanceof THREE.Mesh) {

							// apply custom material
							child.material = material2;

							// enable casting shadows
							child.castShadow = true;
							child.receiveShadow = true;
						}
					});

					object5.position.x = 0;
					object5.position.y = 0;
					object5.position.z = 0;
					object5.scale.set(1, 1, 1);
					scene.add(object5);

					document.getElementById('hideShow5').addEventListener('click', function() {
						object5.visible = !object5.visible;
					});
				});

				oLoader6.load('aligned_lv_TOF.obj', function(object6, materials) {

					// var material = new THREE.MeshFaceMaterial(materials);
					var material2 = new THREE.MeshLambertMaterial({
						color: 0xFF0000
					});

					object6.traverse(function(child) {
						if (child instanceof THREE.Mesh) {

							// apply custom material
							child.material = material2;

							// enable casting shadows
							child.castShadow = true;
							child.receiveShadow = true;
						}
					});

					object6.position.x = 0;
					object6.position.y = 0;
					object6.position.z = 0;
					object6.scale.set(1, 1, 1);
					scene.add(object6);

					document.getElementById('hideShow6').addEventListener('click', function() {
						object6.visible = !object6.visible;
					});
				});

				// lights

				var light = new THREE.DirectionalLight( 0xffffff, 2 );
				light.position.set( 1, 1, 1 );
				scene.add( light );

				var light = new THREE.DirectionalLight( 0x002288, 1 );
				light.position.set( - 1, - 1, - 1 );
				scene.add( light );

				var light = new THREE.DirectionalLight( 0xffffff, 1.5 );
				light.position.set(  -1,  -1 ,  -90 );
				scene.add( light );

				// var light = new THREE.DirectionalLight( 0xffffff, 2 );
				// light.position.set(  -1,  -90 ,  -90 );
				// scene.add( light );

				var light = new THREE.DirectionalLight( 0xffffff, 1 );
				light.position.set(  -50,  -30 ,  40 );
				scene.add( light );

				// var light = new THREE.AmbientLight( 0x222222, 2 );
				// scene.add( light );

				//

				window.addEventListener( 'resize', onWindowResize, false );

			}

			function onWindowResize() {

				camera.aspect = window.innerWidth / window.innerHeight;
				camera.updateProjectionMatrix();

				renderer.setSize( window.innerWidth, window.innerHeight );

			}

			function animate() {

				requestAnimationFrame( animate );

				controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true

				render();

			}

			function render() {

				renderer.render( scene, camera );

			}

		</script>

	</body>
</html>
 """



f.write(message)
f.close()