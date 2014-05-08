using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class SpawnPlayers : MonoBehaviour {
	public static int PLAYER_COUNT = 2;

	static float VIEWPORT_RATIO;
	static float viewport_x = 0;
	static float viewport_y = 0;

	static List<GameObject> players;

	// Performance in world with one plane and a light.
	/* PLAYER_COUNT |  FPS
	 * 8            |  150
	 * 18           |  50
	 * 25           |  30
	 * 32           |  18
	 * 50           |  9 
	 */
	
	// Use this for initialization
	void Start () {
		// For PLAYER_COUNT of 8:
		// PLAYER_COUNT * 2 = numEyes = 8 * 2 = 4 ^ 2 => 16 cameras layed out 4x4.
		// VIEWPORT_RATIO = 1 / sqrt(PLAYER_COUNT * 2)
		// VIEWPORT_RATIO = 1 / 4

		VIEWPORT_RATIO = (float)1 / Mathf.Sqrt((float)PLAYER_COUNT * 2);

		foreach(GameObject player in GetPlayers()) {
			player.GetComponent<HTTPServer>().StartServer();
		}
	}

	public static List<GameObject> GetPlayers() {
		if(players == null) {
			players = new List<GameObject>();
			//		for(int i = 0; i < PLAYER_COUNT; i++) {
			//			players.add();
			//		}
			players.Add(CreatePlayer(1, -6, 2, 12, 0, 0   , 0));
			players.Add(CreatePlayer(2, -6, 2, 15, 0, 180 , 0));
			
			// Set deaths and kills accordingly
			
			
			// add back animations
		}
		return players;
	}

	public static void RecordDeath(int playerNum) {
//		Debug.Log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
		players[ playerNum - 1      ].GetComponent<PlayerScore>().deaths++;
		players[(playerNum - 1) % 2 ].GetComponent<PlayerScore>().kills++;
	}

	static GameObject CreatePlayer(int playerNum, float x, float y, float z, float xDegrees, float yDegrees, float zDegrees) {
		GameObject player = Instantiate ((GameObject)Resources.Load("Player")) as GameObject;
		player.transform.localPosition = new Vector3(x, y, z);
		player.transform.localEulerAngles = new Vector3(xDegrees, yDegrees, zDegrees);
		Transform eyes = player.transform.Find("Eyes");
		SetEyeViewport(eyes.Find("LeftEye" ).gameObject.camera);
		SetEyeViewport(eyes.Find("RightEye").gameObject.camera);
		player.GetComponent<PlayerScore>().playerNum = playerNum;
		return player;
	}
	
	static void SetEyeViewport(Camera eye)
	{
//		Debug.Log (eye.rect);
//		Debug.Log ("viewport_x, viewport_y, VIEWPORT_RATIO = " + viewport_x + " " + viewport_y + " " + VIEWPORT_RATIO);
		eye.rect = new Rect(viewport_x, viewport_y, VIEWPORT_RATIO, VIEWPORT_RATIO);
		
		viewport_x += VIEWPORT_RATIO;
		if(viewport_x >= 1.0) {
			viewport_x = 0;
			viewport_y += VIEWPORT_RATIO;
		}
		
//		Debug.Log ("After change: " + eye.rect);
	}
	
	// Update is called once per frame
	void Update () {
		//		Debug.Log("Left eye cam rect is...." + testEye.camera.rect);
	}
}