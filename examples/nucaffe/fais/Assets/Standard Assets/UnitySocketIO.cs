using UnityEngine;
using System.Collections;
using SocketIOClient;
using SimpleJson;
using System;
using System.Net;

public class UnitySocketIO: MonoBehaviour {

	private Client socket;

//	private void SocketOpened(object sender, MessageEventArgs e) {
//		//invoke when socket opened
//		client.Send("YOOOOOO!!");
//	}
//	
//	private void SocketError(object sender, MessageEventArgs e) {
//		//invoke when socket opened
//		Debug.Log("There was an error");
//	}
//	
//	private void SocketConnectionClosed(object sender, MessageEventArgs e) {
//		//invoke when socket closed
//		client.Close();
//	}
//	
//	private void SocketMessage (object sender, MessageEventArgs e) {
//		if ( e!= null && e.Message.Event == "message") {
//			string msg = e.Message.MessageText;
//			Debug.Log("i have received a message from node!");
//		}
//	}

	// Use this for initialization
	void Start () {
//		client = new Client("http://localhost:3000");
//		
////		client.Opened += SocketOpened;
////		client.Message += SocketMessage;
////		client.SocketConnectionClosed += SocketConnectionClosed;
////		client.Error +=SocketError;
//
//		client.Connect();
////
//		client.On("open", (data) => {
//			Debug.Log("open-----------------------------------------------------------------------------------------------------------------------------------");
//			client.Send("YOOOOOO!!");
//		});
////
////		client.On("close", (data) => {
////			Debug.Log("open");
////			client.Close();
////		});
////
////		client.On("message", (data) => {
////			Debug.Log(data);
////		});
////
////		client.On("error", (data) => {
////			Debug.Log(data);
////		});
////
////		System.Threading.Thread.Sleep(1000);
////
////		client.Send("YOOOOOO!!");
		/// 
		/// 


//		Debug.Log("Starting TestSocketIOClient Example...");
//		
//		socket = new Client("http://127.0.0.1:3000/"); // url to nodejs 
//		socket.Opened += SocketOpened;
//		socket.Message += SocketMessage;
//		socket.SocketConnectionClosed += SocketConnectionClosed;
//		socket.Error += SocketError;
//		
//		// register for 'connect' event with io server
//		socket.On("connect", (fn) =>
//		          {
//			Debug.Log("\r\nConnected event...\r\n");
//			Debug.Log("Emit Part object");
//			
//			// emit Json Serializable object, anonymous types, or strings
//			Part newPart = new Part() 
//			{ PartNumber = "K4P2G324EC", Code = "DDR2", Level = 1 };
//			socket.Emit("partInfo", newPart);
//		});
//		
//		// register for 'update' events - message is a json 'Part' object
//		socket.On("update", (data) =>
//		          {
//			Debug.Log("recv [socket].[update] event");
//			//Debug.Log("  raw message:      {0}", data.RawMessage);
//			//Debug.Log("  string message:   {0}", data.MessageText);
//			//Debug.Log("  json data string: {0}", data.Json.ToJsonString());
//			//Debug.Log("  json raw:         {0}", data.Json.Args[0]);
//			
//			// cast message as Part - use type cast helper
//			Part part = data.Json.GetFirstArgAs<Part>();
//			Debug.Log(" Part Level:   {0}\r\n", part.Level);
//		});
//		
//		// make the socket.io connection
//		socket.Connect();

//		SimpleListenerExample(new string[]{"http://localhost:1234/"});
	}



//	// This example requires the System and System.Net namespaces. 
//	public static void SimpleListenerExample(string[] prefixes)
//	{
//		if (!HttpListener.IsSupported)
//		{
//			Console.WriteLine ("Windows XP SP2 or Server 2003 is required to use the HttpListener class.");
//			return;
//		}
//		// URI prefixes are required, 
//		// for example "http://contoso.com:8080/index/".
//		if (prefixes == null || prefixes.Length == 0)
//			throw new ArgumentException("prefixes");
//		
//		// Create a listener.
//		HttpListener listener = new HttpListener();
//		// Add the prefixes. 
//		foreach (string s in prefixes)
//		{
//			listener.Prefixes.Add(s);
//		}
//		listener.Start();
//		Console.WriteLine("Listening...");
//		// Note: The GetContext method blocks while waiting for a request. 
//		HttpListenerContext context = listener.GetContext();
//		HttpListenerRequest request = context.Request;
//		// Obtain a response object.
//		HttpListenerResponse response = context.Response;
//		// Construct a response. 
//		string responseString = "<HTML><BODY> Hello world!</BODY></HTML>";
//		byte[] buffer = System.Text.Encoding.UTF8.GetBytes(responseString);
//		// Get a response stream and write the response to it.
//		response.ContentLength64 = buffer.Length;
//		System.IO.Stream output = response.OutputStream;
//		output.Write(buffer,0,buffer.Length);
//		// You must close the output stream.
//		output.Close();
//		listener.Stop();
//	}
//
//	// Update is called once per frame
//	void Update () {
//	
//	}
}
