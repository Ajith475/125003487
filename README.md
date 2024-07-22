Now We can created a Backend which has the language model and where we are conversation is happening
Here Two python files Text.py and Text2.py
These are used to convert the Given audio to a text 
Now this Text is given to language model to give a response
The language model has been used and checked using the hugging face app and which returns the Response for the input given by the user and understands the question and give a approprioate answer in text.
Now the text answer is given to python file to convert into audio
This Happens in the backend

Now in the frontend We have created a webpage for the Voice Conversation
We have created a audio inout component which gets audio from user and convert this into wav format for python input
Now fectch button gives the output audio to the user 
Here also description of ai keys also included here
Here css and javascript are used for it
And it is fetched for the output audio
Run in any browser to see the webpage

Here the problem is when a sample audio file of wav format is given to backend and run with comman node backend.js it runs perfectly and the voice response for the question is generated correctly 
But when it integrated with the frontend the audio file doesnt get transfer to the frontend and makes a error in the backend,but backend runs here also perfectly and webpage also works perfectly

This is the only problem Faced by me
