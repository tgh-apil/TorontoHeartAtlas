package javaHTML;
import java.awt.Desktop;
import java.io.*;

import java.io.File;  // Import the File class
import java.io.IOException;  // Import the IOException class to handle errors
import java.io.FileWriter;
import java.util.Scanner;

public class javaHTML {

    public static void main(String[] args) {
        String name1;
        String name2; 
        String name3;
        String name4;
        String name5;
        String name6;
        //String fileName1;

        Scanner myObj = new Scanner(System.in);  // Create a Scanner object

        System.out.println("How many STL's are being used? Choices: | 3 | 4 | 5 | 6 |");
        int choice = myObj.nextInt();

        /*System.out.println("What would you like to name the file? ");
        myObj.nextLine();
        fileName1 = myObj.nextLine();*/

        
        if (choice == 3){
            createFile();
            System.out.println("Name of the heartpiece ");
            myObj.nextLine(); //creates line so program does not skip
            name1 = myObj.nextLine();
            name2 = myObj.nextLine();  
            name3 = myObj.nextLine(); 
            if (name1 != null || name2 != null || name3 != null){
                fileWriter(name1, name2, name3); //helps pass parameters to fileWriter method
            } else {
                System.out.println("end program");
            }
        } 
        
        if (choice == 4){
            //createFile(fileName1);
            System.out.println("Name of the heartpiece ");
            myObj.nextLine();
            name1 = myObj.nextLine();
            name2 = myObj.nextLine();  
            name3 = myObj.nextLine(); 
            name4 = myObj.nextLine();
            if (name1 == null || name2 == null || name3 == null || name4 == null){
                System.out.println("program ends");
            } else {
                fileWriter2(name1, name2, name3, name4);
            }
        }
        
        if (choice == 5){
            //createFile(fileName1);
            System.out.println("Name of the HeartPiece ");
            myObj.nextLine(); 
            name1 = myObj.nextLine();
            name2 = myObj.nextLine();  
            name3 = myObj.nextLine(); 
            name4 = myObj.nextLine();
            name5 = myObj.nextLine();
            fileWriter3(name1, name2, name3, name4, name5);
        }

        if (choice == 6){
            //createFile(fileName1);
            System.out.println("Name of heartpieces ");
            myObj.nextLine();
            name1 = myObj.nextLine();
            name2 = myObj.nextLine();  
            name3 = myObj.nextLine(); 
            name4 = myObj.nextLine();
            name5 = myObj.nextLine();
            name6 = myObj.nextLine();
            fileWriter4(name1, name2, name3, name4, name5, name6);
        }

      }

      public static void createFile(){
        try {
            File myObj = new File("filename.html");
            if (myObj.createNewFile()) {
              System.out.println("File created: " + myObj.getName());
            } else {
              System.out.println("File already exists.");
            }
          } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
      }

      public static void fileWriter(String name1, String name2, String name3){ //passes parameters to the method
        
        try {
            FileWriter myWriter = new FileWriter("filename.html");
            BufferedWriter bw = new BufferedWriter(myWriter);
            //myWriter.write("Files in Java might be tricky, " + name1 + " but it is fun enough!"); //uses the passed parameters
            //myWriter.close();
            bw.write("<!DOCTYPE html>");
            bw.write("\n" + "<html lang=\"en\">");
            bw.write("\n" + "<head>");
            bw.write(" <title>2018017-01 High Resolution</title>" + "\n" + 
            "<meta charset=\"utf-8\">" + "\n" + 
            "<meta name=\"viewport\" content=\"width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0\">");
            bw.write("\n" + "\n" + "<style>" + "\n" + 
            "@import url('https://fonts.googleapis.com/css2?family=Krona+One&display=swap');" + "\n" +
            "body {" + "\n" + 
               "/*background-color: #ccc;*/" + "\n" + 
                "background-color: black;" + "\n" + 
                "color: #000;" + "\n" + "}");
            bw.write("\n" + "\n" + "\t" + "a {" + "\n" + 
                "\t" + "\t" + "color: #f00;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".overlay {" + "\n" + 
                "height: 100%;" + "\n" + 
                "width: 0;" + "\n" + 
                "position: fixed;" + "\n" + 
                "z-index: 1;" + "\n" + 
                "top: 0;" + "\n" + 
                "left: 0;" + "\n" + 
                "background-color: rgb(0,0,0);" + "\n" + 
                "background-color: rgba(0,0,0, 0.9);" + "\n" + 
                "overflow-x: hidden;" + "\n" + 
                "transition: 0.5s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".overlay-content {" + "\n" + 
                "position: relative;" + "\n" +
                "top: 5%;" + "\n" + 
                "width: 100%;" + "\n" + 
                "text-align: center;" + "\n" + 
                "margin-top: 30px;" + "\n" + 
                "color: white;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".overlay a {" + "\n" + 
                "padding: 8px;" + "\n" + 
                "text-decoration: none;" + "\n" + 
                "font-size: 36px;" + "\n" + 
                "color: #818181;" + "\n" + 
                "display: block;" + "\n" + 
                "transition: 0.3s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".overlay a:hover, .overlay a:focus {" + "\n" + 
                "color: #f1f1f1;" + "\n" + 
                "}");
            bw.write(".overlay .closebtn {" + "\n" + 
                "position: absolute;" + "\n" + 
                "top: 20px;" + "\n" + 
                "right: 45px;" + "\n" + 
                "font-size: 60px;" + "\n" +
                "}");
            bw.write("\n" + "\n" + "@media screen and (max-height: 450px) {" + "\n" + 
                ".overlay a {font-size: 20px}" + "\n" + 
                ".overlay .closebtn {" + "\n" + 
                "font-size: 40px;" + "\n" + 
                "top: 15px;" + "\n" + 
                "right: 35px;" + "\n" + 
                "}" + "\n" + 
                "}");
            
            bw.write("\n" + "\n" + ".sidebar{" + "\n" + 
                "position: fixed;" + "\n" + 
                "width: 200px;" + "\n" + 
                "top:0;" + "\n" + 
                "left: 0;" + "\n" + 
                "bottom: 0;" + "\n" + 
                "background: grey;" + "\n" + 
                "padding-top: 50px;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar h1{" + "\n" + 
                "display: block;" + "\n" + 
                "padding: 10px 20px;" + "\n" + 
                "color: #fff;" + "\n" + 
                "text-decoration: none;" + "\n" + 
                "font-family: \"Rubik\";" + "\n" + 
                "letter-spacing: 2px;" + "\n" + 
                "font-weight: 400;" + "\n" + 
                "margin: 0;" + "\n" + 
                "font-size: 20px;" + "\n" + 
                "text-transform: uppercase;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a {" + "\n" + 
                "display: block;" + "\n" + 
                "padding: 10px 20px;" + "\n" + 
                "color: #bbb;" + "\n" + 
                "outline: none;" + "\n" + 
                "border: none;" + "\n" + 
                "background: none;" + "\n" + 
                "text-decoration: none;" + "\n" + 
                "font-family: \"Rubik\";" + "\n" + 
                "letter-spacing: 2px;" + "\n" + 
                
                "}");
            bw.write("\n" + "\n" + ".dropdown-btn{" + "\n" + 
                "font-size: 15px;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a:hover{" + "\n" + 
                "color: #fff;" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.hoverspeed:hover{" + "\n" + 
                "color: #fff;" + "\n" + 
                "margin-left: 7px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a.yellow{" + "\n" + 
                "background-color: yellow;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.yellow:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.red{" + "\n" + 
                "background-color: red;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.red:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.blue{" + "\n" + 
                "background-color: blue;" + "\n" + 
                "color: black;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a.blue:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" +  
                "transition: 0.4s;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a.info:hover{" + "\n" + 
                "background-color: black;" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" +"\n" + 
            "}");
            bw.write("\n" + "\n" + "</style>" + "\n" + 
            "</head>");
            bw.write("\n" + "\n" + "<body>" + "\n" + 

            "\t" + "<div class=\"sidebar\">" + "\n" + 
                "\t" + "\t" + "<a href=\"https://apil.ca/\" class=\"hoverspeed\"><img src=\"https://apillogo.s3.ca-central-1.amazonaws.com/APIL_LOGO.png\" alt=\"Apil\" width=\"175\" height=\"75\" style=\"vertical-align:left;margin:0px -5px\"></a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Aorta\" class=\"yellow\" id=\"hideShow\">Aorta</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#atriaVentricle\" class=\"red\" id=\"hideShow2\">Atria Ventricle</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#venaCava\" class=\"blue\" id=\"hideShow3\">Vena Cava</a>");
            bw.write("\n" + "</div>");
            bw.write("\n" + "\t" + "<script src=\"three.js\"></script>" + "\n" + 
           "\t" + "<script src=\"OrbitControls.js\"></script>" + "\n" + 
            "\t" + "<script src=\"GLTFLoader.js\"></script>" + "\n" + 
            "\t" + "<script src=\"OBJLoader.js\"></script>" + "\n" + 
            "\t" + "<script src=\"WebGL.js\"></script>");
            bw.write("\n" + "\n" + "\t" + "<script>");
            bw.write("\n" + "\n" + "\t" + "\t" + "var camera, controls, scene, renderer, object, object2, object3, object4, object5;" + "\n" + 
            "\t" + "\t" + "var objhidden = false;" + "\n" + 
            "\t" + "\t" + "init();");
            bw.write("\n" + "\n" + "\t" + "\t" + "animate();" + "\n" + 
            "\t" + "\t" + "function init() {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + " scene = new THREE.Scene();" +"\n" + 
            "\t" + "\t" + "\t" + "scene.background = new THREE.Color(0x000000);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + " renderer = new THREE.WebGLRenderer({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "antialias: true"+ "\n" + 
            "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "renderer.setPixelRatio(window.devicePixelRatio);" + "\n" + 
            "\t" + "\t" + "\t" + "renderer.setSize(window.innerWidth, window.innerHeight);" + "\n" + 
            "\t" + "\t" + "\t" + "document.body.appendChild(renderer.domElement);" + "\n" + 
            "\t" + "\t" + "\t" + "camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);" + "\n" + 
            "\t" + "\t" + "\t" + "camera.position.set(0, 0, -400);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "controls = new THREE.OrbitControls(camera, renderer.domElement);" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "//controls.addEventListener( 'change', render ); // call this only in static scenes (i.e., if there is no animation loop)" + "\n" +
            "\t" + "\t" + "\t" + "controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled" + "\n" + 
            "\t" + "\t" + "\t" + "controls.dampingFactor = 0.25;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.screenSpacePanning = false;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.minDistance = 100;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.maxDistance = 500;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.maxPolarAngle = Math.PI;");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "var oLoader = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" + "var oLoader2 = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" +"var oLoader3 = new THREE.OBJLoader();");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader.load(\'" + name1 + "\', function(object, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xa65e00" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object.visible = !object.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader2.load(\'" + name2 + "\', function(object2, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xff0000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object2.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object2.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object2.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object2.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object2.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object2);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow2').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object2.visible = !object2.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader3.load(\'" + name3 + "\', function(object3, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0x0000ff" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object3.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object3.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object3.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object3.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object3.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object3);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow3').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object3.visible = !object3.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-1, -1, -1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-1, -1, -90);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-50, -30, 40);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "window.addEventListener('resize', onWindowResize, false);");

            bw.write("\n" + "\n" + "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "function onWindowResize() {" + "\n" + 
            "\t" + "\t" + "\t" + "camera.aspect = window.innerWidth / window.innerHeight;" + "\n" + 
            "\t" + "\t" + "\t" + "camera.updateProjectionMatrix();" + "\t" + 
            "\t" + "\t" + "\t" + "renderer.setSize(window.innerWidth, window.innerHeight);" + "\t" + 
            "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "function animate() {" + "\n" + 
            "\t" + "\t" + "\t" + "requestAnimationFrame(animate);" + "\n" + 
            "\t" + "\t" + "\t" + "controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true" + "\n" + 
            "\t" + "\t" + "\t" + "render();" + "\n" + 
            "\t" + "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "function render() {" + "\n" + 
            "\t" + "\t" + "\t" + "renderer.render(scene, camera);" + "\n" + 
            "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "</script>" + "\n" + 
            "\t" + "</body>" + "\n" + 
            "\t" + "</html>");

            bw.close();
            System.out.println("Successfully wrote to the file.");
          } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
      }

      public static void fileWriter2(String name1, String name2, String name3, String name4){
        try {
            FileWriter myWriter = new FileWriter("filename.html");
            BufferedWriter bw = new BufferedWriter(myWriter);
            //myWriter.write("Files in Java might be tricky, " + name1 + " but it is fun enough!"); //uses the passed parameters
            //myWriter.close();
            bw.write("<!DOCTYPE html>");
            bw.write("\n" + "<html lang=\"en\">");
            bw.write("\n" + "<head>");
            bw.write(" <title>2018017-01 High Resolution</title>" + "\n" + 
            "<meta charset=\"utf-8\">" + "\n" + 
            "<meta name=\"viewport\" content=\"width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0\">");
            bw.write("\n" + "\n" + "<style>" + "\n" + 
            "@import url('https://fonts.googleapis.com/css2?family=Krona+One&display=swap');" + "\n" +
            "body {" + "\n" + 
               "/*background-color: #ccc;*/" + "\n" + 
                "background-color: black;" + "\n" + 
                "color: #000;" + "\n" + "}");
            bw.write("\n" + "\n" + "\t" + "a {" + "\n" + 
                "\t" + "\t" + "color: #f00;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".overlay {" + "\n" + 
                "height: 100%;" + "\n" + 
                "width: 0;" + "\n" + 
                "position: fixed;" + "\n" + 
                "z-index: 1;" + "\n" + 
                "top: 0;" + "\n" + 
                "left: 0;" + "\n" + 
                "background-color: rgb(0,0,0);" + "\n" + 
                "background-color: rgba(0,0,0, 0.9);" + "\n" + 
                "overflow-x: hidden;" + "\n" + 
                "transition: 0.5s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".overlay-content {" + "\n" + 
                "position: relative;" + "\n" +
                "top: 5%;" + "\n" + 
                "width: 100%;" + "\n" + 
                "text-align: center;" + "\n" + 
                "margin-top: 30px;" + "\n" + 
                "color: white;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".overlay a {" + "\n" + 
                "padding: 8px;" + "\n" + 
                "text-decoration: none;" + "\n" + 
                "font-size: 36px;" + "\n" + 
                "color: #818181;" + "\n" + 
                "display: block;" + "\n" + 
                "transition: 0.3s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".overlay a:hover, .overlay a:focus {" + "\n" + 
                "color: #f1f1f1;" + "\n" + 
                "}");
            bw.write(".overlay .closebtn {" + "\n" + 
                "position: absolute;" + "\n" + 
                "top: 20px;" + "\n" + 
                "right: 45px;" + "\n" + 
                "font-size: 60px;" + "\n" +
                "}");
            bw.write("\n" + "\n" + "@media screen and (max-height: 450px) {" + "\n" + 
                ".overlay a {font-size: 20px}" + "\n" + 
                ".overlay .closebtn {" + "\n" + 
                "font-size: 40px;" + "\n" + 
                "top: 15px;" + "\n" + 
                "right: 35px;" + "\n" + 
                "}" + "\n" + 
                "}");
            
            bw.write("\n" + "\n" + ".sidebar{" + "\n" + 
                "position: fixed;" + "\n" + 
                "width: 200px;" + "\n" + 
                "top:0;" + "\n" + 
                "left: 0;" + "\n" + 
                "bottom: 0;" + "\n" + 
                "background: grey;" + "\n" + 
                "padding-top: 50px;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar h1{" + "\n" + 
                "display: block;" + "\n" + 
                "padding: 10px 20px;" + "\n" + 
                "color: #fff;" + "\n" + 
                "text-decoration: none;" + "\n" + 
                "font-family: \"Rubik\";" + "\n" + 
                "letter-spacing: 2px;" + "\n" + 
                "font-weight: 400;" + "\n" + 
                "margin: 0;" + "\n" + 
                "font-size: 20px;" + "\n" + 
                "text-transform: uppercase;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a {" + "\n" + 
                "display: block;" + "\n" + 
                "padding: 10px 20px;" + "\n" + 
                "color: #bbb;" + "\n" + 
                "outline: none;" + "\n" + 
                "border: none;" + "\n" + 
                "background: none;" + "\n" + 
                "text-decoration: none;" + "\n" + 
                "font-family: \"Rubik\";" + "\n" + 
                "letter-spacing: 2px;" + "\n" + 
                
                "}");
            bw.write("\n" + "\n" + ".dropdown-btn{" + "\n" + 
                "font-size: 15px;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a:hover{" + "\n" + 
                "color: #fff;" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.hoverspeed:hover{" + "\n" + 
                "color: #fff;" + "\n" + 
                "margin-left: 7px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a.yellow{" + "\n" + 
                "background-color: yellow;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.yellow:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.red{" + "\n" + 
                "background-color: red;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.red:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.blue{" + "\n" + 
                "background-color: blue;" + "\n" + 
                "color: white;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a.blue:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" +  
                "transition: 0.4s;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a.green{" + "\n" + 
                "background-color: green;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.green:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.info:hover{" + "\n" + 
                "background-color: black;" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" +"\n" + 
            "}");
            bw.write("\n" + "\n" + "</style>" + "\n" + 
            "</head>");
            bw.write("\n" + "\n" + "<body>" + "\n" + 

            "\t" + "<div class=\"sidebar\">" + "\n" + 
                "\t" + "\t" + "<a href=\"https://apil.ca/\" class=\"hoverspeed\"><img src=\"https://apillogo.s3.ca-central-1.amazonaws.com/APIL_LOGO.png\" alt=\"Apil\" width=\"175\" height=\"75\" style=\"vertical-align:left;margin:0px -5px\"></a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Aorta\" class=\"yellow\" id=\"hideShow\">Aorta</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Pulmonary Artery\" class=\"green\" id=\"hideShow2\">Pulmonary Artery</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Left Atrium\" class=\"red\" id=\"hideShow3\">Left Side</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Right Atrium\" class=\"blue\" id=\"hideShow4\">Right Side</a>");
            bw.write("\n" + "</div>");
            bw.write("\n" + "\t" + "<script src=\"three.js\"></script>" + "\n" + 
           "\t" + "<script src=\"OrbitControls.js\"></script>" + "\n" + 
            "\t" + "<script src=\"GLTFLoader.js\"></script>" + "\n" + 
            "\t" + "<script src=\"OBJLoader.js\"></script>" + "\n" + 
            "\t" + "<script src=\"WebGL.js\"></script>");
            bw.write("\n" + "\n" + "\t" + "<script>");
            bw.write("\n" + "\n" + "\t" + "\t" + "var camera, controls, scene, renderer, object, object2, object3, object4, object5, object6;" + "\n" + 
            "\t" + "\t" + "var objhidden = false;" + "\n" + 
            "\t" + "\t" + "init();");
            bw.write("\n" + "\n" + "\t" + "\t" + "animate();" + "\n" + 
            "\t" + "\t" + "function init() {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + " scene = new THREE.Scene();" +"\n" + 
            "\t" + "\t" + "\t" + "scene.background = new THREE.Color(0x000000);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + " renderer = new THREE.WebGLRenderer({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "antialias: true"+ "\n" + 
            "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "renderer.setPixelRatio(window.devicePixelRatio);" + "\n" + 
            "\t" + "\t" + "\t" + "renderer.setSize(window.innerWidth, window.innerHeight);" + "\n" + 
            "\t" + "\t" + "\t" + "document.body.appendChild(renderer.domElement);" + "\n" + 
            "\t" + "\t" + "\t" + "camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);" + "\n" + 
            "\t" + "\t" + "\t" + "camera.position.set(0, 0, -400);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "controls = new THREE.OrbitControls(camera, renderer.domElement);" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "//controls.addEventListener( 'change', render ); // call this only in static scenes (i.e., if there is no animation loop)" + "\n" +
            "\t" + "\t" + "\t" + "controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled" + "\n" + 
            "\t" + "\t" + "\t" + "controls.dampingFactor = 0.25;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.screenSpacePanning = false;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.minDistance = 100;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.maxDistance = 500;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.maxPolarAngle = Math.PI;");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "var oLoader = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" + "var oLoader2 = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" +"var oLoader3 = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" +"var oLoader4 = new THREE.OBJLoader();");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader.load(\'" + name1 + "\', function(object, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xa65e00" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object.visible = !object.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader2.load(\'" + name2 + "\', function(object2, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0x008000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object2.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object2.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object2.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object2.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object2.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object2);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow2').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object2.visible = !object2.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader3.load(\'" + name3 + "\', function(object3, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xFF0000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object3.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object3.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object3.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object3.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object3.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object3);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow3').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object3.visible = !object3.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader4.load(\'" + name4 + "\', function(object4, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xFF0000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object4.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object4.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object4.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object4.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object4.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object4);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow4').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object4.visible = !object4.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-1, -1, -1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-1, -1, -90);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-1, -90 , -90);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-50, -30 , 40);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "window.addEventListener('resize', onWindowResize, false);");

            bw.write("\n" + "\n" + "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "function onWindowResize() {" + "\n" + 
            "\t" + "\t" + "\t" + "camera.aspect = window.innerWidth / window.innerHeight;" + "\n" + 
            "\t" + "\t" + "\t" + "camera.updateProjectionMatrix();" + "\t" + 
            "\t" + "\t" + "\t" + "renderer.setSize(window.innerWidth, window.innerHeight);" + "\t" + 
            "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "function animate() {" + "\n" + 
            "\t" + "\t" + "\t" + "requestAnimationFrame(animate);" + "\n" + 
            "\t" + "\t" + "\t" + "controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true" + "\n" + 
            "\t" + "\t" + "\t" + "render();" + "\n" + 
            "\t" + "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "function render() {" + "\n" + 
            "\t" + "\t" + "\t" + "renderer.render(scene, camera);" + "\n" + 
            "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "</script>" + "\n" + 
            "\t" + "</body>" + "\n" + 
            "\t" + "</html>");

            bw.close();
            System.out.println("Successfully wrote to the file.");
          } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
      }

      public static void fileWriter3(String name1, String name2, String name3, String name4, String name5){
        try {
            FileWriter myWriter = new FileWriter("filename.html");
            BufferedWriter bw = new BufferedWriter(myWriter);
            //myWriter.write("Files in Java might be tricky, " + name1 + " but it is fun enough!"); //uses the passed parameters
            //myWriter.close();
            bw.write("<!DOCTYPE html>");
            bw.write("\n" + "<html lang=\"en\">");
            bw.write("\n" + "<head>");
            bw.write(" <title>2018017-01 High Resolution</title>" + "\n" + 
            "<meta charset=\"utf-8\">" + "\n" + 
            "<meta name=\"viewport\" content=\"width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0\">");
            bw.write("\n" + "\n" + "<style>" + "\n" + 
            "@import url('https://fonts.googleapis.com/css2?family=Krona+One&display=swap');" + "\n" +
            "body {" + "\n" + 
               "/*background-color: #ccc;*/" + "\n" + 
                "background-color: black;" + "\n" + 
                "color: #000;" + "\n" + "}");
            bw.write("\n" + "\n" + "\t" + "a {" + "\n" + 
                "\t" + "\t" + "color: #f00;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".overlay {" + "\n" + 
                "height: 100%;" + "\n" + 
                "width: 0;" + "\n" + 
                "position: fixed;" + "\n" + 
                "z-index: 1;" + "\n" + 
                "top: 0;" + "\n" + 
                "left: 0;" + "\n" + 
                "background-color: rgb(0,0,0);" + "\n" + 
                "background-color: rgba(0,0,0, 0.9);" + "\n" + 
                "overflow-x: hidden;" + "\n" + 
                "transition: 0.5s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".overlay-content {" + "\n" + 
                "position: relative;" + "\n" +
                "top: 5%;" + "\n" + 
                "width: 100%;" + "\n" + 
                "text-align: center;" + "\n" + 
                "margin-top: 30px;" + "\n" + 
                "color: white;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".overlay a {" + "\n" + 
                "padding: 8px;" + "\n" + 
                "text-decoration: none;" + "\n" + 
                "font-size: 36px;" + "\n" + 
                "color: #818181;" + "\n" + 
                "display: block;" + "\n" + 
                "transition: 0.3s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".overlay a:hover, .overlay a:focus {" + "\n" + 
                "color: #f1f1f1;" + "\n" + 
                "}");
            bw.write(".overlay .closebtn {" + "\n" + 
                "position: absolute;" + "\n" + 
                "top: 20px;" + "\n" + 
                "right: 45px;" + "\n" + 
                "font-size: 60px;" + "\n" +
                "}");
            bw.write("\n" + "\n" + "@media screen and (max-height: 450px) {" + "\n" + 
                ".overlay a {font-size: 20px}" + "\n" + 
                ".overlay .closebtn {" + "\n" + 
                "font-size: 40px;" + "\n" + 
                "top: 15px;" + "\n" + 
                "right: 35px;" + "\n" + 
                "}" + "\n" + 
                "}");
            
            bw.write("\n" + "\n" + ".sidebar{" + "\n" + 
                "position: fixed;" + "\n" + 
                "width: 200px;" + "\n" + 
                "top:0;" + "\n" + 
                "left: 0;" + "\n" + 
                "bottom: 0;" + "\n" + 
                "background: grey;" + "\n" + 
                "padding-top: 50px;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar h1{" + "\n" + 
                "display: block;" + "\n" + 
                "padding: 10px 20px;" + "\n" + 
                "color: #fff;" + "\n" + 
                "text-decoration: none;" + "\n" + 
                "font-family: \"Rubik\";" + "\n" + 
                "letter-spacing: 2px;" + "\n" + 
                "font-weight: 400;" + "\n" + 
                "margin: 0;" + "\n" + 
                "font-size: 20px;" + "\n" + 
                "text-transform: uppercase;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a {" + "\n" + 
                "display: block;" + "\n" + 
                "padding: 10px 20px;" + "\n" + 
                "color: #bbb;" + "\n" + 
                "outline: none;" + "\n" + 
                "border: none;" + "\n" + 
                "background: none;" + "\n" + 
                "text-decoration: none;" + "\n" + 
                "font-family: \"Rubik\";" + "\n" + 
                "letter-spacing: 2px;" + "\n" + 
                
                "}");
            bw.write("\n" + "\n" + ".dropdown-btn{" + "\n" + 
                "font-size: 15px;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a:hover{" + "\n" + 
                "color: #fff;" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.hoverspeed:hover{" + "\n" + 
                "color: #fff;" + "\n" + 
                "margin-left: 7px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a.yellow{" + "\n" + 
                "background-color: yellow;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.yellow:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.red{" + "\n" + 
                "background-color: red;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.red:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.blue{" + "\n" + 
                "background-color: blue;" + "\n" + 
                "color: black;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a.blue:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" +  
                "transition: 0.4s;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a.green{" + "\n" + 
                "background-color: green;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.green:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.skyBlue{" + "\n" + 
                "background-color: skyBlue;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.skyBlue:hover{" + "\n" +  
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.orange{" + "\n" + 
                "background-color: orange;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.orange:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.info:hover{" + "\n" + 
                "background-color: black;" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" +"\n" + 
            "}");
            bw.write("\n" + "\n" + "</style>" + "\n" + 
            "</head>");
            bw.write("\n" + "\n" + "<body>" + "\n" + 

            "\t" + "<div class=\"sidebar\">" + "\n" + 
                "\t" + "\t" + "<a href=\"https://apil.ca/\" class=\"hoverspeed\"><img src=\"https://apillogo.s3.ca-central-1.amazonaws.com/APIL_LOGO.png\" alt=\"Apil\" width=\"175\" height=\"75\" style=\"vertical-align:left;margin:0px -5px\"></a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Aorta\" class=\"yellow\" id=\"hideShow\">Aorta</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Pulmonary Artery\" class=\"green\" id=\"hideShow2\">Pulmonary Artery</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Left Atrium\" class=\"orange\" id=\"hideShow3\">Left Atrium</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Right Atrium\" class=\"skyBlue\" id=\"hideShow4\">Right Atrium</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Left Ventricle\" class=\"red\" id=\"hideShow5\">Left Ventricle</a>");
            bw.write("\n" + "</div>");
            bw.write("\n" + "\t" + "<script src=\"three.js\"></script>" + "\n" + 
           "\t" + "<script src=\"OrbitControls.js\"></script>" + "\n" + 
            "\t" + "<script src=\"GLTFLoader.js\"></script>" + "\n" + 
            "\t" + "<script src=\"OBJLoader.js\"></script>" + "\n" + 
            "\t" + "<script src=\"WebGL.js\"></script>");
            bw.write("\n" + "\n" + "\t" + "<script>");
            bw.write("\n" + "\n" + "\t" + "\t" + "var camera, controls, scene, renderer, object, object2, object3, object4, object5, object6;" + "\n" + 
            "\t" + "\t" + "var objhidden = false;" + "\n" + 
            "\t" + "\t" + "init();");
            bw.write("\n" + "\n" + "\t" + "\t" + "animate();" + "\n" + 
            "\t" + "\t" + "function init() {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + " scene = new THREE.Scene();" +"\n" + 
            "\t" + "\t" + "\t" + "scene.background = new THREE.Color(0x000000);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + " renderer = new THREE.WebGLRenderer({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "antialias: true"+ "\n" + 
            "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "renderer.setPixelRatio(window.devicePixelRatio);" + "\n" + 
            "\t" + "\t" + "\t" + "renderer.setSize(window.innerWidth, window.innerHeight);" + "\n" + 
            "\t" + "\t" + "\t" + "document.body.appendChild(renderer.domElement);" + "\n" + 
            "\t" + "\t" + "\t" + "camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);" + "\n" + 
            "\t" + "\t" + "\t" + "camera.position.set(0, 0, -400);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "controls = new THREE.OrbitControls(camera, renderer.domElement);" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "//controls.addEventListener( 'change', render ); // call this only in static scenes (i.e., if there is no animation loop)" + "\n" +
            "\t" + "\t" + "\t" + "controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled" + "\n" + 
            "\t" + "\t" + "\t" + "controls.dampingFactor = 0.25;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.screenSpacePanning = false;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.minDistance = 100;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.maxDistance = 500;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.maxPolarAngle = Math.PI;");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "var oLoader = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" + "var oLoader2 = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" +"var oLoader3 = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" +"var oLoader4 = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" +"var oLoader5 = new THREE.OBJLoader();");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader.load(\'" + name1 + "\', function(object, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xa65e00" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object.visible = !object.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader2.load(\'" + name2 + "\', function(object2, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0x008000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object2.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object2.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object2.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object2.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object2.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object2);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow2').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object2.visible = !object2.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader3.load(\'" + name3 + "\', function(object3, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xFF0000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object3.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object3.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object3.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object3.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object3.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object3);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow3').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object3.visible = !object3.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader4.load(\'" + name4 + "\', function(object4, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xFF0000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object4.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object4.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object4.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object4.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object4.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object4);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow4').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object4.visible = !object4.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader5.load(\'" + name5 + "\', function(object5, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xFF0000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object5.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object5.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object5.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object5.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object5.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object5);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow5').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object5.visible = !object5.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-1, -1, -1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-1, -1, -90);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-50, -30 , 40);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "window.addEventListener('resize', onWindowResize, false);");

            bw.write("\n" + "\n" + "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "function onWindowResize() {" + "\n" + 
            "\t" + "\t" + "\t" + "camera.aspect = window.innerWidth / window.innerHeight;" + "\n" + 
            "\t" + "\t" + "\t" + "camera.updateProjectionMatrix();" + "\t" + 
            "\t" + "\t" + "\t" + "renderer.setSize(window.innerWidth, window.innerHeight);" + "\t" + 
            "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "function animate() {" + "\n" + 
            "\t" + "\t" + "\t" + "requestAnimationFrame(animate);" + "\n" + 
            "\t" + "\t" + "\t" + "controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true" + "\n" + 
            "\t" + "\t" + "\t" + "render();" + "\n" + 
            "\t" + "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "function render() {" + "\n" + 
            "\t" + "\t" + "\t" + "renderer.render(scene, camera);" + "\n" + 
            "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "</script>" + "\n" + 
            "\t" + "</body>" + "\n" + 
            "\t" + "</html>");

            bw.close();
            System.out.println("Successfully wrote to the file.");
          } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
      }

      public static void fileWriter4(String name1, String name2, String name3, String name4, String name5, String name6){
        try {
            FileWriter myWriter = new FileWriter("filename.html");
            BufferedWriter bw = new BufferedWriter(myWriter);
            //myWriter.write("Files in Java might be tricky, " + name1 + " but it is fun enough!"); //uses the passed parameters
            //myWriter.close();
            bw.write("<!DOCTYPE html>");
            bw.write("\n" + "<html lang=\"en\">");
            bw.write("\n" + "<head>");
            bw.write(" <title>2018017-01 High Resolution</title>" + "\n" + 
            "<meta charset=\"utf-8\">" + "\n" + 
            "<meta name=\"viewport\" content=\"width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0\">");
            bw.write("\n" + "\n" + "<style>" + "\n" + 
            "@import url('https://fonts.googleapis.com/css2?family=Krona+One&display=swap');" + "\n" +
            "body {" + "\n" + 
               "/*background-color: #ccc;*/" + "\n" + 
                "background-color: black;" + "\n" + 
                "color: #000;" + "\n" + "}");
            bw.write("\n" + "\n" + "\t" + "a {" + "\n" + 
                "\t" + "\t" + "color: #f00;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".overlay {" + "\n" + 
                "height: 100%;" + "\n" + 
                "width: 0;" + "\n" + 
                "position: fixed;" + "\n" + 
                "z-index: 1;" + "\n" + 
                "top: 0;" + "\n" + 
                "left: 0;" + "\n" + 
                "background-color: rgb(0,0,0);" + "\n" + 
                "background-color: rgba(0,0,0, 0.9);" + "\n" + 
                "overflow-x: hidden;" + "\n" + 
                "transition: 0.5s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".overlay-content {" + "\n" + 
                "position: relative;" + "\n" +
                "top: 5%;" + "\n" + 
                "width: 100%;" + "\n" + 
                "text-align: center;" + "\n" + 
                "margin-top: 30px;" + "\n" + 
                "color: white;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".overlay a {" + "\n" + 
                "padding: 8px;" + "\n" + 
                "text-decoration: none;" + "\n" + 
                "font-size: 36px;" + "\n" + 
                "color: #818181;" + "\n" + 
                "display: block;" + "\n" + 
                "transition: 0.3s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".overlay a:hover, .overlay a:focus {" + "\n" + 
                "color: #f1f1f1;" + "\n" + 
                "}");
            bw.write(".overlay .closebtn {" + "\n" + 
                "position: absolute;" + "\n" + 
                "top: 20px;" + "\n" + 
                "right: 45px;" + "\n" + 
                "font-size: 60px;" + "\n" +
                "}");
            bw.write("\n" + "\n" + "@media screen and (max-height: 450px) {" + "\n" + 
                ".overlay a {font-size: 20px}" + "\n" + 
                ".overlay .closebtn {" + "\n" + 
                "font-size: 40px;" + "\n" + 
                "top: 15px;" + "\n" + 
                "right: 35px;" + "\n" + 
                "}" + "\n" + 
                "}");
            
            bw.write("\n" + "\n" + ".sidebar{" + "\n" + 
                "position: fixed;" + "\n" + 
                "width: 200px;" + "\n" + 
                "top:0;" + "\n" + 
                "left: 0;" + "\n" + 
                "bottom: 0;" + "\n" + 
                "background: grey;" + "\n" + 
                "padding-top: 50px;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar h1{" + "\n" + 
                "display: block;" + "\n" + 
                "padding: 10px 20px;" + "\n" + 
                "color: #fff;" + "\n" + 
                "text-decoration: none;" + "\n" + 
                "font-family: \"Rubik\";" + "\n" + 
                "letter-spacing: 2px;" + "\n" + 
                "font-weight: 400;" + "\n" + 
                "margin: 0;" + "\n" + 
                "font-size: 20px;" + "\n" + 
                "text-transform: uppercase;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a {" + "\n" + 
                "display: block;" + "\n" + 
                "padding: 10px 20px;" + "\n" + 
                "color: #bbb;" + "\n" + 
                "outline: none;" + "\n" + 
                "border: none;" + "\n" + 
                "background: none;" + "\n" + 
                "text-decoration: none;" + "\n" + 
                "font-family: \"Rubik\";" + "\n" + 
                "letter-spacing: 2px;" + "\n" + 
                
                "}");
            bw.write("\n" + "\n" + ".dropdown-btn{" + "\n" + 
                "font-size: 15px;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a:hover{" + "\n" + 
                "color: #fff;" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.hoverspeed:hover{" + "\n" + 
                "color: #fff;" + "\n" + 
                "margin-left: 7px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a.yellow{" + "\n" + 
                "background-color: yellow;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.yellow:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.red{" + "\n" + 
                "background-color: red;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.red:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.blue{" + "\n" + 
                "background-color: blue;" + "\n" + 
                "color: black;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a.blue:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" +  
                "transition: 0.4s;" + "\n" + 
            "}");
            bw.write("\n" + "\n" + ".sidebar a.green{" + "\n" + 
                "background-color: green;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.green:hover{" + "\n" +  
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.skyBlue{" + "\n" + 
                "background-color: skyBlue;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.skyBlue:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.orange{" + "\n" + 
                "background-color: orange;" + "\n" + 
                "color:black;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.orange:hover{" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" + "\n" + 
                "}");
            bw.write("\n" + "\n" + ".sidebar a.info:hover{" + "\n" + 
                "background-color: black;" + "\n" + 
                "margin-left: 10px;" + "\n" + 
                "transition: 0.4s;" +"\n" + 
            "}");
            bw.write("\n" + "\n" + "</style>" + "\n" + 
            "</head>");
            bw.write("\n" + "\n" + "<body>" + "\n" + 

            "\t" + "<div class=\"sidebar\">" + "\n" + 
                "\t" + "\t" + "<a href=\"https://apil.ca/\" class=\"hoverspeed\"><img src=\"https://apillogo.s3.ca-central-1.amazonaws.com/APIL_LOGO.png\" alt=\"Apil\" width=\"175\" height=\"75\" style=\"vertical-align:left;margin:0px -5px\"></a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Aorta\" class=\"yellow\" id=\"hideShow\">Aorta</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Pulmonary Artery\" class=\"green\" id=\"hideShow2\">Pulmonary Artery</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Left Atrium\" class=\"orange\" id=\"hideShow3\">Left Atrium</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Right Atrium\" class=\"skyBlue\" id=\"hideShow4\">Right Atrium</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Left Ventricle\" class=\"red\" id=\"hideShow5\">Left Ventricle</a>" + "\n" + 
                "\t" + "\t" + "<a href=\"#Left Ventricle\" class=\"blue\" id=\"hideShow5\">Right Ventricle</a>");
            bw.write("\n" + "</div>");
            bw.write("\n" + "\t" + "<script src=\"three.js\"></script>" + "\n" + 
           "\t" + "<script src=\"OrbitControls.js\"></script>" + "\n" + 
            "\t" + "<script src=\"GLTFLoader.js\"></script>" + "\n" + 
            "\t" + "<script src=\"OBJLoader.js\"></script>" + "\n" + 
            "\t" + "<script src=\"WebGL.js\"></script>");
            bw.write("\n" + "\n" + "\t" + "<script>");
            bw.write("\n" + "\n" + "\t" + "\t" + "var camera, controls, scene, renderer, object, object2, object3, object4, object5, object6;" + "\n" + 
            "\t" + "\t" + "var objhidden = false;" + "\n" + 
            "\t" + "\t" + "init();");
            bw.write("\n" + "\n" + "\t" + "\t" + "animate();" + "\n" + 
            "\t" + "\t" + "function init() {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + " scene = new THREE.Scene();" +"\n" + 
            "\t" + "\t" + "\t" + "scene.background = new THREE.Color(0x000000);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + " renderer = new THREE.WebGLRenderer({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "antialias: true"+ "\n" + 
            "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "renderer.setPixelRatio(window.devicePixelRatio);" + "\n" + 
            "\t" + "\t" + "\t" + "renderer.setSize(window.innerWidth, window.innerHeight);" + "\n" + 
            "\t" + "\t" + "\t" + "document.body.appendChild(renderer.domElement);" + "\n" + 
            "\t" + "\t" + "\t" + "camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);" + "\n" + 
            "\t" + "\t" + "\t" + "camera.position.set(0, 0, -400);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "controls = new THREE.OrbitControls(camera, renderer.domElement);" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "//controls.addEventListener( 'change', render ); // call this only in static scenes (i.e., if there is no animation loop)" + "\n" +
            "\t" + "\t" + "\t" + "controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled" + "\n" + 
            "\t" + "\t" + "\t" + "controls.dampingFactor = 0.25;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.screenSpacePanning = false;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.minDistance = 100;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.maxDistance = 500;" + "\n" + 
            "\t" + "\t" + "\t" + "controls.maxPolarAngle = Math.PI;");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "var oLoader = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" + "var oLoader2 = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" +"var oLoader3 = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" +"var oLoader4 = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" +"var oLoader5 = new THREE.OBJLoader();" + "\n" + 
            "\t" + "\t" + "\t" +"var oLoader6 = new THREE.OBJLoader();");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader.load(\'" + name1 + "\', function(object, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xa65e00" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object.visible = !object.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader2.load(\'" + name2 + "\', function(object2, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0x008000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object2.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object2.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object2.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object2.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object2.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object2);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow2').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object2.visible = !object2.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader3.load(\'" + name3 + "\', function(object3, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xFF0000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object3.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object3.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object3.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object3.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object3.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object3);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow3').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object3.visible = !object3.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader4.load(\'" + name4 + "\', function(object4, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xFF0000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object4.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object4.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object4.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object4.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object4.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object4);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow4').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object4.visible = !object4.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader5.load(\'" + name5 + "\', function(object5, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xFF0000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object5.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object5.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object5.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object5.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object5.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object5);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow5').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object5.visible = !object5.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "oLoader6.load(\'" + name6 + "\', function(object6, materials) {");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "\t" + "// var material = new THREE.MeshFaceMaterial(materials);" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "var material2 = new THREE.MeshLambertMaterial({" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "color: 0xFF0000" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object6.traverse(function(child) {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "if (child instanceof THREE.Mesh) {" + "\n" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "// apply custom material" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.material = material2;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "// enable casting shadows" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.castShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "\t" + "child.receiveShadow = true;" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "}" + "\n" + 
            "\t" + "\t" + "\t" + "});");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "object6.position.x = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object6.position.y = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object6.position.z = 0;" + "\n" + 
            "\t" + "\t" + "\t" + "object6.scale.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(object6);");
            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "document.getElementById('hideShow6').addEventListener('click', function() {" + "\n" + 
            "\t" + "\t" + "\t" + "\t" + "object6.visible = !object6.visible;" + "\n" + 
            "\t" + "\t" + "\t" + "});" + "\n" + 
            "\t" + "\t" + "\t" + "});");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(1, 1, 1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-1, -1, -1);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-1, -1, -90);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "// lights" + "\n" + 
            "\t" + "\t" + "\t" + "var light = new THREE.DirectionalLight(0xffffff, 2);" + "\n" + 
            "\t" + "\t" + "\t" + "light.position.set(-50, -30 , 40);" + "\n" + 
            "\t" + "\t" + "\t" + "scene.add(light);");

            bw.write("\n" + "\n" + "\t" + "\t" + "\t" + "window.addEventListener('resize', onWindowResize, false);");

            bw.write("\n" + "\n" + "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "function onWindowResize() {" + "\n" + 
            "\t" + "\t" + "\t" + "camera.aspect = window.innerWidth / window.innerHeight;" + "\n" + 
            "\t" + "\t" + "\t" + "camera.updateProjectionMatrix();" + "\t" + 
            "\t" + "\t" + "\t" + "renderer.setSize(window.innerWidth, window.innerHeight);" + "\t" + 
            "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "function animate() {" + "\n" + 
            "\t" + "\t" + "\t" + "requestAnimationFrame(animate);" + "\n" + 
            "\t" + "\t" + "\t" + "controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true" + "\n" + 
            "\t" + "\t" + "\t" + "render();" + "\n" + 
            "\t" + "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "function render() {" + "\n" + 
            "\t" + "\t" + "\t" + "renderer.render(scene, camera);" + "\n" + 
            "\t" + "\t" + "}");

            bw.write("\n" + "\n" + "\t" + "\t" + "</script>" + "\n" + 
            "\t" + "</body>" + "\n" + 
            "\t" + "</html>");

            bw.close();
            System.out.println("Successfully wrote to the file.");
          } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
      }

}

