name = input('what would you like to name the Web GL File? ')

myoSwitch = input('Is the Web GL for a Myocardium or a regular heart? type yes for Myocardium or no if not ')

if myoSwitch == "yes":

    f = open(name, 'w')
    message = """<!DOCTYPE html>
<html lang="en">

<head>
	<title>2018001-01 Myocardium High Resolution</title>
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

		.sidebar{
			position: fixed;
			width: 200px;
			top:0;
			left: 0;
			bottom: 0;
			background: grey;
			padding-top: 50px;
			}
	
			.sidebar h1{
			display: block;
			padding: 10px 20px;
			color: #fff;
			text-decoration: none;
			letter-spacing: 2px;
			/*font-family: 'Krona One', sans-serif;*/
			font-weight: 400;
			margin: 0;
			font-size: 20px;
			text-transform: uppercase;
			}
	
			.sidebar a {
			display: block;
			padding: 10px 20px;
			color: #bbb;
			outline: none;
			border: none;
			background: none;
			text-decoration: none;
			font-family: "Helvetica";
			letter-spacing: 1px;
			
			}
	
			.dropdown-btn{
				font-size: 15px;
			}
	
			.sidebar a:hover{
			color: #fff;
			margin-left: 10px;
			transition: 0.4s;
			}
	
			.sidebar a.hoverspeed:hover{
				color: #fff;
				margin-left: 7px;
				transition: 0.4s;
			}
	
			.sidebar a.pink:hover{
			background-color: pink;
			color:black;
			margin-left: 10px;
			transition: 0.4s;
			}
	
			.sidebar a.info:hover{
				background-color: black;
				margin-left: 10px;
				transition: 0.4s;
			}
	

	</style>
</head>

<body>

		<div class="sidebar">
			<a href="https://apil.ca/" class="hoverspeed"><img src="https://apillogo.s3.ca-central-1.amazonaws.com/APIL_LOGO.png" alt="Apil" width="175" height="75" style="vertical-align:left;margin:0px -5px"></a>
			<a class="pink" id="hideShow">2018001-01 Myocardium</a>
			<a class = "info" onclick = "document.location = 'https://github.com/tgh-apil/TorontoHeartAtlas/blob/master/2018001MYO/2018001Myocard.obj'">High Resolution Myocardium Download</a>
		</div>
		

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
	<title>2018017-01 High Resolution</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
	<!--<link type="text/css" rel="stylesheet" href="index.css">-->
	<style>
		@import url('https://fonts.googleapis.com/css2?family=Krona+One&display=swap');
		body {
			/*background-color: #ccc;*/
			background-color: black;
			color: #000;
		}

		a {
			color: #f00;
		}

		.overlay {
		height: 100%;
		width: 0;
		position: fixed;
		z-index: 1;
		top: 0;
		left: 0;
		background-color: rgb(0,0,0);
		background-color: rgba(0,0,0, 0.9);
		overflow-x: hidden;
		transition: 0.5s;
		}

		.overlay-content {
		position: relative;
		top: 5%;
		width: 100%;
		text-align: center;
		margin-top: 30px;
		color: white;
		}

		.overlay a {
		padding: 8px;
		text-decoration: none;
		font-size: 36px;
		color: #818181;
		display: block;
		transition: 0.3s;
		}

		.overlay a:hover, .overlay a:focus {
		color: #f1f1f1;
		}

		.overlay .closebtn {
		position: absolute;
		top: 20px;
		right: 45px;
		font-size: 60px;
		}

		@media screen and (max-height: 450px) {
		.overlay a {font-size: 20px}
		.overlay .closebtn {
		font-size: 40px;
		top: 15px;
		right: 35px;
		}
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

		.sidebar{
		position: fixed;
		width: 200px;
		top:0;
		left: 0;
		bottom: 0;
		background: grey;
		padding-top: 50px;
		}

		.sidebar h1{
		display: block;
		padding: 10px 20px;
		color: #fff;
		text-decoration: none;
		font-family: "Rubik";
		letter-spacing: 2px;
		font-weight: 400;
		margin: 0;
		font-size: 20px;
		text-transform: uppercase;
		}

		.sidebar a {
		display: block;
		padding: 10px 20px;
		color: #bbb;
		outline: none;
		border: none;
		background: none;
		text-decoration: none;
		font-family: "Rubik";
		letter-spacing: 2px;
		
		}

		.dropdown-btn{
			font-size: 15px;
		}

		.sidebar a:hover{
		color: #fff;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.hoverspeed:hover{
			color: #fff;
			margin-left: 7px;
			transition: 0.4s;
		}

		.sidebar a.yellow{
		background-color: yellow;
		color:black;
		}

		.sidebar a.yellow:hover{
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.red{
		background-color: red;
		color:black;
		}

		.sidebar a.red:hover{
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.blue{
			background-color: blue;
			color: black;
		}

		.sidebar a.blue:hover{
			margin-left: 10px; 
			transition: 0.4s;
		}

		.sidebar a.info:hover{
			background-color: black;
			margin-left: 10px;
			transition: 0.4s;
		}

	</style>
</head>

<body>

		<div class="sidebar">
			<a href="https://apil.ca/" class="hoverspeed"><img src="https://apillogo.s3.ca-central-1.amazonaws.com/APIL_LOGO.png" alt="Apil" width="175" height="75" style="vertical-align:left;margin:0px -5px"></a>
			<a href="#Aorta" class="yellow" id="hideShow">Aorta</a>
			<a href="#atriaVentricle" class="red" id="hideShow2">Atria Ventricle</a>
			<a href="#venaCava" class="blue" id="hideShow3">Vena Cava</a>
			<a href="#" class="info" onclick="openNav()">Information</a>
			<div id="myNav" class="overlay">
				<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
				
			
			<div class="overlay-content">
				<h1> Male Age 25-30. Source Cardiac CT. Software: ITK-SNAP, 3D Slicer, Blender, Meshmixer. </h1> <br>

				<h2>Original Diagnosis</h2>
				<p>1. Situs solitus, D-TGA: A-V concordance; V-A discordance <br> <br> 
					2. Double inlet left ventricle; hypoplastic right ventricle <br> <br>
					3. Pulmonary stenosis <br> <br>
					4. Subvalvular aortic stenosis <br> <br>
					5. Atrial septal defect</p>
				
				<h2>Procedures</h2>
				<p>1. Right BT shunt (First year) <br> <br>
					2. Bidirectional cavopulmonary anastomosis, aortic myomectomy (Age 6) <br> <br>
					3. Lateral tunnel Fontan (Age 6)</p>
		</div>
		</div>
		</div>

	<script src="three.js"></script>
	<script src="OrbitControls.js"></script>
	<script src="GLTFLoader.js"></script>
	<script src="OBJLoader.js"></script>
	<script src="WebGL.js"></script>


	<script>

		function openNav() {
		document.getElementById("myNav").style.width = "100%";
		}

		function closeNav() {
		document.getElementById("myNav").style.width = "0%";
		}

		if (WEBGL.isWebGLAvailable() === false) {

			document.body.appendChild(WEBGL.getWebGLErrorMessage());

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
		<title>2018004-01 High Resolution</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">

		<link rel="icon" href="data:;base64,iVBORw0KGgo=">
		<style>
			@import url('https://fonts.googleapis.com/css2?family=Krona+One&display=swap');
			body {
				background-color:  black;
				color: #000;
			}

			a {
				color: #f00;
			}

		.overlay {
		height: 100%;
		width: 0;
		position: fixed;
		z-index: 1;
		top: 0;
		left: 0;
		background-color: rgb(0,0,0);
		background-color: rgba(0,0,0, 0.9);
		overflow-x: hidden;
		transition: 0.5s;
		}

		.overlay-content {
		position: relative;
		top: 25%;
		width: 100%;
		text-align: center;
		margin-top: 30px;
		color: white;
		}

		.overlay a {
		padding: 8px;
		text-decoration: none;
		font-size: 36px;
		color: #818181;
		display: block;
		transition: 0.3s;
		}

		.overlay a:hover, .overlay a:focus {
		color: #f1f1f1;
		}

		.overlay .closebtn {
		position: absolute;
		top: 20px;
		right: 45px;
		font-size: 60px;
		}

		@media screen and (max-height: 450px) {
		.overlay a {font-size: 20px}
		.overlay .closebtn {
		font-size: 40px;
		top: 15px;
		right: 35px;
		}
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
				background-color: #ff0000; /* Red background */
				border: 1px solid red; /* Red border */
				color: white; /* White text */
				padding: 10px 24px; /* Some padding */
				cursor: pointer; /* Pointer/hand icon */
			}

			.rightAtrium{
				background-color: #0000ff; /* Blue background */
				border: 1px solid blue; /* Blue border */
				color: white; /* White text */
				padding: 10px 24px; /* Some padding */
				cursor: pointer; /* Pointer/hand icon */
			}

			.sidebar{
		position: fixed;
		width: 200px;
		top:0;
		left: 0;
		bottom: 0;
		background: grey;
		padding-top: 50px;
		}

		.sidebar h1{
		display: block;
		padding: 10px 20px;
		color: #fff;
		text-decoration: none;
		font-family: "Rubik";
		letter-spacing: 2px;
		font-weight: 400;
		margin: 0;
		font-size: 20px;
		text-transform: uppercase;
		}

		.sidebar a {
		display: block;
		padding: 10px 20px;
		color: #bbb;
		outline: none;
		border: none;
		background: none;
		text-decoration: none;
		font-family: "Rubik";
		letter-spacing: 2px;
		
		}

		.dropdown-btn{
			font-size: 15px;
		}

		.sidebar a:hover{
		color: #fff;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.hoverspeed:hover{
			color: #fff;
			margin-left: 7px;
			transition: 0.4s;
		}

		.sidebar a.yellow{
		background-color: yellow;
		color:black;
		}

		.sidebar a.yellow:hover{
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.green{
		background-color: green;
		color:black;
		
		}

		.sidebar a.green:hover{
		background-color: green;
		color:black;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.orange{
		background-color: orange;
		color:black;
		
		}

		.sidebar a.orange:hover{
		background-color: orange;
		color:black;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.skyBlue{
		background-color: skyblue;
		color:black;
		}

		.sidebar a.skyBlue:hover{
		background-color: skyblue;
		color:black;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.red{
		background-color: red;
		color:black;
		}

		.sidebar a.red:hover{
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.info:hover{
			background-color: black;
			margin-left: 10px;
			transition: 0.4s;
		}

		</style>
	</head>

	<body>

<div class="sidebar">
	<a href="https://apil.ca/" class="hoverspeed"><img src="https://apillogo.s3.ca-central-1.amazonaws.com/APIL_LOGO.png" alt="Apil" width="175" height="75" style="vertical-align:left;margin:0px -5px"></a>
	<a href="#Aorta" class="yellow" id="hideShow" style="vertical-align:left;">Aorta</a>
	<a href="#Pulmonary Artery" class="green" id="hideShow2">Pulmonary Artery</a>
	<a href="#Left Atrium" class="orange" id="hideShow3">Left Side</a>
	<a href="#Right Atrium" class="skyBlue" id="hideShow4">Right Side</a>
	<a href="#" class="info" onclick="openNav()">Information</a>
	<div id="myNav" class="overlay">
		<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
	<div class="overlay-content">
		<h1>
			Diagnosis & Procedures
		</h1>

		<p>1. D-TGA (AV concordance; VA discordance) post atrial switch (Mustard) repair. <br> <br>
			2. Large leak between IVC and pulmonary venous baffle.</p>

		
	</div>
	</div>
	</div>

		<script src="three.js"></script>
		<script src="OrbitControls.js"></script>
		<script src="OBJLoader.js"></script>
		<script src="WebGL.js"></script>


		<script>

		function openNav() {
		document.getElementById("myNav").style.width = "100%";
		}

		function closeNav() {
		document.getElementById("myNav").style.width = "0%";
		}

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


				oLoader.load('aligned_baffle_leak_ao.obj', function(object, materials) {

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

				oLoader2.load('aligned_bf_pa.obj', function(object2, materials) {

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

				oLoader3.load('aligned_bf_ls.obj', function(object3, materials) {

					// var material = new THREE.MeshFaceMaterial(materials);
					var material2 = new THREE.MeshLambertMaterial({
						color: 0xFF0000
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

				oLoader4.load('aligned_bf_rs.obj', function(object4, materials) {

					// var material = new THREE.MeshFaceMaterial(materials);
					var material2 = new THREE.MeshLambertMaterial({
						color: 0x0000ff
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

				var light = new THREE.DirectionalLight( 0xffffff, 2 );
				light.position.set( 1, 1, 1 );
				scene.add( light );

				var light = new THREE.DirectionalLight( 0x002288, 2 );
				light.position.set( - 1, - 1, - 1 );
				scene.add( light );

				var light = new THREE.DirectionalLight( 0xffffff, 2 );
				light.position.set(  -1,  -1 ,  -90 );
				scene.add( light );

				var light = new THREE.AmbientLight( 0x222222, 2 );
				scene.add( light );

				var light = new THREE.DirectionalLight( 0xffffff, 2 );
				light.position.set(  -1,  -90 ,  -90 );
				scene.add( light );

				var light = new THREE.DirectionalLight( 0xffffff, 2 );
				light.position.set(  -50,  -30 ,  40 );
				scene.add( light );

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

if choice == '5':

    message = """<!DOCTYPE html>
<html lang="en">

<head>
	<title>2018001-01 High Resolution</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
	<!--<link type="text/css" rel="stylesheet" href="index.css">-->
	<style>
		body {
			/*background-color: #ccc;*/
			background-color: black;
			color: #000;
			font-family: 'Lato', sans-serif;
			
		}

		a {
			color: #f00;
		}

		.overlay {
		height: 100%;
		width: 0;
		position: fixed;
		z-index: 1;
		top: 0;
		left: 0;
		background-color: rgb(0,0,0);
		background-color: rgba(0,0,0, 0.9);
		overflow-x: hidden;
		transition: 0.5s;
		}

		.overlay-content {
		position: relative;
		top: 25%;
		width: 100%;
		text-align: center;
		margin-top: 30px;
		color: white;
		}

		.overlay a {
		padding: 8px;
		text-decoration: none;
		font-size: 36px;
		color: #818181;
		display: block;
		transition: 0.3s;
		}

		.overlay a:hover, .overlay a:focus {
		color: #f1f1f1;
		}

		.overlay .closebtn {
		position: absolute;
		top: 20px;
		right: 45px;
		font-size: 60px;
		}

		@media screen and (max-height: 450px) {
		.overlay a {font-size: 20px}
		.overlay .closebtn {
		font-size: 40px;
		top: 15px;
		right: 35px;
		}
		}

		.offset {
			margin-right: 50px;
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

		.sidebar{
		position: fixed;
		width: 200px;
		top:0;
		left: 0;
		bottom: 0;
		background: grey;
		padding-top: 50px;
		}

		.sidebar h1{
		display: block;
		padding: 10px 20px;
		color: #fff;
		text-decoration: none;
		font-family: "Rubik";
		letter-spacing: 1px;
		font-weight: 400;
		margin: 0;
		font-size: 20px;
		text-transform: uppercase;
		}

		li{
			color: #fff;
			font-size: 20px;
			letter-spacing: 1px;
		}

		.sidebar a {
		display: block;
		padding: 10px 20px;
		color: #bbb;
		outline: none;
		border: none;
		background: none;
		text-decoration: none;
		font-family: "Rubik";
		letter-spacing: 2px;
		
		}

		.dropdown-btn{
			font-size: 15px;
		}

		.sidebar a:hover{
		color: #fff;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.hoverspeed:hover{
			color: #fff;
			margin-left: 7px;
			transition: 0.4s;
		}

		.sidebar a.yellow{
		background-color: yellow;
		color:black;
		}

		.sidebar a.yellow:hover{
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.green{
		background-color: green;
		color:black;
		
		}

		.sidebar a.green:hover{
		background-color: green;
		color:black;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.orange{
		background-color: orange;
		color:black;
		
		}

		.sidebar a.orange:hover{
		background-color: orange;
		color:black;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.skyBlue{
		background-color: skyblue;
		color:black;
		}

		.sidebar a.skyBlue:hover{
		background-color: skyblue;
		color:black;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.red{
		background-color: red;
		color:black;
		}

		.sidebar a.red:hover{
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.info:hover{
			background-color: black;
			margin-left: 10px;
			transition: 0.4s;
		}



	</style>
</head>

<body>

	<div class="sidebar">
		<a href="https://apil.ca/" class="hoverspeed"><img src="https://apillogo.s3.ca-central-1.amazonaws.com/APIL_LOGO.png" alt="Apil" width="175" height="75" style="vertical-align:left;margin:0px -5px"></a>
		<a href="#Aorta" class="yellow" id="hideShow" style="vertical-align:left;">Aorta</a>
		<a href="#Pulmonary Artery" class="green" id="hideShow2">Pulmonary Artery</a>
		<a href="#Left Atrium" class="orange" id="hideShow3">Left Atrium</a>
		<a href="#Right Atrium" class="skyBlue" id="hideShow4">Right Atrium</a>
		<a href="#Left Ventricle" class="red" id="hideShow5">Left Ventricle</a>
		<a href="#" class="info" onclick="openNav()">Information</a>
		<div id="myNav" class="overlay">
			<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
			
		
		<div class="overlay-content">
			<h1>
				Diagnosis
			</h1>

			<p>1. Hypoplastic right heart: tricuspid atresia, pulmonary stenosis, hypoplastic right ventricle <br>
				2. Multiple VSDs <br>
				3. Secundum ASD</p>

			<h1>Procedure</h1>

			<p>1. Right-sided BTT shunt <br>
				2. Bjork Fontan operation; ligation of BT shunt</p>
		</div>
		</div>
	  </div>

	<script src="three.js"></script>
	<script src="OrbitControls.js"></script>
	<script src="GLTFLoader.js"></script>
	<script src="OBJLoader.js"></script>
	<script src="WebGL.js"></script>


	<script>

		function openNav() {
		document.getElementById("myNav").style.width = "100%";
		}

		function closeNav() {
		document.getElementById("myNav").style.width = "0%";
		}


		if (WEBGL.isWebGLAvailable() === false) {

			document.body.appendChild(WEBGL.getWebGLErrorMessage());

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

"""

if choice == '6':
    message = """<!DOCTYPE html>
<html lang="en">
	<head>
		<title>2018002-01 High Resolution</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
		

		<style>
			@import url('https://fonts.googleapis.com/css2?family=Krona+One&display=swap');
			body {
				background-color:  black;
				color: #000;
				font-family: 'Lato', sans-serif;
			}

			

			a {
				color: #f00;
			}

		.overlay {
		height: 100%;
		width: 0;
		position: fixed;
		z-index: 1;
		top: 0;
		left: 0;
		background-color: rgb(0,0,0);
		background-color: rgba(0,0,0, 0.9);
		overflow-x: hidden;
		transition: 0.5s;
		}

		.overlay-content {
		position: relative;
		top: 25%;
		width: 100%;
		text-align: center;
		margin-top: 30px;
		color: white;
		}

		.overlay a {
		padding: 8px;
		text-decoration: none;
		font-size: 36px;
		color: #818181;
		display: block;
		transition: 0.3s;
		}

		.overlay a:hover, .overlay a:focus {
		color: #f1f1f1;
		}

		.overlay .closebtn {
		position: absolute;
		top: 20px;
		right: 45px;
		font-size: 60px;
		}

		@media screen and (max-height: 450px) {
		.overlay a {font-size: 20px}
		.overlay .closebtn {
		font-size: 40px;
		top: 15px;
		right: 35px;
		}
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


		.sidebar{
		position: fixed;
		width: 200px;
		top:0;
		left: 0;
		bottom: 0;
		background: grey;
		padding-top: 50px;
		}

		.sidebar h1{
		display: block;
		padding: 10px 20px;
		color: #fff;
		text-decoration: none;
		font-family: 'Krona One', sans-serif;
		letter-spacing: 2px;
		font-weight: 400;
		margin: 0;
		font-size: 20px;
		text-transform: uppercase;
		}

		.sidebar a {
		display: block;
		padding: 10px 20px;
		color: #bbb;
		outline: none;
		border: none;
		background: none;
		text-decoration: none;
		font-family: "Rubik";
		letter-spacing: 2px;
		
		}

		.dropdown-btn{
			font-size: 15px;
		}

		.sidebar a:hover{
		color: #fff;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.hoverspeed:hover{
			color: #fff;
			margin-left: 7px;
			transition: 0.4s;
		}

		.sidebar a.yellow{
		background-color: yellow;
		color:black;
		}

		.sidebar a.yellow:hover{
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.green{
		background-color: green;
		color:black;
		
		}

		.sidebar a.green:hover{
		background-color: green;
		color:black;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.orange{
		background-color: orange;
		color:black;
		
		}

		.sidebar a.orange:hover{
		background-color: orange;
		color:black;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.skyBlue{
		background-color: skyblue;
		color:black;
		}

		.sidebar a.skyBlue:hover{
		background-color: skyblue;
		color:black;
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.red{
		background-color: red;
		color:black;
		}

		.sidebar a.red:hover{
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.blue{
		background-color: blue;
		color:black;
		}

		.sidebar a.blue:hover{
		margin-left: 10px;
		transition: 0.4s;
		}

		.sidebar a.info:hover{
			background-color: black;
			margin-left: 10px;
			transition: 0.4s;
		}


		</style>
	</head>

	<body>


	<div class="sidebar">
		<a href="https://apil.ca/" class="hoverspeed"><img src="https://apillogo.s3.ca-central-1.amazonaws.com/APIL_LOGO.png" alt="Apil" width="175" height="75" style="vertical-align:left;margin:0px -5px"></a>
		<a href="#aorta" class="yellow" id="hideShow">Aorta</a>
		<a href="#PulmonaryArtery" class="green" id="hideShow2">Pulmonary Artery</a>
		<a href="#LeftAtrium" class="orange" id="hideShow3">Left Atrium</a>
		<a href="#RightAtrium" class="skyBlue" id="hideShow4">Right Atrium</a>
		<a href="#RightAtrium" class="red" id="hideShow6">Left Ventricle</a>
		<a href="#LeftAtrium" class="blue" id="hideShow5">Right Ventricle</a>
		<a href="#" class="info" onclick="openNav()">Information</a>
		<div id="myNav" class="overlay">
			<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
			
		
		<div class="overlay-content">
			<h1>
				Diagnosis
			</h1>

			<p>1. Tetralogy of Fallot, (uncorrected): Overriding aorta, pulmonary stenosis, <br> 
				subaortic ventricular septal defect, right ventricular hypertrophy</p>

			<h1>Procedure</h1>

			<p>1. Remnant of BTT shunt can be seen from left subclavian artery to left pulmonary artery. <br>
				2. No further correction until age 65. Underwent pulmonary valve replacement subsequently.</p>
		</div>
		</div>
	</div>

		<script src="three.js"></script>
		<script src="OrbitControls.js"></script>
		<script src="OBJLoader.js"></script>
		<script src="WebGL.js"></script>


		<script>

		function openNav() {
		document.getElementById("myNav").style.width = "100%";
		}

		function closeNav() {
		document.getElementById("myNav").style.width = "0%";
		}

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