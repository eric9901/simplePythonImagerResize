# ImagerResizer
Resize all image form input folder to telegram maximun size(512X512)pixel, and output to outputfolder save as png format<br \>
Using OpenCV for resize<br \>
Support docker version for different environment <br \>
docker use:<br \>
open cmd<br \>
docker run --rm -it -v youinputfolderlocation:/app/Input -v youroutputfolderlocation:/app/Output resizer:1<br \>
docker option command<br \>
sh open terimal and can type command<br \>
"%cd%"=current location in cmd<br \>
$(pwd)=current location in powershell