using UnityEngine;
using System.Collections;

public class CenterOfView : MonoBehaviour {
	
	public Vector3 focusPoint;
	public bool didCollide;
	public Vector3 forward;

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
		RaycastHit hit;
		didCollide = Physics.Raycast(transform.position, transform.forward, out hit);
//		Debug.Log(didCollide);
		if(didCollide) {
//			Debug.Log(hit.point);
			focusPoint = hit.point;
		} else {
			forward = transform.forward;
		}
	}
}
