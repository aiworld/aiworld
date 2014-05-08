using UnityEngine;
using System.Collections;
using System.IO;

public class SaveScreen : MonoBehaviour {
	
	GameObject player;
	int playerNum;
	HTTPServer playerServer;

	float left;
	float top;
	int widthPixels;
	int heightPixels;

	
	
	// Use this for initialization
	void Start () {
		player = transform.gameObject;
		playerNum    = player.GetComponent<PlayerScore>().playerNum;
		playerServer = player.GetComponent<HTTPServer>();

		Transform eyes = player.transform.Find("Eyes");
		
		Debug.Log("AND THE EYES ARE");
		
		var leftRect  = eyes.Find("LeftEye"   ).gameObject.camera.rect;
		var rightRect = eyes.Find("RightEye"  ).gameObject.camera.rect;
		
		Debug.Log(eyes.Find("LeftEye"  ).gameObject.camera.rect);
		Debug.Log(eyes.Find("RightEye" ).gameObject.camera.rect);
		
		
		// (x:0.50, y:0.00, width:0.50, height:0.50) leftRect sample
		// (x:0.00, y:0.00, width:0.50, height:0.50) rightRect sample
		
		this.left = leftRect.x * (float)Screen.width;
		this.top  = leftRect.y * (float)Screen.height;
		this.widthPixels  = (int)((leftRect.width + rightRect.width) * Screen.width);  // ASSUMING WE ARE SIDE BY SIDE HERE>!>!>>!>>!! i.e. that there are an even number of eyes in x dimension of screen
		this.heightPixels = (int)( leftRect.height                   * Screen.height); // ASSUMING WE ARE SIDE BY SIDE HERE>!>!>>!>>!! i.e. that there are an even number of eyes in x dimension of 

		StartCoroutine(Capture(saveToDisk: true));
		
	}
	
	// Update is called once per frame
	void Update () {
		//		Debug.Log("making call to read pixels");
		StartCoroutine(Capture(saveToDisk: false));
	}
	
	IEnumerator Capture(bool saveToDisk) {
		//		Debug.Log("before reading pixels");
		
		// We should only read the screen buffer after rendering is complete
		yield return new WaitForEndOfFrame();
		
		//		Debug.Log("reading pixels");
		
		// Create a texture the size of the screen, RGB24 format
//		int width = Screen.width;
//		int height = Screen.height;

//		Debug.Log("Screen width "  + Screen.width);
//		Debug.Log("Screen height " + Screen.height);
//		Debug.Log("Read width " + widthPixels);
//		Debug.Log("Read height " + heightPixels);
		
		Texture2D tex = new Texture2D(widthPixels, heightPixels, TextureFormat.RGB24, false);
		tex.ReadPixels(new Rect(left, top, widthPixels, heightPixels), 0, 0);
		tex.Apply();
		
		// Encode texture into PNG
//		tex.Compress(highQuality: false);
		byte[] bytes = tex.EncodeToPNG(); // This slows us down 20fps.
		Destroy(tex);

		playerServer.SetScreen(bytes);
		
		if(saveToDisk) {
			// For testing purposes, also write to a file in the project folder
			File.WriteAllBytes(Application.dataPath + "/../SavedScreen" + playerNum.ToString() + ".png", bytes);	
		}
	}
}
