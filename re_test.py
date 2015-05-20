emphasis_pattern = re.compile(r'''
	\*	#Beginning emphasis tag -- an asterisk
	(	#Begin group for capturing phrse
	[^\*]+ # Capture anything except astericks
	)	#End group
	\*  # Ending emphasis tag
'''), re.VERBOSE