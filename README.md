# Overview

This Choregraphe (v2.5) project makes use of HTML/Javascript to implement various persuasion techniques for petition participation through Pepper robot, as part of the Social Robot Social Influence research.

During interaction, Pepper will first persuade participants based on the script and animation in choregraphe and guide participant to start petition flow on tablet. 
If participant decide to start petition, they can further change the strength of sign or reject.If signed, petition progress will be shown and user feedback will be collected.
All these tablet interaction will be recorded as a csv file on Pepper's tablet, the file can then be send into the data processor python file to further visualise and summarise the responses.

To install this package on a Pepper robot, open the [Petition.pml] file in Choregraphe. Then use the upload to robot feature to send the package to the robot. This will add a launcher entry on the tablet of the robot which when selected will start the behavior.

This project was developed based on the [Pepper Tablet Survey tool](https://github.com/tianleimin/PepperTabletSurvey).
