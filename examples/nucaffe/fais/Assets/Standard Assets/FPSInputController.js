private var motor : CharacterMotor;
private var moveX : float;
private var moveY : float;
private var jump  : boolean;
private var isRemoteMove;

// Use this for initialization
function Awake () {
	motor = GetComponent(CharacterMotor);
}

public function SetMove(x : float, y : float, _jump : boolean) {
	moveX = x;
	moveY = y;
	jump = _jump;
	isRemoteMove = true;
}

// Update is called once per frame
function Update () {
	// Get the input vector from server, keyboard, or analog stick
	var directionVector;
	if(isRemoteMove) {
		directionVector = new Vector3(moveX, 0, moveY);
		motor.inputJump = jump;
		isRemoteMove = false;
	} else {
		directionVector = new Vector3(Input.GetAxis("Horizontal"), 0, Input.GetAxis("Vertical"));
		motor.inputJump = Input.GetButton("Jump");
	}
	
	if (directionVector != Vector3.zero) {
		// Get the length of the directon vector and then normalize it
		// Dividing by the length is cheaper than normalizing when we already have the length anyway
		var directionLength = directionVector.magnitude;
		directionVector = directionVector / directionLength;
		
		// Make sure the length is no bigger than 1
		directionLength = Mathf.Min(1, directionLength);
		
		// Make the input vector more sensitive towards the extremes and less sensitive in the middle
		// This makes it easier to control slow speeds when using analog sticks
		directionLength = directionLength * directionLength;
		
		// Multiply the normalized direction vector by the modified length
		directionVector = directionVector * directionLength;
	}
	
	// Apply the direction to the CharacterMotor
	motor.inputMoveDirection = transform.rotation * directionVector;
}

// Require a character controller to be attached to the same game object
@script RequireComponent (CharacterMotor)
@script AddComponentMenu ("Character/FPS Input Controller")
