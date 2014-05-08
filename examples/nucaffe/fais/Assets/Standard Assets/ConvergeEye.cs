using UnityEngine;
using System.Collections;

public class ConvergeEye : MonoBehaviour {

	public CenterOfView centerOfView;

	// Use this for initialization
	void Start () {
	}
	
	// Update is called once per frame
	void Update () {
		if(centerOfView.didCollide) {
//			Debug.Log(transform.name + " focusing on " + centerOfView.focusPoint + " by shifting to: " + transform.forward);
			transform.LookAt(centerOfView.focusPoint);
		} else {
//			Debug.Log(transform.name + " aligning to " + centerOfView.forward + " by shifting to: " + transform.forward);
			transform.forward = centerOfView.forward;
		}
	}
}
