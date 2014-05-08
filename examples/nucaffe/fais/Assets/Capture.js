#pragma strict
import System.IO;

// Take a shot immediately
function Start () {
	UploadPNG ();
}

function Update () {
//	UploadPNG();
}
	
function UploadPNG () {
	// We should only read the screen buffer after rendering is complete
	yield WaitForEndOfFrame();
	// Create a texture the size of the screen, RGB24 format
	var width = Screen.width;
	var height = Screen.height;
	var tex = new Texture2D (width, height, TextureFormat.RGB24, false);
	// Read screen contents into the texture
	tex.ReadPixels (Rect(0, 0, width, height), 0, 0);
	tex.Apply ();
	// Encode texture into PNG
	var bytes = tex.EncodeToPNG();
	Destroy (tex);
	// For testing purposes, also write to a file in the project folder
	File.WriteAllBytes(Application.dataPath + "/../SavedScreen.png", bytes);
	
	// Create a Web Form
//	var form = new WWWForm();
//	form.AddField("frameCount", Time.frameCount.ToString());
//	form.AddBinaryData("fileUpload",bytes);
//	// Upload to a cgi script
//	var w = WWW("http:/localhostcgi-bin/env.cgi?post", form);
//	yield w;
//	if (w.error != null) {
//		print(w.error);
//	} else {
//		print("Finished Uploading Screenshot");
//	}	
}