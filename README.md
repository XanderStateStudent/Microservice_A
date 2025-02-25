This is my communication contract.
README must contain...

* Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.
Do not advise your teammate to use your test program or require them to, your teammate must write all of their own code.

This microservice displays a notification.
To use, have your program open up the pipeline text file.
The provided file is called: pipeline.txt
Then have your program write to the file the message
that your wish to display in the notification.
Once the text is written to the file,
the microservice will read it and display the notification.

Example call: 
pipeline = open("pipeline.txt", w)
pipeline.write("notification message")

* Clear instructions for how to programmatically RECEIVE data from the microservice you implemented. Include an example call.

There is not data that is received to the program directly. The only received data is notification window.

* UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand.

  (INSERT IMAGE OF DIAGRAM)
  /UML.Diagram.png
