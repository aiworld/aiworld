using UnityEngine;
using System.Collections.Generic;

public class GameSoundManager : MonoBehaviour 
{
	public AudioClip[] clips;
	
	static private Dictionary<string, AudioClip> _clips;
	
	private void Awake() 
	{
		_clips = new Dictionary<string, AudioClip>();
		
		for(int i = 0; i < clips.Length; i++)
		{
			if(!_clips.ContainsKey(clips[i].name))
			{
				_clips.Add(clips[i].name, clips[i]);
			}
		}
	}
	
	static public AudioClip GetClip(string name)
	{
		if(_clips == null) return null;
		
		if(!_clips.ContainsKey(name)) return null;
		
		return _clips[name];
	}
}
