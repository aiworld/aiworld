using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Threading;
using System;
using System.Net;

public class HTTPServer : MonoBehaviour {
	HttpWebRequest myHttpWebRequest;
	HttpWebResponse myHttpWebResponse;
	System.Object thisLock = new System.Object();
	
	GameObject player;
	int playerNum;
	AutoFire shotJudge;
	PlayerMoveController controller;
	Trigger trigger;
	Health health;
	byte[] screen;

	// Two MouseLook scripts now.
	// 1. Eye script for vertical.
	// 2. Body script for horizontal.
	List<MouseLook> mouseLooks = new List<MouseLook>();
	
	// Use this for initialization
	void Start() {
	}

	public void StartServer () {
		player = transform.gameObject;
		controller        =  player.GetComponent           < PlayerMoveController >();
		trigger           =  player.GetComponentInChildren < Trigger              >();
		shotJudge         =  player.GetComponentInChildren < AutoFire             >();
		playerNum         =  player.GetComponent           < PlayerScore          >().playerNum;
		health            =  player.GetComponent           < Health               >();
		mouseLooks.AddRange( player.GetComponents          < MouseLook            >());
		Debug.Log("player num " + playerNum);

		if(playerNum == 2) {
			controller.isNPC = true;
		}

		new Thread(this.EventLoop).Start();
	}

	void EventLoop() {
		var listener = this.StartHttpListener();
		while (true) {
			// The GetContext method blocks while waiting for a request.
			Debug.Log("before reading request");
			HttpListenerContext context = listener.GetContext();
			Debug.Log("before handling request");
			Dictionary<string, string> responseHeaders = null;
			try {
				responseHeaders = this.HandleRequest(context.Request);
			} catch(Exception e) {
				Debug.Log("problem with request" + e.Message);	
				return;
			}
			Debug.Log("after reading request");

			try {
				this.SendResponse(responseHeaders, context.Response);
			} catch(Exception e) {
				Debug.Log("problem with response");
			}

//			this.SendTextResponse("yo", context.Response);
			Debug.Log("after sending response");
		}
		listener.Stop();
	}

	Dictionary<string, string> HandleRequest(HttpListenerRequest request) {
		Dictionary<string, string> responseHeaders = new Dictionary<string, string>();

		var queryString = this.ParseQueryString(request.Url.Query);
		Debug.Log(request.Url.Query);
		if(queryString.Count == 0) {
			responseHeaders.Add("Fais-Error", "please send move_x, move_y, look_x, look_y, jump, and shoot");
			return responseHeaders;
		}
	
		bool jump;
		bool shoot;
		float move_x;
		float move_y;
		float look_x;
		float look_y;

		try {
			jump   =  bool.Parse(queryString["jump"  ].ToLower());
			shoot  =  bool.Parse(queryString["shoot" ].ToLower());
			move_x = float.Parse(queryString["move_x"]);
			move_y = float.Parse(queryString["move_y"]);
			look_x = float.Parse(queryString["look_x"]);
			look_y = float.Parse(queryString["look_y"]);
		} catch(Exception e) {
			responseHeaders.Add("Fais-Error", "input not correct. try something like: /?shoot=False&move_x=-0.585790557602&move_y=-0.0782275326677&look_x=-0.702675762832&look_y=-0.314776947275&jump=True");
			return responseHeaders;
		}


		lock(thisLock) {
			// Lock because this is called from a thread.
			// TODO: Make affected object properties volatile to prevent thread caching
			// from causing inconsistencies.
			try {
				trigger.SetState(shoot);
				controller.SetMove(move_x, move_y, jump);
				foreach(MouseLook ml in mouseLooks) {
					// Center focus and player (vertical and horizontal resp.)
					ml.SetRemoteLook(look_x, look_y);
				}
			} catch(Exception e) {
				Debug.Log("Something went wrong setting input. RELEASE THE LOCK!!!");
			}

		}

		responseHeaders.Add ("Shot-Landed" , BoolToString( shotJudge.shotLanded ));
		responseHeaders.Add ("Was-Shot"    , BoolToString( health.wasShot       ));
		responseHeaders.Add ("Jump"        , BoolToString( jump                 ));
		responseHeaders.Add ("Shoot"       , BoolToString( shoot                ));
		responseHeaders.Add ("Move-X"      ,               move_x.ToString()     );
		responseHeaders.Add ("Move-Y"      ,               move_y.ToString()     );
		responseHeaders.Add ("Look-X"      ,               look_x.ToString()     );
		responseHeaders.Add ("Look-Y"      ,               look_y.ToString()     );

		shotJudge.shotLanded = false; // Reset in case we stop firing.
		health.wasShot       = false;
		return responseHeaders;
	}

	string BoolToString(bool v) {
		if (v) {
			return "true";
		} else {
			return "false";
		}
	}

	void SendTextResponse(string responseString, HttpListenerResponse response) {
		SendByteArrayResponse(System.Text.Encoding.UTF8.GetBytes(responseString), response);	
	}

	void SendResponse(Dictionary<string, string> headers, HttpListenerResponse response) {
		response.ContentType = "image/png";
		foreach(KeyValuePair<string, string> header in headers) {
			response.AddHeader(header.Key, header.Value);
		}
		// Set was_hit, shot_landed here
//		lock(thisLock) {
			// TODO: Probably need to speed this up with a queue.
			SendByteArrayResponse(this.screen, response);
//		}
	}

	void SendByteArrayResponse(byte[] responseBytes, HttpListenerResponse response) {
		response.ContentLength64 = responseBytes.Length;
		System.IO.Stream output = response.OutputStream;
		output.Write(responseBytes, 0, responseBytes.Length);
		output.Close();	
	}
		
	HttpListener StartHttpListener() {
		if (!HttpListener.IsSupported) {
			throw new Exception("HttpListener not supported on this platform for Mono!");
		}
		HttpListener listener = new HttpListener();
		int port = 1234 + playerNum;
		string playerEndpoint = "http://*:" + port.ToString () + "/";
		Debug.Log("listening on: " + playerEndpoint);
		string[] prefixes = new string[]{playerEndpoint};
		// Add the prefixes (aka routes). 
		foreach (string s in prefixes) {
			listener.Prefixes.Add(s);
		}
		listener.Start();
		return listener;
	}

	NameValueCollection ParseQueryString(string queryString) {
		NameValueCollection queryParameters = new NameValueCollection();
		string[] querySegments = queryString.Split('&');
		foreach(string segment in querySegments)
		{
			string[] parts = segment.Split('=');
			if (parts.Length > 0)
			{
				string key = parts[0].Trim(new char[] { '?', ' ' });
				string val = parts[1].Trim();
				
				queryParameters.Add(Uri.UnescapeDataString(key), Uri.UnescapeDataString(val));
			}
		}
		return queryParameters;
	}

	public void SetScreen(byte[] _screen) {
//		lock(thisLock) {
			this.screen = _screen;
//			Debug.Log(this.screen.Length);
//		}
	}

	// Update is called once per frame
	void Update () {

	}
}
